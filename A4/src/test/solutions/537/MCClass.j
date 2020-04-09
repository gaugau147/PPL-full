.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	iconst_2
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iconst_1
	iconst_0
	if_icmpeq Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iand
	ifgt Label6
	goto Label7
Label6:
	ldc "Print this"
	invokestatic io/putString(Ljava/lang/String;)V
Label7:
	ldc "This one!"
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 8
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
