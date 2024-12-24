# Another cool concept in x86 is the ability to independently access the lower register bytes.
# Each register in x86_64 is 64 bits in size, and in the previous levels, we have accessed the full register using rax, rdi, or rsi.
# We can also access the lower bytes of each register using different register names.
# For example, the lower 32 bits of rax can be accessed using eax, the lower 16 bits using ax, and the lower 8 bits using al.
# MSB                                    LSB
# +----------------------------------------+
# |                   rax                  |           <- 64 bit (8 bytes)
# +--------------------+-------------------+
#                      |        eax        |           <- 32 bit (4 bytes)
#                      +---------+---------+
#                                |   ax    |           <- 16 bit (2 bytes)
#                                +----+----+
#                                | ah | al |           <- 8 bit  (1 byte)
#                                +----+----+

# Lower register bytes access is applicable to almost all registers.
# Using only one move instruction, please set the upper 8 bits of the ax register to 0x42.
from pwn import *

p = process(['/challenge/./run'])

code = asm('''
        mov ah, 0x42
''',arch = 'amd64',os = 'linux')

p.send(code)
p.interactive()
