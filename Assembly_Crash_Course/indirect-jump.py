# Using the jump table, we can greatly reduce the amount of cmps we use.
# Now all we need to check is if number is greater than 2. If it is, always do:
# jmp [0x1337+0x18]

# Otherwise:
# jmp [jump_table_address + number * 8]

# if rdi is 0:
#   jmp 0x40301e
# else if rdi is 1:
#   jmp 0x4030da
# else if rdi is 2:
#   jmp 0x4031d5
# else if rdi is 3:
#   jmp 0x403268
# else:
#   jmp 0x40332c

# Assume rdi will NOT be negative.
# Use no more than 1 cmp instruction.
# Use no more than 3 jumps (of any variant).
# We will provide you with the number to 'switch' on in rdi.
# We will provide you with a jump table base address in rsi.

from pwn import *

p = process('/challenge/./run')

code = asm('''
        cmp rdi, 3
        jg default
        jmp [rsi + rdi*8]

default:
        jmp [rsi +4*8]
''', arch='amd64', os='linux')

p.send(code)
p.interactive()
