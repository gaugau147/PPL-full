import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_var(self):
        input = """int a;"""
        expect = str(Program([VarDecl("a",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    def test_var1(self):
        input = """float a;"""
        expect = str(Program([VarDecl("a",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    
    def test_var2(self):
        input = """boolean a;"""
        expect = str(Program([VarDecl("a",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    
    def test_var3(self):
        input = """string a;"""
        expect = str(Program([VarDecl("a",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    
    def test_var4(self):
        input = """int a; int b;"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    
    def test_var5(self):
        input = """int a,b;"""
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    
    # def test_var6(self):
    #     input = """int a,b[5];"""
    #     expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(IntLiteral(5),IntType()))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_random(self):
        input = """void Plus(int a[]){1+1;}"""
        expect = str(Program([FuncDecl(Id("Plus"),[VarDecl("a",ArrayPointerType(IntType()))],VoidType(),Block([BinaryOp("+",IntLiteral(1),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_random1(self):
        input = """int boring(){}"""
        expect = str(Program([FuncDecl(Id("boring"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_random2(self):
        input = """int boring(int a){}"""
        expect = str(Program([FuncDecl(Id("boring"),[VarDecl("a",IntType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_random3(self):
        input = """int boring(int a, int b){}"""
        expect = str(Program([FuncDecl(Id("boring"),[VarDecl("a",IntType()),VarDecl("b",IntType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_random4(self):
        input = """int boring(int a[]){}"""
        expect = str(Program([FuncDecl(Id("boring"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_random5(self):
        input = """int boring(int a, int b[], float c[]){}"""
        expect = str(Program([FuncDecl(Id("boring"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(IntType())),VarDecl("c",ArrayPointerType(FloatType()))],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_random6(self):
        input = """int[] boring(int _b_[]){}"""
        expect = str(Program([FuncDecl(Id("boring"),[VarDecl("_b_",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    # def test_random7(self):
    #     input = """int boring(int a, int b, int e[]){int c[3];}"""
    #     expect = str(Program([FuncDecl(Id("boring"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("e",ArrayPointerType(IntType()))],IntType(),Block([VarDecl("c",ArrayType(IntLiteral(3),IntType()))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_random8(self):
        input = """int[] boring(int bored[]){int a; int b;}"""
        expect = str(Program([FuncDecl(Id("boring"),[VarDecl("bored",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([VarDecl("a",IntType()),VarDecl("b",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_random9(self):
        input = """int[] boring(int bored[]){return a;}"""
        expect = str(Program([FuncDecl(Id("boring"),[VarDecl("bored",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Return(Id("a"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_random10(self):
        input = """void boring(){return;}"""
        expect = str(Program([FuncDecl(Id("boring"),[],VoidType(),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_random11(self):
        input = """int boring(){if (a>0) a = 5; else a = -5;}"""
        expect = str(Program([FuncDecl(Id("boring"),[],IntType(),Block([If(BinaryOp(">",Id("a"),IntLiteral(0)),BinaryOp("=",Id("a"),IntLiteral(5)),BinaryOp("=",Id("a"),UnaryOp("-",IntLiteral(5))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_random12(self):
        input = """int test(){b = 1; a = 5*(a + b);}"""
        expect = str(Program([FuncDecl(Id("test"),[],IntType(),Block([BinaryOp("=",Id("b"),IntLiteral(1)),BinaryOp("=",Id("a"),BinaryOp("*",IntLiteral(5),BinaryOp("+",Id("a"),Id("b"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_random13(self):
        input = """int test(){b = 1; a = 5*(a + b)/2 - c*b;}"""
        expect = str(Program([FuncDecl(Id("test"),[],IntType(),Block([BinaryOp("=",Id("b"),IntLiteral(1)),BinaryOp("=",Id("a"),BinaryOp("-",BinaryOp("/",BinaryOp("*",IntLiteral(5),BinaryOp("+",Id("a"),Id("b"))),IntLiteral(2)),BinaryOp("*",Id("c"),Id("b"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    # def test_random14(self):
    #     input = """int test(){string a[20]; a = "Test string";}"""
    #     expect = str(Program([FuncDecl(Id("test"),[],IntType(),Block([VarDecl("a",ArrayType(IntLiteral(20),StringType())),BinaryOp("=",Id("a"),StringLiteral("Test string"))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_random15(self):
        input = """int test() {if (a>0) return a; else return b;}"""
        expect = str(Program([FuncDecl(Id("test"),[],IntType(),Block([If(BinaryOp(">",Id("a"),IntLiteral(0)),Return(Id("a")),Return(Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_random16(self):
        input = """int test() {if (a>10 || a<100) return a; else return b;}"""
        expect = str(Program([FuncDecl(Id("test"),[],IntType(),Block([If(BinaryOp("||",BinaryOp(">",Id("a"),IntLiteral(10)),BinaryOp("<",Id("a"),IntLiteral(100))),Return(Id("a")),Return(Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_random17(self):
        input = """int test(){do a=a*b; while a != c ;}"""
        expect = str(Program([FuncDecl(Id("test"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("*",Id("a"),Id("b")))],BinaryOp("!=",Id("a"),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_random18(self):
        input = """int test(){do i = i + 1; if(i==5) break; while i != 10;}"""
        expect = str(Program([FuncDecl(Id("test"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp("==",Id("i"),IntLiteral(5)),Break())],BinaryOp("!=",Id("i"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_random19(self):
        input = """int test(){do i = i + 1; if(i==5) continue; while i != 10;}"""
        expect = str(Program([FuncDecl(Id("test"),[],IntType(),Block([Dowhile([BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If(BinaryOp("==",Id("i"),IntLiteral(5)),Continue())],BinaryOp("!=",Id("i"),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_random20(self):
        input = """int test(int a, float b[]) {combo(2,3);}"""
        expect = str(Program([FuncDecl(Id("test"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([CallExpr(Id("combo"),[IntLiteral(2),IntLiteral(3)])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_random21(self):
        input = """int test(int a, float b[]) {combo((2+5),3/3);}"""
        expect = str(Program([FuncDecl(Id("test"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([CallExpr(Id("combo"),[BinaryOp("+",IntLiteral(2),IntLiteral(5)),BinaryOp("/",IntLiteral(3),IntLiteral(3))])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_random22(self):
        input = """int test(int a, float b[]){2*a+b[2]*2/5;}"""
        expect = str(Program([FuncDecl(Id("test"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([BinaryOp("+",BinaryOp("*",IntLiteral(2),Id("a")),BinaryOp("/",BinaryOp("*",ArrayCell(Id("b"),IntLiteral(2)),IntLiteral(2)),IntLiteral(5)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    # def test_random23(self):
    #     input = """int test(){a+b*5 = 5*2-7+1.7;}"""
    #     expect = str(Program([FuncDecl(Id("test"),[],IntType(),Block([BinaryOp("=",BinaryOp("+",Id("a"),BinaryOp("*",Id("b"),IntLiteral(5))),BinaryOp("+",BinaryOp("-",BinaryOp("*",IntLiteral(5),IntLiteral(2)),IntLiteral(7)),FloatLiteral(1.7)))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_random24(self):
        input = """void test1(int a[]){} void test2(int b){}"""
        expect = str(Program([FuncDecl(Id("test1"),[VarDecl("a",ArrayPointerType(IntType()))],VoidType(),Block([])),FuncDecl(Id("test2"),[VarDecl("b",IntType())],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_random25(self):
        # MC page 12
        input = """int test(){foo(2)[3+x] = a[b[2]]+3;}"""
        expect = str(Program([FuncDecl(Id("test"),[],IntType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_random26(self):
        input = """int main()    
                {    
                 int a1,a2,a3,i,number;    
                 for(i=2;i<number;i=i+1)   
                 {    
                  a3=a1+a2;    
                  printf(a3);  
                 }  
                 return 0;  
                 }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a1",IntType()),VarDecl("a2",IntType()),VarDecl("a3",IntType()),VarDecl("i",IntType()),VarDecl("number",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(2)),BinaryOp("<",Id("i"),Id("number")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",Id("a3"),BinaryOp("+",Id("a1"),Id("a2"))),CallExpr(Id("printf"),[Id("a3")])])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    # def test_random27(self):
    #     # MC page 9
    #     input = """int[] foo(int a, float b[]){int c[3]; if (a>0) foo(a-1,b); return c;}"""
    #     expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([VarDecl("c",ArrayType(IntLiteral(3),IntType())),If(BinaryOp(">",Id("a"),IntLiteral(0)),CallExpr(Id("foo"),[BinaryOp("-",Id("a"),IntLiteral(1)),Id("b")])),Return(Id("c"))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_random28(self):
        input = """int foo(int a, float b[])    
                {
                    boolean c;
                    int i;
                    i = a + 3 ;
                    if (i >0){
                        int d;
                        d = i + 3;
                        putInt(d);
                        }
                    return i;
                }"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(FloatType()))],IntType(),Block([VarDecl("c",BoolType()),VarDecl("i",IntType()),BinaryOp("=",Id("i"),BinaryOp("+",Id("a"),IntLiteral(3))),If(BinaryOp(">",Id("i"),IntLiteral(0)),Block([VarDecl("d",IntType()),BinaryOp("=",Id("d"),BinaryOp("+",Id("i"),IntLiteral(3))),CallExpr(Id("putInt"),[Id("d")])])),Return(Id("i"))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))
    
    def test_random29(self):
      
        input = """int main()    
                {    
                    int n,r,sum,temp;    
                    printf("enter the number=");    
                    scanf(n);    
                    temp=n;
                    do					
                    {    
                        r=n%10;    
                        sum=(sum*10)+r;    
                        n=n/10;    
                    }
                    while(n>0);   
                    if(temp==sum)    
                        printf("palindrome number");    
                    else    
                        printf("isnot palindrome");   
                    return 0;  
                }   """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),VarDecl("r",IntType()),VarDecl("sum",IntType()),VarDecl("temp",IntType()),CallExpr(Id("printf"),[StringLiteral("enter the number=")]),CallExpr(Id("scanf"),[Id("n")]),BinaryOp("=",Id("temp"),Id("n")),Dowhile([Block([BinaryOp("=",Id("r"),BinaryOp("%",Id("n"),IntLiteral(10))),BinaryOp("=",Id("sum"),BinaryOp("+",BinaryOp("*",Id("sum"),IntLiteral(10)),Id("r"))),BinaryOp("=",Id("n"),BinaryOp("/",Id("n"),IntLiteral(10)))])],BinaryOp(">",Id("n"),IntLiteral(0))),If(BinaryOp("==",Id("temp"),Id("sum")),CallExpr(Id("printf"),[StringLiteral("palindrome number")]),CallExpr(Id("printf"),[StringLiteral("isnot palindrome")])),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))
   