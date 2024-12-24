# Hint: it may require some tricks to assign a big constant to a dereferenced register.
# Try setting a register to the constant value then assigning that register to the dereferenced register.

# We will now set the following in preparation for your code:
#   [0x4047c0] = 0xffffffffffffffff
#   [0x404a28] = 0xffffffffffffffff
#   rdi = 0x4047c0
#   rsi = 0x404a28

from pwn import *

p = process('/challenge/./run')

code = asm('''
        xor rax, rax
        mov rax, 0xdeadbeef00001337
        mov [rdi], rax
        mov rax, 0xc0ffee0000
        mov [rsi], rax
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
