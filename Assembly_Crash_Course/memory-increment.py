from pwn import *

p = process('/challenge/./run')

code = asm('''
    xor rax, rax
    xor rbx, rbx

    mov rax, [0x404000]
    mov rbx, 0x1337
    add [0x404000], rbx
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
