.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
	bipush 10
	istore_1
	bipush 20
	istore_2
	iload_1
	invokestatic io/putIntLn(I)V
	iload_2
	invokestatic io/putIntLn(I)V
	iload_1
	iload_2
	iadd
	istore_1
	iload_1
	iload_2
	isub
	istore_2
	iload_1
	iload_2
	isub
	istore_1
	ldc "After:"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iload_1
	invokestatic io/putIntLn(I)V
	iload_2
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 3
.limit locals 3
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
