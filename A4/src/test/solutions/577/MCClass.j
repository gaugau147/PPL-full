.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
.var 2 is reverse I from Label0 to Label1
.var 3 is rem I from Label0 to Label1
	iconst_0
	istore_2
	bipush 123
	istore_1
	iload_1
	bipush 10
	irem
	istore_3
	iload_2
	bipush 10
	imul
	iload_3
	iadd
	istore_2
	iload_1
	bipush 10
	idiv
	istore_1
Label4:
Label5:
Label6:
	iload_1
	iconst_0
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label7
	iload_1
	bipush 10
	irem
	istore_3
	iload_2
	bipush 10
	imul
	iload_3
	iadd
	istore_2
	iload_1
	bipush 10
	idiv
	istore_1
Label8:
	goto Label6
Label7:
Label9:
	iload_2
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 6
.limit locals 4
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
