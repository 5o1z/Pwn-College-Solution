# Relative jumps: jump + or - the next instruction.
# Absolute jumps: jump to a specific address.
# Indirect jumps: jump to the memory address specified in a register.

# In x86, absolute jumps (jump to a specific address) are accomplished by first putting the target address in a register reg, then doing jmp reg.

from pwn import *

p = process('/challenge/./run')

code = asm('''
    mov rax , 0x403000
    jmp rax
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
