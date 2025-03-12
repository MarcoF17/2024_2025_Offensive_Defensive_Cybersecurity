import z3
from pwn import *

#Create symbolic input
a1 = [z3.BitVec(f"c_{i}", 32) for i in range(29)]

solver = z3.Solver()

#each byte should be printable
for bitvec in a1:
    solver.add(bitvec >= 0x20, bitvec <= 0x7e)
    
#add constraints
#check 1
solver.add(a1[5] == 45, a1[11] == 45, a1[17]  == 45, a1[23] == 45)

#check 2
solver.add(a1[1] - 48 <= 9)
solver.add(a1[4] - 48 <= 9)
solver.add(a1[6] - 48 <= 9)
solver.add(a1[9] - 48 <= 9)
solver.add(a1[15] - 48 <= 9)
solver.add(a1[18] - 48 <= 9)
solver.add(a1[22] - 48 <= 9)
solver.add(a1[27] - 48 <= 9)
solver.add(a1[28] - 48 <= 9)

#check 3
solver.add(a1[4] - 48 == 2 * (a1[1] - 48) + 1, a1[4] - 48 > 7, a1[9] == a1[4] - (a1[1] - 48) + 2)

#check 4
solver.add(((a1[27]) + (a1[28])) % 13 == 8)

#check 5
solver.add(((a1[27]) + (a1[22])) % 22 == 18)

#check 6
solver.add((a1[18] + (a1[22])) % 11 == 5)

#check 7
solver.add((a1[22] + a1[28] + a1[18]) % 26 == 4)

#check 8
solver.add((a1[1] + a1[4] * a1[6]) % 41 == 5)

#check 9
solver.add(((a1[15]) - (a1[28])) % 4 == 1)

#check A
solver.add(((a1[22]) + (a1[4])) % 4 == 3)

#check B
solver.add((a1[20]) == 66, (a1[21]) == 66)

#check C
solver.add((a1[6] + a1[15] * a1[9]) % 10 == 1)

#check D
solver.add((a1[15] + a1[4] + a1[27] - 18 ) % 16 == 8)

#check E
v1 = z3.If(a1[28] < a1[9], z3.BitVecVal(1, 32), z3.BitVecVal(0, 32))
solver.add(((v1 + a1[28] - a1[9]) & 1) - v1 == 1)

#check F
solver.add(a1[0] == 77)

check = solver.check()
print(check)

prodkey = ''
for i in range(29):
    prodkey += chr(solver.model()[a1[i]].as_long())
    
print(f"Found prodkey {prodkey}")

c = remote("prodkey.training.offensivedefensive.it", 8080, ssl = True)

c.recvuntil(b"continue: ")
c.sendline(prodkey.encode())

c.interactive()
