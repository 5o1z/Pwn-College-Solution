# Here are some useful instructions:

# add reg1, reg2 <=> reg1 += reg2
# sub reg1, reg2 <=> reg1 -= reg2
# imul reg1, reg2 <=> reg1 *= reg2
# div is more complicated, and we will discuss it later. Note: all regX can be replaced by a constant or memory location.

# Do the following:
# Add 0x331337 to rdi

from pwn import *

p = process(['/challenge/./run'])

code = asm('''
 add rdi, 0x331337
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
