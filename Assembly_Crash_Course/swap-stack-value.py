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
