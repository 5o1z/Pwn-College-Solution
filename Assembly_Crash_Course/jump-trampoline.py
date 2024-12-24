# Now, we will combine the two prior levels and perform the following:

# Create a two jump trampoline:
# - Make the first instruction in your code a jmp.
# - Make that jmp a relative jump to 0x51 bytes from its current position.
# - At 0x51, write the following code:
#   + Place the top value on the stack into register rdi.
#   + jmp to the absolute address 0x403000.

from pwn import *

p = process('/challenge/./run')

code = asm('''
    jmp $ + 0x53
    .rept 0x51
    nop
    .endr

target:
    pop rdi
    mov rax, 0x403000
    jmp rax
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
