.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n1 I from Label0 to Label1
.var 2 is n2 I from Label0 to Label1
.var 3 is n3 I from Label0 to Label1
.var 4 is i I from Label0 to Label1
.var 5 is number I from Label0 to Label1
	iconst_0
	istore_1
	iconst_1
	istore_2
	bipush 10
	istore 5
	iload_1
	invokestatic io/putInt(I)V
	iload_2
	invokestatic io/putInt(I)V
	iconst_3
	istore 4
Label4:
	iload 4
	iload 5
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iload_1
	iload_2
	iadd
	istore_3
	iload_3
	invokestatic io/putIntLn(I)V
	iload_2
	istore_1
	iload_3
	istore_2
Label6:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 5
.limit locals 6
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
