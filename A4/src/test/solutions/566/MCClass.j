.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a F
.field static b F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	i2f
	putstatic MCClass/a F
	getstatic MCClass/a F
	invokestatic io/putFloat(F)V
	getstatic MCClass/a F
	iconst_1
	i2f
	fadd
	putstatic MCClass/b F
	getstatic MCClass/b F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 3
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
