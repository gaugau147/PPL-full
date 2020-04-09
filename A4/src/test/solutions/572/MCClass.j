.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is m I from Label0 to Label1
.var 4 is flag I from Label0 to Label1
	iconst_0
	istore_3
	iconst_0
	istore 4
	bipush 44
	istore_1
	iload_1
	iconst_2
	idiv
	istore_3
	iconst_2
	istore_2
Label4:
	iload_2
	iload_3
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iload_1
	iload_2
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
	ldc "44 is not prime"
	invokestatic io/putString(Ljava/lang/String;)V
	iconst_1
	istore 4
	goto Label7
Label11:
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label5:
Label7:
	iload 4
	iconst_0
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	goto Label15
Label14:
	ldc "Number is prime"
	invokestatic io/putString(Ljava/lang/String;)V
Label15:
Label1:
	return
.limit stack 7
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
