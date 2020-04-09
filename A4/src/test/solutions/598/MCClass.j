.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is flag Z from Label0 to Label1
.var 2 is arr [Z from Label0 to Label1
	iconst_5
	newarray boolean
	astore_2
	iconst_3
	iconst_2
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	dup
	istore_1
	aload_2
	iconst_2
	aload_2
	iconst_1
	aload_2
	iconst_0
	iconst_3
	iconst_2
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	dup
	istore_1
	dup_x2
	bastore
	dup_x2
	bastore
	bastore
	aload_2
	iconst_0
	baload
	invokestatic io/putBool(Z)V
	aload_2
	iconst_1
	baload
	invokestatic io/putBool(Z)V
	aload_2
	iconst_2
	baload
	invokestatic io/putBool(Z)V
	iload_1
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 21
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
