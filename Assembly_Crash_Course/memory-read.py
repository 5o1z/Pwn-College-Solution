from pwn import *

p = process('/challenge/./run')

code = asm('''
    xor rax, rax
    mov rax, [0x404000]
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
