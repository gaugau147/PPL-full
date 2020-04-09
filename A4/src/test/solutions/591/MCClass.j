.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arrStr [Ljava/lang/String; from Label0 to Label1
	bipush 10
	anewarray java/lang/String
	astore_1
.var 2 is arrA [I from Label0 to Label1
	iconst_5
	newarray int
	astore_2
.var 3 is arrB [I from Label0 to Label1
	iconst_4
	newarray int
	astore_3
.var 4 is arrFloat1 [F from Label0 to Label1
	iconst_1
	newarray float
	astore 4
.var 5 is arrFloat2 [F from Label0 to Label1
	iconst_2
	newarray float
	astore 5
.var 6 is arrBoo1 [Z from Label0 to Label1
	iconst_2
	newarray boolean
	astore 6
.var 7 is arrBoo2 [Z from Label0 to Label1
	iconst_3
	newarray boolean
	astore 7
Label1:
	return
.limit stack 1
.limit locals 8
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
