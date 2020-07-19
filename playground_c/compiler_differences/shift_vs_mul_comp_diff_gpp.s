	.file	"shift_vs_mul_comp_diff.c"
	.def	___main;	.scl	2;	.type	32;	.endef
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
	pushl	%ebp
	movl	%esp, %ebp
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$42, 8(%esp)
	movl	$0, 12(%esp)
	movl	8(%esp), %eax
	movl	12(%esp), %edx
	shldl	$1, %eax, %edx
	addl	%eax, %eax
	movl	%eax, 8(%esp)
	movl	%edx, 12(%esp)
	movl	8(%esp), %eax
	movl	12(%esp), %edx
	shldl	$1, %eax, %edx
	addl	%eax, %eax
	movl	%eax, 8(%esp)
	movl	%edx, 12(%esp)
	movl	$0, %eax
	leave
	ret
	.ident	"GCC: (tdm-1) 4.9.2"
