.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is dividend I from Label0 to Label1
.var 2 is divisor I from Label0 to Label1
.var 3 is quotient I from Label0 to Label1
.var 4 is remainder I from Label0 to Label1
	bipush 25
	istore_1
	iconst_4
	istore_2
	iload_1
	iload_2
	idiv
	istore_3
	iload_1
	iload_2
	irem
	istore 4
	iload_3
	invokestatic io/putIntLn(I)V
	iload 4
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
.limit locals 5
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
