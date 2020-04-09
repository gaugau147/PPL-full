.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n1 I from Label0 to Label1
.var 2 is n2 I from Label0 to Label1
.var 3 is i I from Label0 to Label1
.var 4 is gcd I from Label0 to Label1
	bipush 81
	istore_1
	sipush 153
	istore_2
	iconst_1
	istore 4
	iconst_2
	istore_3
Label6:
	iload_3
	iload_1
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload_3
	iload_2
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iand
	ifle Label7
	iload_1
	iload_3
	irem
	iconst_0
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	iload_2
	iload_3
	irem
	iconst_0
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	iand
	ifgt Label14
	goto Label15
Label14:
	iload_3
	istore 4
Label15:
Label8:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label6
Label7:
Label9:
	iload 4
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 11
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
