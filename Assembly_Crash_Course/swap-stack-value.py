# In this level, we are going to explore the last in first out (LIFO) property of the stack.

# Using only the following instructions:

# push
# pop
# Swap values in rdi and rsi.

# Example:

# If to start rdi = 2 and rsi = 5
# Then to end rdi = 5 and rsi = 2

from pwn import *

p = process('/challenge/./run')

code = asm('''
        push rdi
        push rsi

        pop rdi
        pop rsi
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
