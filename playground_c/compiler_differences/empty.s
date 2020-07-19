	.file	"empty.c"
	.def	___main;	.scl	2;	.type	32;	.endef
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
	pushl	%ebp
	movl	%esp, %ebp
	andl	$-16, %esp
	call	___main
	movl	$0, %eax
	leave
	ret
	.ident	"GCC: (tdm-1) 4.9.2"
