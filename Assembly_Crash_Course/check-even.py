from pwn import *

p = process('/challenge/./run')

# if x is even then
#   y = 1
# else
#   y = 0
# --> Use AND to take low bit (0 is even & 1 is odd) --> Use XOR with 1 (to change 0 to 1 & 1 to 0)
code = asm('''
    and rdi, 1
    xor rdi, 1
    xor rax, rax
    or rax, rdi
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
