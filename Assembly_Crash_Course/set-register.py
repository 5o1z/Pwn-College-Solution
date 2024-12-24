# In this level, you will work with registers! Please set the following:

# rdi = 0x1337
from pwn import *

p = process(['/challenge/./run'])

code = asm("mov rdi,0x1337", arch='amd64', os='linux')

p.send(code)
p.interactive()
