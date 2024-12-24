# Please perform the following: Place the value stored at 0x404000 into rax.
# Make sure the value in rax is the original value stored at 0x404000.
from pwn import *

p = process('/challenge/./run')

code = asm('''
    xor rax, rax
    mov rax, [0x404000]
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
