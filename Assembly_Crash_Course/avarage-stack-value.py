from pwn import *

p = process('/challenge/./run')

code = asm('''
    mov rax, [RSP + 0]
    mov rbx, [RSP + 8]
    mov rcx, [RSP + 16]
    mov rdx, [RSP + 24]

    add rax, rbx
    add rax, rcx
    add rax, rdx

    xor rdx, rdx
    mov rbx, 4
    idiv rbx

    push rax
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
