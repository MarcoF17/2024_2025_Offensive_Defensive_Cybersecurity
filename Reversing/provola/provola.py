from libdebug import debugger
import string

d = debugger("./provola")

flag = "$"*37

maxc = 0

def hit(t, bp):
    #print("HIT")
    pass

for i in range(37):
    for c in string.printable:
        new_flag = flag[:i] + c + flag[i+1:]
    
        r = d.run()
        bp = d.bp(0x1A0F, file="provola", callback=hit)
        d.cont()

        r.recvuntil(b'password')
        r.sendline(new_flag.encode())

        d.wait()
        d.kill()

        if bp.hit_count > maxc:
            maxc = bp.hit_count
            flag = new_flag
            print(f"New flag: {flag}")