from pwn import *

p = process(['/challenge/./run'])

code = asm('''
 add rdi, 0x331337
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
