from pwn import *

p = process('/challenge/./run')

code = asm('''
    jmp $ + 0x53
    .rept 0x51
    nop
    .endr

target:
    mov rax, 0x1
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
