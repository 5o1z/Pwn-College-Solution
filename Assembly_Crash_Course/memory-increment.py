# Please perform the following:

# Place the value stored at 0x404000 into rax.
# Increment the value stored at the address 0x404000 by 0x1337.
# Make sure the value in rax is the original value stored at 0x404000 and make sure that [0x404000] now has the incremented value.

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
