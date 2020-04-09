import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_program1(self):
        input = """int[] foo(int a[]){return a;}
            void main(){
                int a[10];
                foo(a)[0] = 1;
            }"""
        expect = str(Program([VarDecl('a',IntType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

'''
    def test_program1(self):
        input = """int a;  """
        expect = str(Program([VarDecl('a',IntType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_var_declare1(self):
        input = """ int a, b;
                float c, d; """
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',FloatType()),VarDecl('d',FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_func_declare1(self):
        input = """ int main(){ } """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_func_declare2(self):
        input = """ int foo(int a){ } """
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_func_declare3(self):
        input = """ int foo(int a){ int b; } """
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType())],IntType(),Block([VarDecl('b',IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_func_declare4(self):
        input = """ int foo(int a, int b[]){ int c; } """
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',ArrayPointerType(IntType()))],IntType(),Block([VarDecl('c',IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_func_declare5(self):
        input = """ int[] foo(int a, float b[]){ }  """
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_assignment_stmt1(self):
        input = """ int foo(int a){ a = a + 1; } """
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType())],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_assignment_stmt2(self):
        input = """ int main(){ a = 1; } """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_assignment_stmt3(self):
        input = """ int main(){ a = b = 1; } """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('=',Id('b'),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))
    
    def test_assignment_stmt4(self):
        input = """ int main(){ a = b[2] = 1; } """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('=',ArrayCell(Id('b'),IntLiteral(2)),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_assignment_stmt5(self):
        input = """ int main(){ a = b[2] = boo(3)[4]; } """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('=',ArrayCell(Id('b'),IntLiteral(2)),ArrayCell(CallExpr(Id('boo'),[IntLiteral(3)]),IntLiteral(4))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_assignment_stmt6(self):
        input = """int main(){
                    s = "this is a string";
                    f = 1.2;
                    a = b = d[10] = 100;
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('s'),StringLiteral('this is a string')),BinaryOp('=',Id('f'),FloatLiteral(1.2)),BinaryOp('=',Id('a'),BinaryOp('=',Id('b'),BinaryOp('=',ArrayCell(Id('d'),IntLiteral(10)),IntLiteral(100))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_assignment_stmt7(self):
        input = """int foo(int a[], int b){
                    a = func(b,c);
            }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',ArrayPointerType(IntType())),VarDecl('b',IntType())],IntType(),Block([BinaryOp('=',Id('a'),CallExpr(Id('func'),[Id('b'),Id('c')]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_assignment_stmt8(self):
        input = """int main(){
                    a = func(func(b)[100]);
                    a[10] = b[10] = 1.1e10;
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),CallExpr(Id('func'),[ArrayCell(CallExpr(Id('func'),[Id('b')]),IntLiteral(100))])),BinaryOp('=',ArrayCell(Id('a'),IntLiteral(10)),BinaryOp('=',ArrayCell(Id('b'),IntLiteral(10)),FloatLiteral(1.1e10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_expression_stmt1(self):
        input = """int main(){
                    flag = a >= b;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('flag'),BinaryOp('>=',Id('a'),Id('b')))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_expression_stmt2(self):
        input = """int main(){
                    flag = a >= b || c && d == e;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('flag'),BinaryOp('||',BinaryOp('>=',Id('a'),Id('b')),BinaryOp('&&',Id('c'),BinaryOp('==',Id('d'),Id('e')))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_expression_stmt3(self):
        input = """int main(){
                    a = b*c + d*e*f - (h+2)*3;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('-',BinaryOp('+',BinaryOp('*',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',Id('d'),Id('e')),Id('f'))),BinaryOp('*',BinaryOp('+',Id('h'),IntLiteral(2)),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))
    
    def test_expression_stmt4(self):
        input = """int main(){
                    a = d*e/f - (h+2/a/b%2)*3;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('-',BinaryOp('/',BinaryOp('*',Id('d'),Id('e')),Id('f')),BinaryOp('*',BinaryOp('+',Id('h'),BinaryOp('%',BinaryOp('/',BinaryOp('/',IntLiteral(2),Id('a')),Id('b')),IntLiteral(2))),IntLiteral(3))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_expression_stmt5(self):
        input = """int main(){
                    a = d * -e;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('*',Id('d'),UnaryOp('-',Id('e'))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_if_statement1(self):
        input = """int main(){
                    if (true)
                        a = 10;
                    else
                        a = a + 1;
                    int b;
                        
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BooleanLiteral(True),BinaryOp('=',Id('a'),IntLiteral(10)),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1)))),VarDecl('b',IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_if_statement2(self):
        input = """int main(){
                    if (true) {
                        a = 10;
                        b = 10;
                    }
                    else
                        a = a + 1;
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BooleanLiteral(True),Block([BinaryOp('=',Id('a'),IntLiteral(10)),BinaryOp('=',Id('b'),IntLiteral(10))]),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_if_statement3(self):
        input = """int main(){
                    if (true)
                    {a = 10;}
                    else
                    a = a + 1;
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BooleanLiteral(True),Block([BinaryOp('=',Id('a'),IntLiteral(10))]),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_if_statement4(self):
        input = """int main(){
                    if (a=10) a = 10;
                    else {a = 0; b = 10;}
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('=',Id('a'),IntLiteral(10)),BinaryOp('=',Id('a'),IntLiteral(10)),Block([BinaryOp('=',Id('a'),IntLiteral(0)),BinaryOp('=',Id('b'),IntLiteral(10))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_if_statement5(self):
        input = """int main(){
                    if (a>=b)
                        a = 100;
                    b = a;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('>=',Id('a'),Id('b')),BinaryOp('=',Id('a'),IntLiteral(100))),BinaryOp('=',Id('b'),Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_if_statement6(self):
        input = """int main(){
                    if (a != true)
                        a = false;
                    else {
                        a = 10;
                        b = 100;
                    }
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('!=',Id('a'),BooleanLiteral(True)),BinaryOp('=',Id('a'),BooleanLiteral(False)),Block([BinaryOp('=',Id('a'),IntLiteral(10)),BinaryOp('=',Id('b'),IntLiteral(100))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_if_statement7(self):
        input = """int main(){
                    if (a == 10)
                        a = false;
                    else if (a == 11)
                        a = 10;
                    else
                        b = 100;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('==',Id('a'),IntLiteral(10)),BinaryOp('=',Id('a'),BooleanLiteral(False)),If(BinaryOp('==',Id('a'),IntLiteral(11)),BinaryOp('=',Id('a'),IntLiteral(10)),BinaryOp('=',Id('b'),IntLiteral(100))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_if_statement8(self):
        input = """int main(){
                    if (a<10)
                        print("This is a test case");
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('<',Id('a'),IntLiteral(10)),CallExpr(Id('print'),[StringLiteral("This is a test case")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_func_declare6(self):
        input = """ int foo(int a, int c[]){
                    foo2(b);
                }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('c',ArrayPointerType(IntType()))],IntType(),Block([CallExpr(Id('foo2'),[Id('b')])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_if_statement9(self):
        input = """int main() {
                    if (a+b>c+d-e*3){
                        a = 10;
                    }
                    else
                        a = 100;
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('>',BinaryOp('+',Id('a'),Id('b')),BinaryOp('-',BinaryOp('+',Id('c'),Id('d')),BinaryOp('*',Id('e'),IntLiteral(3)))),Block([BinaryOp('=',Id('a'),IntLiteral(10))]),BinaryOp('=',Id('a'),IntLiteral(100)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_if_statement10(self):
        input = """int main(){
                    if (foo(3) == foo (4) && foo(5) != foo(6)){
                        print("it's true");
                    }
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('&&',BinaryOp('==',CallExpr(Id('foo'),[IntLiteral(3)]),CallExpr(Id('foo'),[IntLiteral(4)])),BinaryOp('!=',CallExpr(Id('foo'),[IntLiteral(5)]),CallExpr(Id('foo'),[IntLiteral(6)]))),Block([CallExpr(Id('print'),[StringLiteral("it's true")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))
    
    def test_if_statement11(self):
        input = """int main(){
                    if(foo()) {
                        a = 10;
                    }
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(CallExpr(Id('foo'),[]),Block([BinaryOp('=',Id('a'),IntLiteral(10))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_if_statement12(self):
        input = """int main(){
                    a = true;
                    if (a){
                        a == false;
                    }
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BooleanLiteral(True)),If(Id('a'),Block([BinaryOp('==',Id('a'),BooleanLiteral(False))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))
    
    def test_do_while_stmt1(self):
        input = """int main(){
                    do 
                        y = 10;
                    while (true);
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([BinaryOp('=',Id('y'),IntLiteral(10))],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_do_while_stmt2(self):
        input = """int main(){
                    do { }
                    while (true);
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Block([])],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_do_while_stmt3(self):
        input = """int main(){
                    do { }{ }
                    while true ;
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Block([]),Block([])],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))


    def test_do_while_stmt4(self):
        input = """int main() {
                    do {y = 10;}{}{string x;}
                    while(true);
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Block([BinaryOp('=',Id('y'),IntLiteral(10))]),Block([]),Block([VarDecl('x',StringType())])],BooleanLiteral('true'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_do_while_stmt5(self):
        input = """int main(){
                    do y = true;
                    while (a*2 == 3 && c == d || g != h);
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([BinaryOp('=',Id('y'),BooleanLiteral(True))],BinaryOp('||',BinaryOp('&&',BinaryOp('==',BinaryOp('*',Id('a'),IntLiteral(2)),IntLiteral(3)),BinaryOp('==',Id('c'),Id('d'))),BinaryOp('!=',Id('g'),Id('h'))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_for_statement1(self):
        input = """int main(){
                for(a; a<10; a=a+1){
                    print("testing");
                }
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(Id('a'),BinaryOp('<',Id('a'),IntLiteral(10)),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),Block([CallExpr(Id('print'),[StringLiteral('testing')])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_for_statement2(self):
        input = """int main(){
                    for (a=10; a<100; a=a+1){
                        print("testing");
                    }
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(BinaryOp('=',Id('a'),IntLiteral(10)),BinaryOp('<',Id('a'),IntLiteral(100)),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),Block([CallExpr(Id('print'),[StringLiteral('testing')])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_for_statement3(self):
        input = """int main(){
                    for(a; a==100; a=a+1){ }
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(Id('a'),BinaryOp('==',Id('a'),IntLiteral(100)),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_break_statement(self):
        input = """int main(){
                    do break;
                    while true;
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Break()],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_continue_stmt(self):
        input = """int main(){
                    do continue;
                    while true;
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Continue()],BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_return_stmt(self):
        input = """int main(){
                    return;
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_func_call1(self):
        input = """int main(){
                    foo(a+1>b+c*3/2/3/d[c+d]);
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('foo'),[BinaryOp('>',BinaryOp('+',Id('a'),IntLiteral(1)),BinaryOp('+',Id('b'),BinaryOp('/',BinaryOp('/',BinaryOp('/',BinaryOp('*',Id('c'),IntLiteral(3)),IntLiteral(2)),IntLiteral(3)),ArrayCell(Id('d'),BinaryOp('+',Id('c'),Id('d'))))))])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))
    
    def test_func_call2(self):
        input = """int main(){
                    if(foo(3)>foo(2)+10){ }
                    else {foo(3)[a+b[foo(c)]];}
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('>',CallExpr(Id('foo'),[IntLiteral(3)]),BinaryOp('+',CallExpr(Id('foo'),[IntLiteral(2)]),IntLiteral(10))),Block([]),Block([ArrayCell(CallExpr(Id('foo'),[IntLiteral(3)]),BinaryOp('+',Id('a'),ArrayCell(Id('b'),CallExpr(Id('foo'),[Id('c')]))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))
    
    def test_func_call3(self):
        input = """int main(){
                    foo(3,a+b,c+d,4);
                    foo();
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('foo'),[IntLiteral(3),BinaryOp('+',Id('a'),Id('b')),BinaryOp('+',Id('c'),Id('d')),IntLiteral(4)]),CallExpr(Id('foo'),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))
    
    def test_func_call4(self):
        input = """int main(){
                    foo(3, foo(4, foo(5, foo(6, foo1(7)))));
                    return 3;
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('foo'),[IntLiteral(3),CallExpr(Id('foo'),[IntLiteral(4),CallExpr(Id('foo'),[IntLiteral(5),CallExpr(Id('foo'),[IntLiteral(6),CallExpr(Id('foo1'),[IntLiteral(7)])])])])]),Return(IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_func_call5(self):
        input = """int main(){
                    return foo(a,b,c,4,5,6);
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Return(CallExpr(Id('foo'),[Id('a'),Id('b'),Id('c'),IntLiteral(4),IntLiteral(5),IntLiteral(6)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_func_call6(self):
        input = """int main(){
                    a[foo()]==10;
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('==',ArrayCell(Id('a'),CallExpr(Id('foo'),[])),IntLiteral(10))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_var_declare2(self):
        input = """ int main() {
            int i, j, k;
            string s;
            }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('i',IntType()),VarDecl('j',IntType()),VarDecl('k',IntType()),VarDecl('s',StringType())]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_var_dec_3(self):
        input = """int a[10];"""
        expect = str(Program([VarDecl('a',ArrayType(10,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_var_dec_4(self):
        input = """int a, b[10], c;"""
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',ArrayType(10,IntType())),VarDecl('c',IntType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_var_dec_5(self):
        input = """ int a, b[10], c[1];
                    float d[3]; string f[4];"""
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',ArrayType(10, IntType())),VarDecl('c',ArrayType(1,IntType())),VarDecl('d',ArrayType(3,FloatType())),VarDecl('f',ArrayType(4,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_var_dec_6(self):
        input = """ int a, b[10];
                    float foo(int b[]){
                        string c[10];
                        c = b;
                        return c[1];
                    }"""
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',ArrayType(10,IntType())),FuncDecl(Id('foo'),[VarDecl('b',ArrayPointerType(IntType()))],FloatType(),Block([VarDecl('c',ArrayType(10,StringType())),BinaryOp('=',Id('c'),Id('b')),Return(ArrayCell(Id('c'),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_var_dec_7(self):
        input = """ int main(){ 
                        int a, b[10];
                        if (a>b[1]){ int c; c = a;}
                        else {int c[10]; c[0] = b;}
                    }
                    int d[10],c;"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),VarDecl('b',ArrayType(10,IntType())),If(BinaryOp('>',Id('a'),ArrayCell(Id('b'),IntLiteral(1))),Block([VarDecl('c',IntType()),BinaryOp('=',Id('c'),Id('a'))]),Block([VarDecl('c',ArrayType(10,IntType())),BinaryOp('=',ArrayCell(Id('c'),IntLiteral(0)),Id('b'))]))])),VarDecl('d',ArrayType(10,IntType())),VarDecl('c',IntType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_var_dec_8(self):
        input = """ float y;
                int main(){}
                void func(){}
                string z[2];
            """
        expect = str(Program([VarDecl('y',FloatType()),FuncDecl(Id('main'),[],IntType(),Block([])),FuncDecl(Id('func'),[],VoidType(),Block([])),VarDecl('z',ArrayType(2,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_expression_stmt6(self):
        input = """ int main() {
                        int a, b[10];
                        a = b || c && d || a > b || c<=d && a != e || g >= h && a > c && a - -a + (a||b) && a - !a && true || false;
                    }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),VarDecl('b',ArrayType(10,IntType())),BinaryOp('=',Id('a'),BinaryOp('||',BinaryOp('||',BinaryOp('||',BinaryOp('||',BinaryOp('||',Id('b'),BinaryOp('&&',Id('c'),Id('d'))),BinaryOp('>',Id('a'),Id('b'))),BinaryOp('&&',BinaryOp('<=',Id('c'),Id('d')),BinaryOp('!=',Id('a'),Id('e')))),BinaryOp('&&',BinaryOp('&&',BinaryOp('&&',BinaryOp('&&',BinaryOp('>=',Id('g'),Id('h')),BinaryOp('>',Id('a'),Id('c'))),BinaryOp('+',BinaryOp('-',Id('a'),UnaryOp('-',Id('a'))),BinaryOp('||',Id('a'),Id('b')))),BinaryOp('-',Id('a'),UnaryOp('!',Id('a')))),BooleanLiteral(True))),BooleanLiteral(False)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))  

    def test_bulk1(self):
        input = """ int a, b, c[10];
                    int foo(float a, float b){
                        return a+b;
                    }
                    int main(){
                        foo(3,5);
                    }
                """
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',ArrayType(10,IntType())),FuncDecl(Id('foo'),[VarDecl('a',FloatType()),VarDecl('b',FloatType())],IntType(),Block([Return(BinaryOp('+',Id('a'),Id('b')))])),FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('foo'),[IntLiteral(3),IntLiteral(5)])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))  
    
    def test_bulk2(self):
        input = """ void foo1(){
                        if (a==b)
                            b = c;
                        if (e!=f)
                            foo(a,b);
                    }"""
        expect = str(Program([FuncDecl(Id('foo1'),[],VoidType(),Block([If(BinaryOp('==',Id('a'),Id('b')),BinaryOp('=',Id('b'),Id('c'))),If(BinaryOp('!=',Id('e'),Id('f')),CallExpr(Id('foo'),[Id('a'),Id('b')]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))  

    def test_bulk3(self):
        input = """ void foo1(){
                        if (a==b)
                            b = c;
                        else 
                            foo(a,b);
                }"""
        expect = str(Program([FuncDecl(Id('foo1'),[],VoidType(),Block([If(BinaryOp('==',Id('a'),Id('b')),BinaryOp('=',Id('b'),Id('c')),CallExpr(Id('foo'),[Id('a'),Id('b')]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))  

    def test_bulk4(self):
        input = """ int main(){
                        if (a==b) {
                            if (c==d){
                                do { } while true ;
                            }
                        }
                        else c=1;
                    }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('==',Id('a'),Id('b')),Block([If(BinaryOp('==',Id('c'),Id('d')),Block([Dowhile([Block([])],BooleanLiteral(True))]))]),BinaryOp('=',Id('c'),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))  

    def test_bulk5(self):
        input = """ int a;
                    int foo(int x){return x;}
                    int main(){
                        int b;
                        b = foo(a);
                        getInt(b);
                        do {
                            int c;
                            int m;
                            int f;
                        }
                        while getInt(b);
                    }"""
        expect = str(Program([VarDecl('a',IntType()),FuncDecl(Id('foo'),[VarDecl('x',IntType())],IntType(),Block([Return(Id('x'))])),FuncDecl(Id('main'),[],IntType(),Block([VarDecl('b',IntType()),BinaryOp('=',Id('b'),CallExpr(Id('foo'),[Id('a')])),CallExpr(Id('getInt'),[Id('b')]),Dowhile([Block([VarDecl('c',IntType()),VarDecl('m',IntType()),VarDecl('f',IntType())])],CallExpr(Id('getInt'),[Id('b')]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))  

    def test_bulk6(self):
        input = """ string hello(int a, int b){
                    c = a+b;
                    putString("Hello World");
                }"""
        expect = str(Program([FuncDecl(Id('hello'),[VarDecl('a',IntType()),VarDecl('b',IntType())],StringType(),Block([BinaryOp('=',Id('c'),BinaryOp('+',Id('a'),Id('b'))),CallExpr(Id('putString'),[StringLiteral("Hello World")])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))  

    def test_bulk7(self):
        input = """ int a, b;
                    int sum(int a, int b) {return a+b;}
                    int main(){
                        putString("Enter a num: ");
                        getInt(a);
                        putString("Enter a num: ");
                        getInt(b);
                        putString("The sum of them is: ");
                        putInt(sum(a, b));
                    }"""
        expect = str(Program([VarDecl('a',IntType()),VarDecl('b',IntType()),FuncDecl(Id('sum'),[VarDecl('a',IntType()),VarDecl('b',IntType())],IntType(),Block([Return(BinaryOp('+',Id('a'),Id('b')))])),FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('putString'),[StringLiteral("Enter a num: ")]),CallExpr(Id('getInt'),[Id('a')]),CallExpr(Id('putString'),[StringLiteral("Enter a num: ")]),CallExpr(Id('getInt'),[Id('b')]),CallExpr(Id('putString'),[StringLiteral("The sum of them is: ")]),CallExpr(Id('putInt'),[CallExpr(Id('sum'),[Id('a'),Id('b')])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))  
    
    def test_bulk8(self):
        input = """ string first, last;
                    int main(){
                        first = "Edison";
                        last = "Thomas";
                        putString("Full name is: ");
                        putString(first);
                        putString(last);
                    }"""
        expect = str(Program([VarDecl('first',StringType()),VarDecl('last',StringType()),FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('first'),StringLiteral("Edison")),BinaryOp('=',Id('last'),StringLiteral("Thomas")),CallExpr(Id('putString'),[StringLiteral("Full name is: ")]),CallExpr(Id('putString'),[Id('first')]),CallExpr(Id('putString'),[Id('last')])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))  

    def test_bulk9(self):
        input = """ int main(){
                        a = a + b + c + 10 - 12 / 13 / 14.1 / 15.2 * 3 / 2 + foo()[foo()];
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('-',BinaryOp('+',BinaryOp('+',BinaryOp('+',Id('a'),Id('b')),Id('c')),IntLiteral(10)),BinaryOp('/',BinaryOp('*',BinaryOp('/',BinaryOp('/',BinaryOp('/',IntLiteral(12),IntLiteral(13)),FloatLiteral(14.1)),FloatLiteral(15.2)),IntLiteral(3)),IntLiteral(2))),ArrayCell(CallExpr(Id('foo'),[]),CallExpr(Id('foo'),[]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))  

    def test_bulk10(self):
        input = """ int main(){
                        a[b[19]] = 19;
                        a = foo(3);
                        b = a;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',ArrayCell(Id('a'),ArrayCell(Id('b'),IntLiteral(19))),IntLiteral(19)),BinaryOp('=',Id('a'),CallExpr(Id('foo'),[IntLiteral(3)])),BinaryOp('=',Id('b'),Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))  

    def test_bulk11(self):
        input = """ int main(){
                        if (a==b)
                            if (c==d)
                                e = f;
                            else i = 1;
                        else x = 2;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('==',Id('a'),Id('b')),If(BinaryOp('==',Id('c'),Id('d')),BinaryOp('=',Id('e'),Id('f')),BinaryOp('=',Id('i'),IntLiteral(1))),BinaryOp('=',Id('x'),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))  

    def test_bulk12(self):
        input =  """ int main(){
                        int a[10], i, j, temp;
                        for (i=0; i<10; i = i+1){
                            for (j=0; j<10; j = j+1){
                                if (a[i]>a[j]){
                                    temp = a[i];
                                    a[i] = a[j];
                                    a[j] = temp;
                                }
                            }
                        }
                    }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',ArrayType(10,IntType())),VarDecl('i',IntType()),VarDecl('j',IntType()),VarDecl('temp',IntType()),For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([For(BinaryOp('=',Id('j'),IntLiteral(0)),BinaryOp('<',Id('j'),IntLiteral(10)),BinaryOp('=',Id('j'),BinaryOp('+',Id('j'),IntLiteral(1))),Block([If(BinaryOp('>',ArrayCell(Id('a'),Id('i')),ArrayCell(Id('a'),Id('j'))),Block([BinaryOp('=',Id('temp'),ArrayCell(Id('a'),Id('i'))),BinaryOp('=',ArrayCell(Id('a'),Id('i')),ArrayCell(Id('a'),Id('j'))),BinaryOp('=',ArrayCell(Id('a'),Id('j')),Id('temp'))]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))  

    def test_bulk13(self):
        input = """ int sum(int a[], int m){
                        int sum;
                        sum = 0;
                        int i;
                        for (i=0; i<m; i=i+1){
                            sum = sum + a[i]; 
                        }
                        return sum;
                    }
                    int main(){
                        int a[10];
                        s = sum(a, 10);
                    }"""
        expect = str(Program([FuncDecl(Id('sum'),[VarDecl('a',ArrayPointerType(IntType())),VarDecl('m',IntType())],IntType(),Block([VarDecl('sum',IntType()),BinaryOp('=',Id('sum'),IntLiteral(0)),VarDecl('i',IntType()),For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),Id('m')),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([BinaryOp('=',Id('sum'),BinaryOp('+',Id('sum'),ArrayCell(Id('a'),Id('i'))))])),Return(Id('sum'))])),FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',ArrayType(10,IntType())),BinaryOp('=',Id('s'),CallExpr(Id('sum'),[Id('a'),IntLiteral(10)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))  
        
    def test_bulk14(self):
        input = """ int main(){
                        int a[10], sum, i;
                        sum = 0;
                        for (i=0; i<10; i=i+1)
                            sum = sum + a[i];
                        return sum;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',ArrayType(10,IntType())),VarDecl('sum',IntType()),VarDecl('i',IntType()),BinaryOp('=',Id('sum'),IntLiteral(0)),For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),BinaryOp('=',Id('sum'),BinaryOp('+',Id('sum'),ArrayCell(Id('a'),Id('i'))))),Return(Id('sum'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))  

    def test_bulk15(self):
        input = """ int foo(int a[], int n){
                        int sum, i;
                        s = 0;
                        for (i = 0; i<5; i=i+1){
                            if (a[i] % 2 == 0)
                                sum = sum + a[i];
                        }
                        return sum;
                }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',ArrayPointerType(IntType())),VarDecl('n',IntType())],IntType(),Block([VarDecl('sum',IntType()),VarDecl('i',IntType()),BinaryOp('=',Id('s'),IntLiteral(0)),For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),IntLiteral(5)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([If(BinaryOp('==',BinaryOp('%',ArrayCell(Id('a'),Id('i')),IntLiteral(2)),IntLiteral(0)),BinaryOp('=',Id('sum'),BinaryOp('+',Id('sum'),ArrayCell(Id('a'),Id('i')))))])),Return(Id('sum'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))  

    def test_bulk16(self):
        input = """ int foo(int n){
                        int i;
                        for(i=2; i<n-1; i=i+1){
                            if (n % i == 0)
                                return 0;
                            else
                                return 1;
                        }
                }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('n',IntType())],IntType(),Block([VarDecl('i',IntType()),For(BinaryOp('=',Id('i'),IntLiteral(2)),BinaryOp('<',Id('i'),BinaryOp('-',Id('n'),IntLiteral(1))),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([If(BinaryOp('==',BinaryOp('%',Id('n'),Id('i')),IntLiteral(0)),Return(IntLiteral(0)),Return(IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))  

    def test_bulk17(self):
        input = """ boolean foo(int a[], int n, int k){
                        boolean flag;
                        int i;
                        for (i=1; i<n; i=i+1){
                            if (a[i] != a[i-1]+k){
                                flag = false;
                                return flag;
                            }
                        }
                        return flag;
                }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',ArrayPointerType(IntType())),VarDecl('n',IntType()),VarDecl('k',IntType())],BoolType(),Block([VarDecl('flag',BoolType()),VarDecl('i',IntType()),For(BinaryOp('=',Id('i'),IntLiteral(1)),BinaryOp('<',Id('i'),Id('n')),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([If(BinaryOp('!=',ArrayCell(Id('a'),Id('i')),BinaryOp('+',ArrayCell(Id('a'),BinaryOp('-',Id('i'),IntLiteral(1))),Id('k'))),Block([BinaryOp('=',Id('flag'),BooleanLiteral(False)),Return(Id('flag'))]))])),Return(Id('flag'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))  

    def test_bulk18(self):
        input = """ int foo(int x) {
                        int f1, f2;
                        if (x<=2)
                            return 1;
                        else
                            return foo(x-2) + foo(x-1);
                }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('x',IntType())],IntType(),Block([VarDecl('f1',IntType()),VarDecl('f2',IntType()),If(BinaryOp('<=',Id('x'),IntLiteral(2)),Return(IntLiteral(1)),Return(BinaryOp('+',CallExpr(Id('foo'),[BinaryOp('-',Id('x'),IntLiteral(2))]),CallExpr(Id('foo'),[BinaryOp('-',Id('x'),IntLiteral(1))]))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))  

    def test_bulk19(self):
        input = """ boolean foo(int i){
                        int k;
                        boolean flag;
                        flag = true;
                        for (k=2; k<i/2; k=k+1){
                            if (foo2(k, i-2*k+1,k) == foo2(k,i-2/k+1,k))
                                flag = false;
                            return flag;
                        }
                        return flag;
                }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('i',IntType())],BoolType(),Block([VarDecl('k',IntType()),VarDecl('flag',BoolType()),BinaryOp('=',Id('flag'),BooleanLiteral(True)),For(BinaryOp('=',Id('k'),IntLiteral(2)),BinaryOp('<',Id('k'),BinaryOp('/',Id('i'),IntLiteral(2))),BinaryOp('=',Id('k'),BinaryOp('+',Id('k'),IntLiteral(1))),Block([If(BinaryOp('==',CallExpr(Id('foo2'),[Id('k'),BinaryOp('+',BinaryOp('-',Id('i'),BinaryOp('*',IntLiteral(2),Id('k'))),IntLiteral(1)),Id('k')]),CallExpr(Id('foo2'),[Id('k'),BinaryOp('+',BinaryOp('-',Id('i'),BinaryOp('/',IntLiteral(2),Id('k'))),IntLiteral(1)),Id('k')])),BinaryOp('=',Id('flag'),BooleanLiteral('false'))),Return(Id('flag'))])),Return(Id('flag'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))  

    def test_bulk20(self):
        input = """ float foo(float a, float b, float c){
                        if ((a+b)>c && (b+c)>a && (a+c)>b){
                            p = (a+b+c)/2;
                            s = sqrt(p*(p-a)*(p-b)*(p-c));
                            return p;
                        } 
                        else return 0; //abc thang hang
                }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',FloatType()),VarDecl('b',FloatType()),VarDecl('c',FloatType())],FloatType(),Block([If(BinaryOp('&&',BinaryOp('&&',BinaryOp('>',BinaryOp('+',Id('a'),Id('b')),Id('c')),BinaryOp('>',BinaryOp('+',Id('b'),Id('c')),Id('a'))),BinaryOp('>',BinaryOp('+',Id('a'),Id('c')),Id('b'))),Block([BinaryOp('=',Id('p'),BinaryOp('/',BinaryOp('+',BinaryOp('+',Id('a'),Id('b')),Id('c')),IntLiteral(2))),BinaryOp('=',Id('s'),CallExpr(Id('sqrt'),[BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('p'),BinaryOp('-',Id('p'),Id('a'))),BinaryOp('-',Id('p'),Id('b'))),BinaryOp('-',Id('p'),Id('c')))])),Return(Id('p'))]),Return(IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))  

    def test_bulk21(self):
        input = """ string foo(){
                        float a, b, c;
                        do
                            print("enter a, b, c: ");
                        while 1;
                        d = sqrt(b)-4*a*c;
                        if (d<0) 
                            return "vo nghiem";
                        else if (d==0)
                            return "co mot nghiem";
                        else if (d>0)
                            return "co hai nghiem";
                        else
                            return "just testing";
                }"""
        expect = str(Program([FuncDecl(Id('foo'),[],StringType(),Block([VarDecl('a',FloatType()),VarDecl('b',FloatType()),VarDecl('c',FloatType()),Dowhile([CallExpr(Id('print'),[StringLiteral("enter a, b, c: ")])],IntLiteral(1)),BinaryOp('=',Id('d'),BinaryOp('-',CallExpr(Id('sqrt'),[Id('b')]),BinaryOp('*',BinaryOp('*',IntLiteral(4),Id('a')),Id('c')))),If(BinaryOp('<',Id('d'),IntLiteral(0)),Return(StringLiteral("vo nghiem")),If(BinaryOp('==',Id('d'),IntLiteral(0)),Return(StringLiteral("co mot nghiem")),If(BinaryOp('>',Id('d'),IntLiteral(0)),Return(StringLiteral("co hai nghiem")),Return(StringLiteral("just testing")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))  

    def test_bulk22(self):
        input = """ int main(){
                        do{ }
                        while a==4 && b==6-8-9-5;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Block([])],BinaryOp('&&',BinaryOp('==',Id('a'),IntLiteral(4)),BinaryOp('==',Id('b'),BinaryOp('-',BinaryOp('-',BinaryOp('-',IntLiteral(6),IntLiteral(8)),IntLiteral(9)),IntLiteral(5)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))  

    def test_bulk23(self):
        input = """ int main(){
                        a[1] = 1;
                        a[2] = 2+a[1][1]+c+a;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1)),BinaryOp('=',ArrayCell(Id('a'),IntLiteral(2)),BinaryOp('+',BinaryOp('+',BinaryOp('+',IntLiteral(2),ArrayCell(ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(1))),Id('c')),Id('a')))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))  

    def test_bulk24(self):
        input = """ int[] foo(int a[], int b){
                        int c[3];
                        return c;
                }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',ArrayPointerType(IntType())),VarDecl('b',IntType())],ArrayPointerType(IntType()),Block([VarDecl('c',ArrayType(3,IntType())),Return(Id('c'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))  

    def test_bulk25(self):
        input = """void main( ){ 
                    if (a) 
                        if (b) 
                            if (c) a; 
                            else a; 
                     }
                """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([If(Id('a'),If(Id('b'),If(Id('c'),Id('a'),Id('a'))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))  
        
    def test_bulk26(self):
        input = """ string[] foo(){
                        int c[3];
                        return c;
                }"""
        expect = str(Program([FuncDecl(Id('foo'),[],ArrayPointerType(StringType()),Block([VarDecl('c',ArrayType(3,IntType())),Return(Id('c'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))  

    def test_bulk27(self):
        input = """string[]foo(){return c[10];}"""
        expect = str(Program([FuncDecl(Id('foo'),[],ArrayPointerType(StringType()),Block([Return(ArrayCell(Id('c'),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))  

    def test_bulk28(self):
        input =  """int[] foo(int a, float b[]) {
                        int c[3]; 
                        if (a>0) 
                            foo(2)[3+x] = a[b[2]] + 3;
                        return c; 
                }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([VarDecl('c',ArrayType(3,IntType())),If(BinaryOp('>',Id('a'),IntLiteral(0)),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),BinaryOp('+',IntLiteral(3),Id('x'))),BinaryOp('+',ArrayCell(Id('a'),ArrayCell(Id('b'),IntLiteral(2))),IntLiteral(3)))),Return(Id('c'))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))  

    def test_bulk29(self):
        input = """ int i ;
                        int f ( ) {
                            return 200;
                        }
                        void main ( ) {
                            int main ;
                            main = f ( ) ;
                            putIntLn (main ) ;
                            {
                                int i ;
                                int main ;
                                int f ;
                                main = f = i = 100;
                                putIntLn ( i ) ;
                                putIntLn (main ) ;
                                putIntLn ( f ) ;
                            }
                            putIntLn (main ) ;
                        }"""
        expect = str(Program([VarDecl('i',IntType()),FuncDecl(Id('f'),[],IntType(),Block([Return(IntLiteral(200))])),FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('main',IntType()),BinaryOp('=',Id('main'),CallExpr(Id('f'),[])),CallExpr(Id('putIntLn'),[Id('main')]),Block([VarDecl('i',IntType()),VarDecl('main',IntType()),VarDecl('f',IntType()),BinaryOp('=',Id('main'),BinaryOp('=',Id('f'),BinaryOp('=',Id('i'),IntLiteral(100)))),CallExpr(Id('putIntLn'),[Id('i')]),CallExpr(Id('putIntLn'),[Id('main')]),CallExpr(Id('putIntLn'),[Id('f')])]),CallExpr(Id('putIntLn'),[Id('main')])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))  
        
    def test_bulk30(self):
        input = """ int foo(float a){
                        if (a==1)
                            if (b>3) c=5;
                            else d=1;
                        if (e<4) good();
                        else
                            if (h>5) notgood();
                            else good();
                }"""
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',FloatType())],IntType(),Block([If(BinaryOp('==',Id('a'),IntLiteral(1)),If(BinaryOp('>',Id('b'),IntLiteral(3)),BinaryOp('=',Id('c'),IntLiteral(5)),BinaryOp('=',Id('d'),IntLiteral(1)))),If(BinaryOp('<',Id('e'),IntLiteral(4)),CallExpr(Id('good'),[]),If(BinaryOp('>',Id('h'),IntLiteral(5)),CallExpr(Id('notgood'),[]),CallExpr(Id('good'),[])))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))  

    def test_bulk31(self):
        input = """ int foo(){
                        float a;
                        a = (((5 != 6) < (6 == 5)) >= (4 + 5 > 1)) <= 1;
                }"""
        expect = str(Program([FuncDecl(Id('foo'),[],IntType(),Block([VarDecl('a',FloatType()),BinaryOp('=',Id('a'),BinaryOp('<=',BinaryOp('>=',BinaryOp('<',BinaryOp('!=',IntLiteral(5),IntLiteral(6)),BinaryOp('==',IntLiteral(6),IntLiteral(5))),BinaryOp('>',BinaryOp('+',IntLiteral(4),IntLiteral(5)),IntLiteral(1))),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))  

    def test_bulk32(self):
        input = """ void main(){
                        a = -a * b / 5 + (x && y && z + a || q * -p) && 6 * 5 / -(5 % t);
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('=',Id('a'),BinaryOp('&&',BinaryOp('+',BinaryOp('/',BinaryOp('*',UnaryOp('-',Id('a')),Id('b')),IntLiteral(5)),BinaryOp('||',BinaryOp('&&',BinaryOp('&&',Id('x'),Id('y')),BinaryOp('+',Id('z'),Id('a'))),BinaryOp('*',Id('q'),UnaryOp('-',Id('p'))))),BinaryOp('/',BinaryOp('*',IntLiteral(6),IntLiteral(5)),UnaryOp('-',BinaryOp('%',IntLiteral(5),Id('t'))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))  

    def test_bulk33(self):
        input = """ void main() {
                        float a;
                        a = b/2*n/4/5%2 && 2*9/4%2;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',FloatType()),BinaryOp('=',Id('a'),BinaryOp('&&',BinaryOp('%',BinaryOp('/',BinaryOp('/',BinaryOp('*',BinaryOp('/',Id('b'),IntLiteral(2)),Id('n')),IntLiteral(4)),IntLiteral(5)),IntLiteral(2)),BinaryOp('%',BinaryOp('/',BinaryOp('*',IntLiteral(2),IntLiteral(9)),IntLiteral(4)),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))  

    def test_bulk34(self):
        input = """ int main(){
                        foo(2)[3+x] = a[b[f+y[2]-h[t[5+j]] * 4]] + 3;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),BinaryOp('+',IntLiteral(3),Id('x'))),BinaryOp('+',ArrayCell(Id('a'),ArrayCell(Id('b'),BinaryOp('-',BinaryOp('+',Id('f'),ArrayCell(Id('y'),IntLiteral(2))),BinaryOp('*',ArrayCell(Id('h'),ArrayCell(Id('t'),BinaryOp('+',IntLiteral(5),Id('j')))),IntLiteral(4))))),IntLiteral(3)))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))  

    def test_bulk35(self):
        input = """ int main(){
                        b[1] = 1;
                        foo(a+1)[2] = 1+a[1]+c+("abc"<0);
                        foo(1)[m+1] = 3;
                        foo(1+a[1]+(1<0))[10] = 4;
                }"""
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',ArrayCell(Id('b'),IntLiteral(1)),IntLiteral(1)),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[BinaryOp('+',Id('a'),IntLiteral(1))]),IntLiteral(2)),BinaryOp('+',BinaryOp('+',BinaryOp('+',IntLiteral(1),ArrayCell(Id('a'),IntLiteral(1))),Id('c')),BinaryOp('<',StringLiteral('abc'),IntLiteral(0)))),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[IntLiteral(1)]),BinaryOp('+',Id('m'),IntLiteral(1))),IntLiteral(3)),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[BinaryOp('+',BinaryOp('+',IntLiteral(1),ArrayCell(Id('a'),IntLiteral(1))),BinaryOp('<',IntLiteral(1),IntLiteral(0)))]),IntLiteral(10)),IntLiteral(4))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))  

    def test_bulk36(self):
        input = """ float foo(){
                        int a[3];
                        string b;
                        float e;
                        boolean f;
                        do 
                            for (i=4; i<9+9; i=i+1)
                                if (a==3 && b==true)
                                    e = e + 5;
                                else continue;
                        while a==4 && c ==4 ;

                }"""
        expect = str(Program([FuncDecl(Id('foo'),[],FloatType(),Block([VarDecl('a',ArrayType(3,IntType())),VarDecl('b',StringType()),VarDecl('e',FloatType()),VarDecl('f',BoolType()),Dowhile([For(BinaryOp('=',Id('i'),IntLiteral(4)),BinaryOp('<',Id('i'),BinaryOp('+',IntLiteral(9),IntLiteral(9))),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),If(BinaryOp('&&',BinaryOp('==',Id('a'),IntLiteral(3)),BinaryOp('==',Id('b'),BooleanLiteral(True))),BinaryOp('=',Id('e'),BinaryOp('+',Id('e'),IntLiteral(5))),Continue()))],BinaryOp('&&',BinaryOp('==',Id('a'),IntLiteral(4)),BinaryOp('==',Id('c'),IntLiteral(4))))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))  

    def test_bulk37(self):
        input = """ void main () {
                        int x,y,z;
                        printf("Trau dung\\tTrau nam\\tTrau gia\\n");
                        for(x=1;x<=100;x=x+1) {
                            for(y=1;y<=100;y=y+1) {
                                for(z=1;z<=100;z=z+1) {
                                    if ((x+y+z==100) && (5*x+3*y+z/3==100) && (z%3==0)) {
                                        printf("%d\\t\\t%d\\t\\t%d\\n",x,y,z);
                                    }
                                }
                            }
                        }
                    }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('x',IntType()),VarDecl('y',IntType()),VarDecl('z',IntType()),CallExpr(Id('printf'),[StringLiteral('Trau dung\\tTrau nam\\tTrau gia\\n')]),For(BinaryOp('=',Id('x'),IntLiteral(1)),BinaryOp('<=',Id('x'),IntLiteral(100)),BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(1))),Block([For(BinaryOp('=',Id('y'),IntLiteral(1)),BinaryOp('<=',Id('y'),IntLiteral(100)),BinaryOp('=',Id('y'),BinaryOp('+',Id('y'),IntLiteral(1))),Block([For(BinaryOp('=',Id('z'),IntLiteral(1)),BinaryOp('<=',Id('z'),IntLiteral(100)),BinaryOp('=',Id('z'),BinaryOp('+',Id('z'),IntLiteral(1))),Block([If(BinaryOp('&&',BinaryOp('&&',BinaryOp('==',BinaryOp('+',BinaryOp('+',Id('x'),Id('y')),Id('z')),IntLiteral(100)),BinaryOp('==',BinaryOp('+',BinaryOp('+',BinaryOp('*',IntLiteral(5),Id('x')),BinaryOp('*',IntLiteral(3),Id('y'))),BinaryOp('/',Id('z'),IntLiteral(3))),IntLiteral(100))),BinaryOp('==',BinaryOp('%',Id('z'),IntLiteral(3)),IntLiteral(0))),Block([CallExpr(Id('printf'),[StringLiteral("%d\\t\\t%d\\t\\t%d\\n"),Id('x'),Id('y'),Id('z')])]))]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))  
        
    def test_bulk38(self):
        input = """ void main (){
                        int a,b,r;
                        scanf ("%d", a);
                        scanf ("%d", b);

                        r = a % b;
                        do 
                            a = b;
                            b = r;
                        while (r>0) ;
                        printf ("UCLN cua a va b la %d",b);
                        getch();
                    }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('r',IntType()),CallExpr(Id('scanf'),[StringLiteral('%d'),Id('a')]),CallExpr(Id('scanf'),[StringLiteral('%d'),Id('b')]),BinaryOp('=',Id('r'),BinaryOp('%',Id('a'),Id('b'))),Dowhile([BinaryOp('=',Id('a'),Id('b')),BinaryOp('=',Id('b'),Id('r'))],BinaryOp('>',Id('r'),IntLiteral(0))),CallExpr(Id('printf'),[StringLiteral('UCLN cua a va b la %d'),Id('b')]),CallExpr(Id('getch'),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))  

    def test_bulk39(self):
        input = """ 
                    void main () {
                        float dntt, price, price_tax;

                        printf("Vui long nhap so dien nang tieu thu: ");
                        scanf("%d", dntt);

                        if (dntt>=0) {
                            if (dntt<=50)       price = b1*dntt;
                            else if (dntt<=100) price = b1*50+b2*(dntt-50);
                            else if (dntt<=200) price = b1*50+b2*50+b3*(dntt-100);
                            else                price = b1*50+b2*50+b3*100+b4*100+b5*100+b6*(dntt-400);
                        price_tax = price*1.1;
                        printf("Tong tien dien la %.0f \\n", price_tax);
                        }
                        else    printf("Loi: dien nang tieu thu la mot so khong am\\n");
                    }
                    """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('dntt',FloatType()),VarDecl('price',FloatType()),VarDecl('price_tax',FloatType()),CallExpr(Id('printf'),[StringLiteral('Vui long nhap so dien nang tieu thu: ')]),CallExpr(Id('scanf'),[StringLiteral('%d'),Id('dntt')]),If(BinaryOp('>=',Id('dntt'),IntLiteral(0)),Block([If(BinaryOp('<=',Id('dntt'),IntLiteral(50)),BinaryOp('=',Id('price'),BinaryOp('*',Id('b1'),Id('dntt'))),If(BinaryOp('<=',Id('dntt'),IntLiteral(100)),BinaryOp('=',Id('price'),BinaryOp('+',BinaryOp('*',Id('b1'),IntLiteral(50)),BinaryOp('*',Id('b2'),BinaryOp('-',Id('dntt'),IntLiteral(50))))),If(BinaryOp('<=',Id('dntt'),IntLiteral(200)),BinaryOp('=',Id('price'),BinaryOp('+',BinaryOp('+',BinaryOp('*',Id('b1'),IntLiteral(50)),BinaryOp('*',Id('b2'),IntLiteral(50))),BinaryOp('*',Id('b3'),BinaryOp('-',Id('dntt'),IntLiteral(100))))),BinaryOp('=',Id('price'),BinaryOp('+',BinaryOp('+',BinaryOp('+',BinaryOp('+',BinaryOp('+',BinaryOp('*',Id('b1'),IntLiteral(50)),BinaryOp('*',Id('b2'),IntLiteral(50))),BinaryOp('*',Id('b3'),IntLiteral(100))),BinaryOp('*',Id('b4'),IntLiteral(100))),BinaryOp('*',Id('b5'),IntLiteral(100))),BinaryOp('*',Id('b6'),BinaryOp('-',Id('dntt'),IntLiteral(400)))))))),BinaryOp('=',Id('price_tax'),BinaryOp('*',Id('price'),FloatLiteral(1.1))),CallExpr(Id('printf'),[StringLiteral('Tong tien dien la %.0f \\n'),Id('price_tax')])]),CallExpr(Id('printf'),[StringLiteral('Loi: dien nang tieu thu la mot so khong am\\n')]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))  

    def test_bulk40(self):
        input = """ 
                    void main () {
                        int N, factorial;
                        factorial = 1;
                        int i;

                        printf ("Please enter N:");
                        scanf ("%d", N);

                        for (i = 1; i <= N; i=i+1)
                            factorial = factorial * i;

                        printf ("Giai thua cua %d la: %d", N, factorial);
                    }"""
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('N',IntType()),VarDecl('factorial',IntType()),BinaryOp('=',Id('factorial'),IntLiteral(1)),VarDecl('i',IntType()),CallExpr(Id('printf'),[StringLiteral('Please enter N:')]),CallExpr(Id('scanf'),[StringLiteral('%d'),Id('N')]),For(BinaryOp('=',Id('i'),IntLiteral(1)),BinaryOp('<=',Id('i'),Id('N')),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),BinaryOp('=',Id('factorial'),BinaryOp('*',Id('factorial'),Id('i')))),CallExpr(Id('printf'),[StringLiteral('Giai thua cua %d la: %d'),Id('N'),Id('factorial')])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))  

    def test_bulk41(self):
        input = """ 
                    void main () {
                        int max_len;
                        max_len = 50;
                        string str[50], ch;
                        int i;
                        i = 0;
                        printf("Enter a string, %d chars max: ", max_len);
                        do 
                            ch = getchar();
                            str[i] = ch;
                            i = i + 1;
                        while(ch!="\\n"); 
                        str[i] = "NULL";
                        printf("Line: %s", str);
                    }
                    """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('max_len',IntType()),BinaryOp('=',Id('max_len'),IntLiteral(50)),VarDecl('str',ArrayType(50,StringType())),VarDecl('ch',StringType()),VarDecl('i',IntType()),BinaryOp('=',Id('i'),IntLiteral(0)),CallExpr(Id('printf'),[StringLiteral('Enter a string, %d chars max: '),Id('max_len')]),Dowhile([BinaryOp('=',Id('ch'),CallExpr(Id('getchar'),[])),BinaryOp('=',ArrayCell(Id('str'),Id('i')),Id('ch')),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)))],BinaryOp('!=',Id('ch'),StringLiteral('\\n'))),BinaryOp('=',ArrayCell(Id('str'),Id('i')),StringLiteral('NULL')),CallExpr(Id('printf'),[StringLiteral('Line: %s'),Id('str')])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))  

    def test_all(self):
        input = """ int a, b[10];
                    string c[2], d;
                    int foo1(int a, int b[]){
                        int d;
                        do 
                            a = d;
                            {
                                int e;
                                d = d + 1;
                                if (d == e) {break;}
                            }
                            { }
                        while true;
                        return a == b <= c;
                    }
                    float[] foo2(string c){
                        a = c;
                        if (a == c >= d) continue;
                        else {break;}
                        return;
                    }
                    int main(){
                        boolean a;
                        a = foo(3)[10] = c[foo1(foo(d[30]))] = 100;
                        (a > b) + c * d - e || a && (foo(2) >= (foo1(2)[3] < 3)) <= 4 + (a != c[10]) + !a + -a % 100;
                        for (i=foo(foo1(c[3])); i<foo(a); i = i*2)
                            print("This is the value", i);
                    }"""
        expect = str(Program([  VarDecl('a',IntType()),
                                VarDecl('b',ArrayType(10,IntType())),
                                VarDecl('c',ArrayType(2,StringType())),
                                VarDecl('d',StringType()),
                                FuncDecl(   Id('foo1'),
                                            [VarDecl('a',IntType()),VarDecl('b',ArrayPointerType(IntType()))],
                                            IntType(),
                                            Block([ VarDecl('d',IntType()),
                                                    Dowhile([   BinaryOp('=',Id('a'),Id('d')),
                                                                Block([ VarDecl('e',IntType()),
                                                                        BinaryOp('=',Id('d'),BinaryOp('+',Id('d'),IntLiteral(1))),
                                                                        If(BinaryOp('==',Id('d'),Id('e')),
                                                                            Block([Break()]))]),
                                                                            Block([])],
                                                                BooleanLiteral(True)),
                                                    Return(BinaryOp('==',Id('a'),BinaryOp('<=',Id('b'),Id('c'))))])),
                                FuncDecl(   Id('foo2'),
                                            [VarDecl('c',StringType())],
                                            ArrayPointerType(FloatType()),
                                            Block([ BinaryOp('=',Id('a'),Id('c')),
                                                    If( BinaryOp('==',Id('a'),BinaryOp('>=',Id('c'),Id('d'))),
                                                        Continue(),
                                                        Block([Break()])),
                                                    Return()])),
                                FuncDecl(   Id('main'),
                                            [],
                                            IntType(),
                                            Block([ VarDecl('a',BoolType()),
                                                    BinaryOp('=',Id('a'),BinaryOp('=',ArrayCell(CallExpr(Id('foo'),[IntLiteral(3)]),IntLiteral(10)),BinaryOp('=',ArrayCell(Id('c'),CallExpr(Id('foo1'),[CallExpr(Id('foo'),[ArrayCell(Id('d'),IntLiteral(30))])])),IntLiteral(100)))),BinaryOp('||',BinaryOp('-',BinaryOp('+',BinaryOp('>',Id('a'),Id('b')),BinaryOp('*',Id('c'),Id('d'))),Id('e')),BinaryOp('&&',Id('a'),BinaryOp('<=',BinaryOp('>=',CallExpr(Id('foo'),[IntLiteral(2)]),BinaryOp('<',ArrayCell(CallExpr(Id('foo1'),[IntLiteral(2)]),IntLiteral(3)),IntLiteral(3))),BinaryOp('+',BinaryOp('+',BinaryOp('+',IntLiteral(4),BinaryOp('!=',Id('a'),ArrayCell(Id('c'),IntLiteral(10)))),UnaryOp('!',Id('a'))),BinaryOp('%',UnaryOp('-',Id('a')),IntLiteral(100)))))),
                                                    For(    BinaryOp('=',Id('i'),CallExpr(Id('foo'),[CallExpr(Id('foo1'),[ArrayCell(Id('c'),IntLiteral(3))])])),
                                                            BinaryOp('<',Id('i'),CallExpr(Id('foo'),[Id('a')])),
                                                            BinaryOp('=',Id('i'),BinaryOp('*',Id('i'),IntLiteral(2))),
                                                            CallExpr(Id('print'),[StringLiteral('This is the value'),Id('i')]))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))  
    '''