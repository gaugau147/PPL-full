.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is sum I from Label0 to Label1
	iconst_0
	istore_3
	bipush 10
	istore_1
	iconst_1
	istore_2
Label4:
	iload_2
	iload_1
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iload_3
	iload_2
	iadd
	istore_3
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label5:
Label7:
	iload_3
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 5
.limit locals 4
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
