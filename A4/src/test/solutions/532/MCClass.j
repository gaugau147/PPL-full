.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 11
	bipush 22
	iadd
	bipush 33
	iconst_4
	idiv
	iadd
	invokestatic io/putIntLn(I)V
	ldc 1.25
	ldc 3.75
	fadd
	invokestatic io/putFloatLn(F)V
	ldc "Print this one"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_0
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
