	.file	"compiler_differences.c"
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
	movb	$1, 15(%esp)
	movb	$1, 14(%esp)
	movb	$0, 13(%esp)
	movl	$0, 8(%esp)
	cmpb	$0, 15(%esp)
	je	L2
	cmpb	$0, 14(%esp)
	je	L2
	cmpb	$0, 13(%esp)
	je	L2
	movl	$1, 8(%esp)
	jmp	L3
L2:
	cmpb	$0, 15(%esp)
	je	L4
	cmpb	$0, 14(%esp)
	je	L4
	movzbl	13(%esp), %eax
	xorl	$1, %eax
	testb	%al, %al
	je	L4
	movl	$2, 8(%esp)
	jmp	L3
L4:
	cmpb	$0, 15(%esp)
	je	L3
	movzbl	14(%esp), %eax
	xorl	$1, %eax
	testb	%al, %al
	je	L3
	movzbl	13(%esp), %eax
	xorl	$1, %eax
	testb	%al, %al
	je	L3
	movl	$3, 8(%esp)
L3:
	movl	$0, %eax
	leave
	ret
	.ident	"GCC: (tdm-1) 4.9.2"
