.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n1 F from Label0 to Label1
.var 2 is n2 F from Label0 to Label1
.var 3 is n3 F from Label0 to Label1
	ldc 1.1
	fstore_1
	ldc 10.56
	fstore_2
	ldc 100.01
	fstore_3
	fload_1
	fload_2
	fcmpl
	iflt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	fload_1
	fload_3
	fcmpl
	iflt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iand
	ifgt Label6
	goto Label7
Label6:
	ldc "n1 is largest"
	invokestatic io/putString(Ljava/lang/String;)V
Label7:
	fload_2
	fload_1
	fcmpl
	iflt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	fload_2
	fload_3
	fcmpl
	iflt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	iand
	ifgt Label12
	goto Label13
Label12:
	ldc "n2 is largest"
	invokestatic io/putString(Ljava/lang/String;)V
Label13:
	fload_3
	fload_1
	fcmpl
	iflt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	fload_3
	fload_2
	fcmpl
	iflt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	iand
	ifgt Label18
	goto Label19
Label18:
	ldc "n3 is largest"
	invokestatic io/putString(Ljava/lang/String;)V
Label19:
Label1:
	return
.limit stack 14
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
