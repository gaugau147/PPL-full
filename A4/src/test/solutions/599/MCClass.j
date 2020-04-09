.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static check(I)Ljava/lang/String;
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	ldc "The number is POSITIVE"
	areturn
Label4:
	iload_0
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	ldc "The number is NEGATIVE"
	areturn
Label8:
	ldc "The number is ZERO"
	areturn
Label9:
Label5:
Label1:
.limit stack 7
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n1 I from Label0 to Label1
.var 2 is n2 I from Label0 to Label1
.var 3 is n3 I from Label0 to Label1
	iconst_5
	ineg
	istore_1
	iconst_0
	istore_2
	bipush 14
	istore_3
	iload_1
	invokestatic MCClass/check(I)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iload_2
	invokestatic MCClass/check(I)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iload_3
	invokestatic MCClass/check(I)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
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
