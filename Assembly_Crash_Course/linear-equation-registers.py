# Using your new knowledge, please compute the following:

# f(x) = mx + b, where:
# m = rdi
# x = rsi
# b = rdx
# Place the result into rax.

# Note: There is an important difference between mul (unsigned multiply) and imul (signed multiply) in terms of which registers are used.
# Look at the documentation on these instructions to see the difference.

# In this case, you will want to use imul.

from pwn import *

p = process(['/challenge/./run'])

code = asm('''
 mov rax, rdi
 imul rax,rsi
 add rax, rdx
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
