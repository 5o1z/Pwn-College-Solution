# If we have x % y, and y is a power of 2, such as 2^n, the result will be the lower n bits of x

# Example:
# For x % 256, the value of 256 is 2^8. This means that the result of the rdi % 256 operation is the value of the lowest 8 bits of the rdi register.
# Similarly, for x % 65536, the value of 65536 is 2^16. The result of rsi % 65536 is the value of the lowest 16 bits of the rsi register

from pwn import *

p = process(['/challenge/./run'])

code = asm('''
    mov    al, dil
    mov    bx, si
    ''', arch = 'amd64',os = 'linux')

p.send(code)
p.interactive()
