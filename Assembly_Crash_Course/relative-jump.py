# Useful instructions for this level:

# jmp (reg1 | addr | offset)
# nop
# Hint: For the relative jump, look up how to use labels in x86.

# Using the above knowledge, perform the following:

# - Make the first instruction in your code a jmp.
# - Make that jmp a relative jump to 0x51 bytes from the current position.
# - At the code location where the relative jump will redirect control flow, set rax to 0x1.

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
