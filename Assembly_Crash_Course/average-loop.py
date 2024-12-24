# rdi = memory address of the 1st quad word
# rsi = n (amount to loop for)
# rax = average computed

from pwn import *

p = process('/challenge/./run')

code = asm('''
      xor rcx, rcx
      xor rax, rax
      mov rdx, rsi

loop:
      add rax, [rdi + rcx * 8]
      inc rcx
      cmp rcx, rdx
      jle loop

      xor rdx, rdx
      div rsi
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
