# Assume each dereferenced value is a signed dword. This means the values can start as a negative value at each memory position.

from pwn import *

p = process('/challenge/./run')

code = asm('''
        xor rax, rax
        mov esi, [rdi]
        mov ebx, [rdi+4]
        mov edx, [rdi+8]
        mov ecx, [rdi+12]

        cmp esi, 0x7f454c46
        je add

        cmp esi, 0x00005A4D
        je sub

        mov eax, ebx
        imul eax, edx
        imul eax, ecx
        jmp done

add:
        mov eax, ebx
        add eax, edx
        add eax, ecx
        jmp done
sub:
        mov eax, ebx
        sub eax, edx
        sub eax, ecx

done:
        nop

''', arch='amd64', os='linux')

p.send(code)
p.interactive()
