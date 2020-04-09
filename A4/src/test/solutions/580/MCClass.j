.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is year I from Label0 to Label1
	sipush 2019
	istore_1
	iload_1
	iconst_4
	irem
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	ldc "not a leap year"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label5
Label4:
	iload_1
	bipush 100
	irem
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	ldc "leap year"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label9
Label8:
	iload_1
	sipush 400
	irem
	iconst_0
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	ldc "not a leap year"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label13
Label12:
	ldc "leap year"
	invokestatic io/putString(Ljava/lang/String;)V
Label13:
Label9:
Label5:
Label1:
	return
.limit stack 7
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
