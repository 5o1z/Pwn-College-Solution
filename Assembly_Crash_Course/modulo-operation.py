# Modulo in assembly is another interesting concept!
# x86 allows you to get the remainder after a div operation.
# For instance: 10 / 3 results in a remainder of 1.
# The remainder is the same as modulo, which is also called the "mod" operator.
# In most programming languages, we refer to mod with the symbol %.
# Please compute the following: rdi % rsi
# Place the value in rax.

from pwn import *

p = process(['/challenge/./run'])

code = asm('''
        mov rax,rdi
        div rsi
        mov rax, rdx
''',arch = 'amd64',os = 'linux')

p.send(code)
p.interactive()
