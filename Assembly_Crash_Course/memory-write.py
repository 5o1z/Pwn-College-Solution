# Please perform the following: Place the value stored in rax to 0x404000.
from pwn import *

p = process('/challenge/./run')

code = asm('''
    mov [0x404000], rax
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
