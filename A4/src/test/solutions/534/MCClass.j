.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
.var 2 is b F from Label0 to Label1
.var 3 is c Ljava/lang/String; from Label0 to Label1
.var 4 is d Z from Label0 to Label1
	bipush 10
	istore_1
	iload_1
	i2f
	ldc 0.25
	fadd
	fstore_2
	ldc "a string"
	astore_3
	iload_1
	i2f
	fload_2
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore 4
	iload 4
	invokestatic io/putBoolLn(Z)V
	aload_3
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
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
