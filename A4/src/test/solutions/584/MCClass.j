.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is num [I from Label0 to Label1
	bipush 50
	newarray int
	astore_3
.var 4 is sum I from Label0 to Label1
.var 5 is avg F from Label0 to Label1
	iconst_0
	istore 4
	bipush 50
	istore_1
	ldc 0.0
	fstore 5
	iconst_0
	istore_2
Label4:
	iload_2
	iload_1
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	aload_3
	iload_2
	iload_2
	iastore
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label5:
Label7:
	iconst_0
	istore_2
Label10:
	iload_2
	iload_1
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label11
	iload 4
	aload_3
	iload_2
	iaload
	iadd
	istore 4
Label12:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label10
Label11:
Label13:
	iload 4
	iload_1
	idiv
	i2f
	fstore 5
	fload 5
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 9
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
