# In this level you will be working with functions! This will involve manipulating the instruction pointer (rip),
# as well as doing harder tasks than normal. You may be asked to use the stack to store values
# or call functions that we provide you.

# In previous levels you implemented a while loop to count the number of
# consecutive non-zero bytes in a contiguous region of memory.

# In this level you will be provided with a contiguous region of memory again and will loop
# over each performing a conditional operation till a zero byte is reached.
# All of which will be contained in a function!

# A function is a callable segment of code that does not destroy control flow.
# Functions use the instructions "call" and "ret".

# The "call" instruction pushes the memory address of the next instruction onto
# the stack and then jumps to the value stored in the first argument.

# Let's use the following instructions as an example:
#   0x1021 mov rax, 0x400000
#   0x1028 call rax
#   0x102a mov [rsi], rax

# 1. call pushes 0x102a, the address of the next instruction, onto the stack.
# 2. call jumps to 0x400000, the value stored in rax.

# The "ret" instruction is the opposite of "call".

# ret pops the top value off of the stack and jumps to it.

# Let's use the following instructions and stack as an example:

#                               Stack ADDR  VALUE
#   0x103f mov rax, rdx         RSP + 0x8   0xdeadbeef
#   0x1042 ret                  RSP + 0x0   0x0000102a

# Here, ret will jump to 0x102a

# Please implement the following logic:
#   str_lower(src_addr):
#     i = 0
#     if src_addr != 0:
#       while [src_addr] != 0x00:
#         if [src_addr] <= 0x5a:
#           [src_addr] = foo([src_addr])
#           i += 1
#         src_addr += 1
#     return i

# foo is provided at 0x403000.
# foo takes a single argument as a value and returns a value.

# All functions (foo and str_lower) must follow the Linux amd64 calling convention (also known as System V AMD64 ABI):
#   https://en.wikipedia.org/wiki/X86_calling_conventions#System_V_AMD64_ABI

# Therefore, your function str_lower should look for src_addr in rdi and place the function return in rax.

# An important note is that src_addr is an address in memory (where the string is located) and [src_addr] refers to the byte that exists at src_addr.

# Therefore, the function foo accepts a byte as its first argument and returns a byte.

# We will now run multiple tests on your code, here is an example run:
#   (data) [0x404000] = {10 random bytes},
#   rdi = 0x404000

from pwn import *

p = process('/challenge/./run')

code = asm('''
str_lower:
        mov rbx, 0x403000
        xor rax, rax
        xor rcx, rcx
        test rdi, rdi
        jz done
proc_string:
        mov al, byte ptr [rdi]
        test al, al
        jz done

        cmp al, 0x5A
        jg skip

        mov rsi, rdi
        mov dil, al
        call rbx

        mov rdi, rsi
        mov byte ptr [rdi], al

        inc rcx
skip:
        inc rdi
        jmp proc_string
done:
        mov rax, rcx
        ret
''', arch='amd64', os='linux')

p.send(code)
p.interactive()

# Executing your code...
# 0x400000:    mov       rbx, 0x403000
# 0x400007:    xor       rax, rax
# 0x40000a:    xor       rcx, rcx
# 0x40000d:    test      rdi, rdi
# 0x400010:    je        0x400031
# 0x400012:    mov       al, byte ptr [rdi]
# 0x400014:    test      al, al
# 0x400016:    je        0x400031
# 0x400018:    cmp       al, 0x5a
# 0x40001a:    jg        0x40002c
# 0x40001c:    mov       rsi, rdi
# 0x40001f:    mov       dil, al
# 0x400022:    call      rbx
# 0x400024:    mov       rdi, rsi
# 0x400027:    mov       byte ptr [rdi], al
# 0x400029:    inc       rcx
# 0x40002c:    inc       rdi
# 0x40002f:    jmp       0x400012
# 0x400031:    mov       rax, rcx
# 0x400034:    ret
