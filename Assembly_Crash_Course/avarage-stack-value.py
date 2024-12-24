# Similar to the memory levels, we can use [rsp] to access the value at the memory address in rsp.

# Without using pop, please calculate the average of 4 consecutive quad words stored on the stack.
# Push the average on the stack.

# Hint:
# RSP+0x?? Quad Word A
# RSP+0x?? Quad Word B
# RSP+0x?? Quad Word C
# RSP Quad Word D

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
