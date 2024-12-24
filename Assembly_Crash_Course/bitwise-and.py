# Set rax to the value of (rdi AND rsi)
from pwn import *

p = process('/challenge/./run')

# Use AND operate
# Clear rax register with XOR
# Copy rdi to rax using OR
code = asm('''
    and rdi, rsi
    xor rax, rax
    or rax, rdi
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
