from pwn import *

p = process(['/challenge/./run'])

code = asm('''
 mov rax,rdi
 div rsi
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
