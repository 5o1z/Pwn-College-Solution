# The first quad words are stored from offset 0 -> 7.
# The next quad words are stored from 8 -> 15.

from pwn import *

p = process('/challenge/./run')

code = asm('''
        xor rax, rax
        mov rax, [rdi] # First quad words (8 bytes)
        mov rbx, [rdi+8] # Second quad words
        add rax, rbx
        mov [rsi], rax
''', arch='amd64', os='linux')

p.send(code)
p.interactive()

