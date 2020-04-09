.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is low I from Label0 to Label1
.var 2 is high I from Label0 to Label1
.var 3 is i I from Label0 to Label1
.var 4 is flag I from Label0 to Label1
	iconst_0
	istore 4
	bipush 20
	istore_1
	bipush 50
	istore_2
	iconst_0
	istore 4
	iconst_2
	istore_3
Label8:
	iload_3
	iload_1
	iconst_2
	idiv
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label9
	iload_1
	iload_3
	irem
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
	iconst_1
	istore 4
	goto Label11
Label15:
Label10:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label8
Label9:
Label11:
	iload 4
	iconst_0
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifgt Label18
	goto Label19
Label18:
	iload_1
	invokestatic io/putInt(I)V
Label19:
	iload_1
	iconst_1
	iadd
	istore_1
Label4:
Label5:
Label20:
	iload_1
	iload_2
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label21
	iconst_0
	istore 4
	iconst_2
	istore_3
Label26:
	iload_3
	iload_1
	iconst_2
	idiv
	if_icmpgt Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label27
	iload_1
	iload_3
	irem
	iconst_0
	if_icmpne Label30
	iconst_1
	goto Label31
Label30:
	iconst_0
Label31:
	ifgt Label32
	goto Label33
Label32:
	iconst_1
	istore 4
	goto Label29
Label33:
Label28:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label26
Label27:
Label29:
	iload 4
	iconst_0
	if_icmpne Label34
	iconst_1
	goto Label35
Label34:
	iconst_0
Label35:
	ifgt Label36
	goto Label37
Label36:
	iload_1
	invokestatic io/putInt(I)V
Label37:
	iload_1
	iconst_1
	iadd
	istore_1
Label22:
	goto Label20
Label21:
Label23:
Label1:
	return
.limit stack 17
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
