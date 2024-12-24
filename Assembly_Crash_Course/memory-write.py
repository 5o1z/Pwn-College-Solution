from pwn import *

p = process('/challenge/./run')

code = asm('''
    mov [0x404000], rax
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
