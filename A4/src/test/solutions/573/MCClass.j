.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
.var 2 is r I from Label0 to Label1
.var 3 is sum I from Label0 to Label1
.var 4 is temp I from Label0 to Label1
	iconst_0
	istore_3
	sipush 12321
	istore_1
	iload_1
	istore 4
	iload_1
	bipush 10
	irem
	istore_2
	iload_3
	bipush 10
	imul
	iload_2
	iadd
	istore_3
	iload_1
	bipush 10
	idiv
	istore_1
Label4:
Label5:
Label6:
	iload_1
	iconst_0
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label7
	iload_1
	bipush 10
	irem
	istore_2
	iload_3
	bipush 10
	imul
	iload_2
	iadd
	istore_3
	iload_1
	bipush 10
	idiv
	istore_1
Label8:
	goto Label6
Label7:
Label9:
	iload 4
	iload_3
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	ldc "not palindrome"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label13
Label12:
	ldc "palindrome number"
	invokestatic io/putString(Ljava/lang/String;)V
Label13:
Label1:
	return
.limit stack 6
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
