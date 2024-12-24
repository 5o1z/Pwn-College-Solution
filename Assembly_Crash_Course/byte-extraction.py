# Shifting bits around in assembly is another interesting concept!
# x86 allows you to 'shift' bits around in a register.
# Take, for instance, al, the lowest 8 bits of rax.
# The value in al (in bits) is:
# rax = 10001010
# If we shift once to the left using the shl instruction:
# shl al, 1
# The new value is:
# al = 00010100
# Everything shifted to the left, and the highest bit fell off while a new 0 was added to the right side.
# You can use this to do special things to the bits you care about.
# Shifting has the nice side effect of doing quick multiplication (by 2) or division (by 2), and can also be used to compute modulo.

from pwn import *

p = process(['/challenge/./run'])

code = asm('''
    shr rdi, 32
    mov al, dil
    ''', arch = 'amd64',os = 'linux')

p.send(code)
p.interactive()
