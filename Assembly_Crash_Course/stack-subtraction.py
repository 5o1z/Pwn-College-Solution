from pwn import *

p = process('/challenge/./run')

code = asm('''
        xor rax, rax
        pop rax
        sub rax, rdi
        push rax
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
