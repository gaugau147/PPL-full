.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [Ljava/lang/String; from Label0 to Label1
	iconst_5
	anewarray java/lang/String
	astore_1
	aload_1
	iconst_2
	aload_1
	iconst_1
	aload_1
	iconst_0
	ldc "Hello"
	dup_x2
	aastore
	dup_x2
	aastore
	aastore
	aload_1
	iconst_0
	aaload
	invokestatic io/putString(Ljava/lang/String;)V
	aload_1
	iconst_1
	aaload
	invokestatic io/putString(Ljava/lang/String;)V
	aload_1
	iconst_2
	aaload
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 17
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
