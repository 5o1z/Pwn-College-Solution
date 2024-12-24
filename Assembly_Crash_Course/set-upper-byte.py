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

from pwn import *

p = process(['/challenge/./run'])

code = asm('''
        mov ah, 0x42
''',arch = 'amd64',os = 'linux')

p.send(code)
p.interactive()
