from pwn import *

#print_flag offset = 0x1309 -> 4873

elf = ELF('./the_adder')

print(hex(elf.symbols['main']))

