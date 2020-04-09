.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
	iconst_1
	istore_1
Label4:
	iload_1
	iconst_3
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iconst_1
	istore_2
Label10:
	iload_2
	iconst_3
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label11
	iload_1
	invokestatic io/putInt(I)V
	iload_2
	invokestatic io/putIntLn(I)V
Label12:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label10
Label11:
Label13:
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 7
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
