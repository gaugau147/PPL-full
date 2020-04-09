.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [I from Label0 to Label1
	iconst_5
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_1
	iastore
	aload_1
	iconst_0
	iaload
	invokestatic io/putInt(I)V
.var 2 is i I from Label0 to Label1
	iconst_1
	istore_2
	aload_1
	iload_2
	iconst_2
	iastore
	aload_1
	iload_2
	iconst_1
	iadd
	iconst_3
	iastore
	aload_1
	iload_2
	iconst_2
	iadd
	iconst_4
	iastore
	aload_1
	iload_2
	iaload
	invokestatic io/putInt(I)V
	aload_1
	iload_2
	iconst_1
	iadd
	iaload
	invokestatic io/putInt(I)V
	aload_1
	iload_2
	iconst_2
	iadd
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 9
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
