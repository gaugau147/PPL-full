.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arrStr [Ljava/lang/String;
.field static arrA [I
.field static arrB [I
.field static arrFloat1 [F
.field static arrFloat2 [F
.field static arrBoo1 [Z
.field static arrBoo2 [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 1
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
	bipush 10
	anewarray java/lang/String
	putstatic MCClass/arrStr [Ljava/lang/String;
	iconst_5
	newarray int
	putstatic MCClass/arrA [I
	iconst_4
	newarray int
	putstatic MCClass/arrB [I
	iconst_1
	newarray float
	putstatic MCClass/arrFloat1 [F
	iconst_2
	newarray float
	putstatic MCClass/arrFloat2 [F
	iconst_2
	newarray boolean
	putstatic MCClass/arrBoo1 [Z
	iconst_3
	newarray boolean
	putstatic MCClass/arrBoo2 [Z
Label1:
	return
.limit stack 1
.limit locals 0
.end method
