.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static pow(II)I
.var 0 is base I from Label0 to Label1
.var 1 is exp I from Label0 to Label1
Label0:
.var 2 is result I from Label0 to Label1
	iconst_1
	istore_2
	iload_2
	iload_0
	imul
	istore_2
	iload_1
	iconst_1
	isub
	istore_1
Label4:
Label5:
Label6:
	iload_1
	iconst_0
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label7
	iload_2
	iload_0
	imul
	istore_2
	iload_1
	iconst_1
	isub
	istore_1
Label8:
	goto Label6
Label7:
Label9:
	iload_2
	ireturn
Label1:
.limit stack 6
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	iconst_4
	invokestatic MCClass/pow(II)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
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
