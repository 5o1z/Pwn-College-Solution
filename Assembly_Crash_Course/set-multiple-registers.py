from pwn import *

p = process(['/challenge/./run'])

code = asm('''
 mov rax, 0x1337
 mov r12, 0xCAFED00D1337BEEF
 mov rsp, 0x31337
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
