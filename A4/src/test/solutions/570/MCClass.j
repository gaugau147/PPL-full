.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo()I
Label0:
	iconst_1
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	bipush 10
	newarray int
	astore_1
	aload_1
	iconst_1
	aload_1
	iconst_0
	iconst_1
	dup_x2
	iastore
	iastore
	aload_1
	iconst_0
	iaload
	aload_1
	iconst_1
	iaload
	iadd
	aload_1
	invokestatic MCClass/foo()I
	iaload
	iadd
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 11
.limit locals 2
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
