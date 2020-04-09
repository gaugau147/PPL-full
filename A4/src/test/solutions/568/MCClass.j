.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/a [I
	iconst_1
	getstatic MCClass/a [I
	iconst_0
	iconst_1
	dup_x2
	iastore
	iastore
	getstatic MCClass/a [I
	iconst_0
	iaload
	getstatic MCClass/a [I
	iconst_1
	iaload
	iadd
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 11
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
	newarray int
	putstatic MCClass/a [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
