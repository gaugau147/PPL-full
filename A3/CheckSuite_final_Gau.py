import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    ########################################
    #            NO ENTRY POINT (5)
    ########################################
    
    def test_no_entry_point_simple(self):
        input = """ 
                int a;
                int foo(){return 3;}
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_no_entry_point_empty(self):
        input = """ 
                boolean a;
                boolean foo(int a){}
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_no_entry_point_no_main_1(self):
        input = """ 
                int a;
                
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_no_entry_point_no_main_2(self):
        input = """ 
                void foo(){}
                
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_no_entry_point_var_main(self):
        input = """ 
                int main;
                void foo(){}
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,405))

    ########################################
    #            REDECLARATION (7)
    ########################################

    def test_redeclared_simple(self):
        input = """ 
                int a;
                float a;
                void main(){}
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,406))
    
    def test_redeclared_var_func(self):
        input = """ 
                int a;
                void a(){}
                void main(){a();}
                """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_func_var(self):
        input = """ 
                void b(){}
                int b;
                void main(){b();}
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_func(self):
        input = """ 
                void a(int a, int b){}
                void a(){}
                void main(){a();}
                """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclared_in_param(self):
        input = """ 
                int a;
                void foo(int x, float x){}
                void main(){foo();}
                """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input,expect,410))


    def test_redeclared_in_block(self):
        input = """ 
                int a;
                void b(int a){int a; float a;}
                void main(){b();}
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redeclared_block_param(self):
        input = """ 
                int a;
                void foo(int a, int b){int a;}
                void main(){foo(1,2);}
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,412))

    ########################################
    #            UNDECLARATION (8)
    ########################################

    def test_undeclared_func_1(self):
        input = """ 
                void a(int b){foo();}
                void main(){a(10);}
                """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_undeclared_func_2(self):
        input = """ 
                void foo(int a){ }
                void main(){
                    foo1();
                }
                """
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_undeclared_func_param(self):
        input = """ 
                void foo(int a){ }
                void main(){
                    foo(b());
                }
                """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_undeclared_id_ret(self):
        input = """ 
                int foo(int a){ return b;}
                void main(){
                    foo(10);
                }
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,416))
    
    def test_undeclared_id_ret_2(self):
        input = """ 
                int foo(){ return b;}
                void main(){
                    foo();
                }
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,417))

    
    def test_undeclared_id_local_if(self):
        input = """ 
                int a;
                int foo(int a){
                    if (true){
                        int c;
                    }
                    return c;
                }
                int b;
                void main(){
                    foo(10);
                }
                """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclared_id_local_block(self):
        input = """ 
                int foo(){ 
                    {
                        int a;
                    }
                    return a;
                }
                void main(){
                    foo();
                }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undeclared_id_local_ifelse(self):
        input = """ 
                int foo(){ 
                    if (true) {
                        int a;
                    }
                    else {
                        int a;
                    }
                    return a;
                }
                void main(){
                    foo();
                }
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,420))


    ########################################
    #         TYPE MISMATCH STATEMENT (25)
    ########################################
    
    def test_mismatch_stmt_if_int(self):
        input = """ 
                void main(){
                    if(1){
                        putInt(10);
                    }
                }
                """
        expect = "Type Mismatch In Statement: If(IntLiteral(1),Block([CallExpr(Id(putInt),[IntLiteral(10)])]))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_mismatch_stmt_if_str(self):
        input = """ 
                void main(){
                    if("a string")
                        putInt(10);
                    
                }
                """
        expect = "Type Mismatch In Statement: If(StringLiteral(a string),CallExpr(Id(putInt),[IntLiteral(10)]))"
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_mismatch_stmt_if_void(self):
        input = """ 
                void foo1(){}
                boolean foo2(){return true;}
                void main(){
                    if(foo2()){
                        putInt(10);
                    } else if (foo1()){
                        putInt(10);
                    }
                }
                """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(foo1),[]),Block([CallExpr(Id(putInt),[IntLiteral(10)])]))"
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_mismatch_stmt_if_assign(self):
        input = """ 
                void main(){
                    int a;
                    a = 2;
                    if(a=1)
                        putInt(10);
                    
                }
                """
        expect = "Type Mismatch In Statement: If(BinaryOp(=,Id(a),IntLiteral(1)),CallExpr(Id(putInt),[IntLiteral(10)]))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_mismatch_stmt_if_biop(self):
        input = """ 
                void main(){
                    int a;
                    a = 1;
                    if(a+10)
                        getInt();
                    
                }
                """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),IntLiteral(10)),CallExpr(Id(getInt),[]))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_mismatch_stmt_for_exp1_bool(self):
        input = """ 
                void main(){
                    int a;
                    a = 1;
                    for (a!=1; a<10; a=a+1){
                        putIntLn(10);
                    }
                    
                }
                """
        expect = "Type Mismatch In Statement: For(BinaryOp(!=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([CallExpr(Id(putIntLn),[IntLiteral(10)])]))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_mismatch_stmt_for_exp3(self):
        input = """ 
                void main(){
                    int a;
                    for (a=1; a<10; a>=0){
                        putIntLn(10);
                    }
                    
                }
                """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(>=,Id(a),IntLiteral(0));Block([CallExpr(Id(putIntLn),[IntLiteral(10)])]))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_mismatch_stmt_for_exp2(self):
        input = """ 
                void main(){
                    int a;
                    for (a=1; a=10; a=a+1){
                        putIntLn(10);
                    }
                    
                }
                """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(=,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([CallExpr(Id(putIntLn),[IntLiteral(10)])]))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_mismatch_stmt_for_exp1_float(self):
        input = """ 
                void main(){
                    int a;
                    float b;
                    boolean c;
                    c = true;
                    a = 1;
                    for (b=1.1; c == true ; a=a+1){
                        putIntLn(10);
                    }
                    
                }
                """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(b),FloatLiteral(1.1));BinaryOp(==,Id(c),BooleanLiteral(true));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([CallExpr(Id(putIntLn),[IntLiteral(10)])]))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_mismatch_stmt_for_exp2_exp3(self):
        input = """ 
                void main(){
                    int a;
                    float b;
                    boolean c;
                    a = 1;
                    b = 1;
                    c = true;
                    for (a; c ; b){
                        putIntLn(10);
                    }
                    
                }
                """
        expect = "Type Mismatch In Statement: For(Id(a);Id(c);Id(b);Block([CallExpr(Id(putIntLn),[IntLiteral(10)])]))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_mismatch_stmt_dowhile_assign(self):
        input = """ 
                void main(){
                    int a;
                    a = 1;
                    do 
                        a=1;
                    while (a=1);
                }
                """
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(a),IntLiteral(1))],BinaryOp(=,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_mismatch_stmt_dowhile_biop(self):
        input = """ 
                void main(){
                    float a;
                    a = 1;
                    do {
                        int b;
                        b = 1;
                        putInt(b);
                    }
                    while (a+1);
                }
                """
        expect = "Type Mismatch In Statement: Dowhile([Block([VarDecl(b,IntType),BinaryOp(=,Id(b),IntLiteral(1)),CallExpr(Id(putInt),[Id(b)])])],BinaryOp(+,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_mismatch_stmt_dowhile_div(self):
        input = """ 
                void main(){
                    float a;
                    a = 10;
                    do {
                        int b;
                        b = 100;
                        putInt(b);
                    }
                    while (a/10);
                }
                """
        expect = "Type Mismatch In Statement: Dowhile([Block([VarDecl(b,IntType),BinaryOp(=,Id(b),IntLiteral(100)),CallExpr(Id(putInt),[Id(b)])])],BinaryOp(/,Id(a),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_mismatch_stmt_return_void_bool(self):
        input = """ 
                void main(){
                    int a;
                    return true;
                }
                """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_mismatch_stmt_return_void_int(self):
        input = """ 
                void main(){
                    int a;
                    a = 10;
                    return a;
                }
                """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_mismatch_stmt_return_void_func(self):
        input = """ 
                boolean foo(int a){
                    return a==1;
                }
                void main(){
                    return foo(1);
                }
                """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo),[IntLiteral(1)]))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_mismatch_stmt_return_void_biop(self):
        input = """ 
                void foo(int a){
                    return a+1;
                }
                void main(){
                    foo(1);
                }
                """
        expect = "Type Mismatch In Statement: Return(BinaryOp(+,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_mismatch_stmt_return_int_float(self):
        input = """ 
                int foo(int a){
                    return a+1.1;
                }
                void main(){
                    int a;
                    a = foo(1);
                }
                """
        expect = "Type Mismatch In Statement: Return(BinaryOp(+,Id(a),FloatLiteral(1.1)))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_mismatch_stmt_return_str_int(self):
        input = """ 
                string foo(int a){
                    return a;
                }
                void main(){
                    string a;
                    a = foo(1);
                }
                """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_mismatch_stmt_return_bool_assign(self):
        input = """ 
                boolean foo(int a){
                    return a=1;
                }
                void main(){
                    boolean a;
                    a = foo(1);
                }
                """
        expect = "Type Mismatch In Statement: Return(BinaryOp(=,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_mismatch_stmt_return_bool_func(self):
        input = """ 
                void foo(int a){
                    return;
                }
                boolean foo2(int b){
                    return foo(b);
                }
                void main(){
                    boolean a;
                    a = foo2(1);
                }
                """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo),[Id(b)]))"
        self.assertTrue(TestChecker.test(input,expect,441))
    
    def test_mismatch_stmt_return_bool_float(self):
        input = """ 
                float foo(int a, int b){
                    return a+b;
                }
                boolean foo2(int a, int b){
                    return foo(a,b);
                }
                void main(){
                    boolean a;
                    a = foo2(1,1);
                }
                """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo),[Id(a),Id(b)]))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_mismatch_stmt_return_arrcell(self):
        input = """ 
                float[] foo(int a[], int b){
                    return a[1];
                }
                void main(){
                    float a[10];
                    int b[10];
                    foo(b,1);
                }
                """
        expect = "Type Mismatch In Statement: Return(ArrayCell(Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_mismatch_stmt_return_arrpointer(self):
        input = """ 
                float foo(float a[], int b){
                    return a;
                }
                void main(){
                    float a[10];
                    int b[10];
                    a[0] = foo(b,1);
                }
                """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,444))
    
    def test_mismatch_stmt_return_arrpointer_2(self):
        input = """ 
                boolean[] foo(int a[]){
                    return a;
                }
                void main(){
                    int b[10];
                    foo(b,1);
                }
                """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,445))

    ########################################
    #         TYPE MISMATCH EXPRESSION (23)
    ########################################
    
    # ArrayCell
    def test_mismatch_expr_arrcell_idx(self):
        input = """ 
                void main(){
                    int b[10];
                    float a;
                    a = b[2.1];
                }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),FloatLiteral(2.1))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_mismatch_expr_arrcell_idx_2(self):
        input = """ 
                void foo(){}
                void main(){
                    int b[10];
                    float a;
                    a = b[foo()];
                }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_mismatch_expr_arrcell_idx_3(self):
        input = """ 
                void main(){
                    int b[10];
                    float a;
                    a = b[a];
                }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_mismatch_expr_arrcell_type(self):
        input = """ 
                void main(){
                    int c;
                    float a;
                    a = c[0];
                }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(c),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_mismatch_expr_arrcell_arr(self):
        input = """ 
                void foo(){return;}
                void main(){
                    foo();
                    float a;
                    a = foo[0];
                }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(foo),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,450))
    
    # Binary Op
    def test_mismatch_expr_biOp_coerce(self):
        input = """ 
                void main(){
                    int a, b;
                    float c;
                    b = 10;
                    c = 1.1;
                    a = b+c;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,Id(b),Id(c)))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_mismatch_expr_biOp_coerce_2(self):
        input = """ 
                void main(){
                    int a;
                    float b, c;
                    c = b = a = 5.1;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(5.1))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_mismatch_expr_biOp_coerce_3(self):
        input = """ 
                void main(){
                    int a;
                    float b, c;
                    a = b = c = 5;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(=,Id(b),BinaryOp(=,Id(c),IntLiteral(5))))"
        self.assertTrue(TestChecker.test(input,expect,453))
    
    def test_mismatch_expr_biOp_bool(self):
        input = """ 
                void main(){
                    boolean a, b;
                    a = true;
                    b = false;
                    if (a == false || b != true && a && !b){
                        putInt(10);
                    }
                    if (a >= 0){}
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(>=,Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_mismatch_expr_biOp_bool_2(self):
        input = """ 
                void main(){
                    int a, b;
                    a = 10; 
                    b = 10;
                    a = a + b/10 + a*2 + 3%a - b;
                    if (a >= 1 && a+2){
                        putInt(10);
                    }
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(&&,BinaryOp(>=,Id(a),IntLiteral(1)),BinaryOp(+,Id(a),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_mismatch_expr_biOp_coerce_4(self):
        input = """ 
                void main(){
                    float a, b;
                    a = 10.1;
                    b = 10.2;
                    a = a + b + 10/a + a*b - 100;
                    int c;
                    c = a;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(c),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_mismatch_expr_biOp_coerce_5(self):
        input = """ 
                void main(){
                    float a, b;
                    a = b = 1.1;
                    a = a + b + 10/a + a*b - 100;
                    int c;
                    c = a;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(c),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_mismatch_expr_biOp_str(self):
        input = """ 
                void main(){
                    string a, b;
                    a = "a string";
                    putString(a);
                    b = a + 1;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test_mismatch_expr_biOp_arr(self):
        input = """ 
                float[] foo(int a[]){
                    return a;
                }
                void main(){
                    int a[10];
                    a[0] = a[1] + foo(a)[3];
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(a),IntLiteral(0)),BinaryOp(+,ArrayCell(Id(a),IntLiteral(1)),ArrayCell(CallExpr(Id(foo),[Id(a)]),IntLiteral(3))))"
        self.assertTrue(TestChecker.test(input,expect,459))
    
    def test_mismatch_expr_uOp_bool(self):
        input = """ 
                void main(){
                    boolean b;
                    b = false;
                    if(-b)
                        putInt(11);
                }
                """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(b))"
        self.assertTrue(TestChecker.test(input,expect,460))
    
    def test_mismatch_expr_assign_arr_LHS(self):
        input = """ 
                void main(){
                    int a, b[10], c[10];
                    a = 10;
                    b = a;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_mismatch_expr_assign_arr_LHS_2(self):
        input = """ 
                int[] foo(int a[]){
                    return a;
                }
                void main(){
                    int a[10], b[10];
                    a = foo(b);
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),CallExpr(Id(foo),[Id(b)]))"
        self.assertTrue(TestChecker.test(input,expect,462))
    
    def test_mismatch_expr_assign_coerce(self):
        input = """ 
                float foo(float a){
                    return a;
                }
                void main(){
                    int a;
                    float b;
                    b = 1.1;
                    a = foo(b);
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),CallExpr(Id(foo),[Id(b)]))"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_mismatch_expr_callexpr_num_param(self):
        input = """ 
                int foo(int a){
                    return a;
                }
                void main(){
                    int a, b;
                    a = b = 1;
                    a = foo(a,b);
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_mismatch_expr_callexpr_num_param_2(self):
        input = """ 
                int foo(int a, int b){
                    return a;
                }
                void main(){
                    int a, b;
                    a = b = 1;
                    b = foo(a);
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_mismatch_expr_callexpr_type_param_3(self):
        input = """ 
                void foo(int a[], int b){
                    return;
                }
                void main(){
                    int a, b;
                    a = b = 1;
                    foo(a,b);
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_mismatch_expr_callexpr_type_param_4(self):
        input = """ 
                int[] goo(int a[]){
                    return a;
                }
                void foo(int a[], int b){
                    return;
                }
                void main(){
                    int a[10], b;
                    b = 1;
                    foo(goo(a),b);
                    goo(b);
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(goo),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_mismatch_expr_callexpr_type_param_5(self):
        input = """ 
                void foo(int a, float b){
                    return;
                }
                void main(){
                    float a,b;
                    a = b = 1.1;
                    foo(a,b);
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,468))

    ########################################
    #     BREAK / CONTINUE NOT IN LOOP (6)
    ########################################

    def test_break_not_inloop_main(self):
        input = """ 
                void main(){
                    int a;
                    for (a=0; a<10; a=a+1){
                        if (a==4)
                            break;
                        else
                            continue;
                    }
                    break;
                }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_break_not_inloop_if(self):
        input = """ 
                void main(){
                    int a, b;
                    b = 10;
                    for (a=0; a<10; a=a+1){
                        if (a==4){
                            if (b>5){
                                break;
                            }
                        }
                    }
                    if (a==10)
                        break;
                }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,470))
    
    def test_break_not_inloop_func(self):
        input = """ 
                int foo(int a){
                    do 
                        a = a+1;
                    while(a<10);
                    return a;
                }
                void main(){
                    int a;
                    a = foo(1);
                    break;
                }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_continue_not_inloop_main(self):
        input = """ 
                void main(){
                    int a;
                    for (a=0; a<10; a=a+1){
                        if (a==4)
                            break;
                        else
                            continue;
                    }
                    continue;
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_continue_not_inloop_if(self):
        input = """ 
                void main(){
                    int a, b;
                    b = 5;
                    for (a=0; a<10; a=a+1){
                        if (a==4){
                            if (b>5){
                                break;
                            }
                        }
                    }
                    if (a==10)
                        continue;
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_continue_not_inloop_func(self):
        input = """ 
                int foo(int a){
                    do 
                        a = a+1;
                    while(a<10);
                    return a;
                }
                void main(){
                    int a;
                    a = foo(1);
                    continue;
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,474))

    ########################################
    #         UNREACHABLE FUNCTION (3)
    ########################################

    def test_unreach_func_simple(self):
        input = """ 
                int foo(int a){
                    return a;
                }
                void main(){
                    int a;
                    return;
                }
                """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,475))
    
    def test_unreach_func_2(self):
        input = """ 
                void foo(int a){
                    return;
                }
                void goo(){
                    foo(1);
                }
                void main(){
                    int a;
                    return;
                }
                """
        expect = "Unreachable Function: goo"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_unreach_func_3(self):
        input = """ 
                void foo(int a){
                    return;
                }
                void main(){
                    boolean a;
                    a = true;
                    if(a){
                        goo(1);
                    }
                }
                void goo(int a){}
                """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,477))

    ########################################
    #         NOT LEFT VALUE (9)
    ########################################
    
    def test_not_left_value_func_use_ast(self):
        """ 
            void foo(){}
            void main(){
                foo() = 1;
            }
        """
        input = Program([FuncDecl(Id("foo"), [], VoidType(), Block([])), FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp('=', CallExpr(Id("foo"),[]), IntLiteral(1))]))])
                
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_not_left_value_func2_use_ast(self):
        """ 
            int foo(int a){return a;}
            void main(){
                foo(1) = 1;
            }
        """
        input = Program([FuncDecl(Id("foo"), [VarDecl("a", IntType())], IntType(), Block([Return(Id("a"))])), FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp('=', CallExpr(Id("foo"),[IntLiteral(1)]), IntLiteral(1))]))])
                
        expect = "Not Left Value: CallExpr(Id(foo),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_not_left_value_func3_use_ast(self):
        """ 
            int[] foo(int a[]){return a;}
            void main(){
                int a[10];
                foo(a) = 1;
            }
        """
        input = Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10, IntType())),BinaryOp("=",CallExpr(Id("foo"),[Id("a")]),IntLiteral(0)),IntLiteral(1)]))])
                
        expect = "Not Left Value: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_not_left_value_biOp_use_ast(self):
        """ 
            void main(){
                int a;
                float b;
                a = 1;
                b = 2.2;
                a + b = 1;
            }
        """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()), VarDecl("b", FloatType()), BinaryOp("=", Id("a"), IntLiteral(1)), BinaryOp("=", Id("b"), FloatLiteral(2.2)),BinaryOp("=",BinaryOp("+", Id("a"), Id("b")),IntLiteral(1))]))])
                
        expect = "Not Left Value: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_not_left_value_biOp2_use_ast(self):
        """ 
            void main(){
                int a;
                int b;
                b = 1;
                a + 1 = b;
            }
        """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()), VarDecl("b", IntType()),BinaryOp("=", Id("b"), IntLiteral(1)),BinaryOp("=",BinaryOp("+", Id("a"), IntLiteral(1)),Id("b"))]))])
                
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,48))

    def test_not_left_value_multi_biOp_use_ast(self):
        """ 
            void main(){
                int a;
                int b;
                a = b + 1 = 10;
            }
        """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()), VarDecl("b", IntType()),BinaryOp("=", Id("a"), BinaryOp("=", BinaryOp("+", Id("b"), IntLiteral(1)), IntLiteral(10)))]))])
                
        expect = "Not Left Value: BinaryOp(+,Id(b),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_not_left_value_multi_biOp2_use_ast(self):
        """ 
            void main(){
                int a;
                int b;
                a = b/1 = 10;
            }
        """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()), VarDecl("b", IntType()),BinaryOp("=", Id("a"), BinaryOp("=", BinaryOp("/", Id("b"), IntLiteral(1)), IntLiteral(10)))]))])
                
        expect = "Not Left Value: BinaryOp(/,Id(b),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_not_left_value_NaN_biOp_use_ast(self):
        """ 
            void main(){
                boolean a, b;
                b && false = true;
            }
        """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",BoolType()), VarDecl("b", BoolType()),BinaryOp("=", BinaryOp("&&", Id("b"), BooleanLiteral(False)), BooleanLiteral(True))]))])
                
        expect = "Not Left Value: BinaryOp(&&,Id(b),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_not_left_value_NaN_biOp2_use_ast(self):
        """ 
            void main(){
                boolean a, b;
                a = b && false = true;
            }
        """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",BoolType()), VarDecl("b", BoolType()),BinaryOp("=", Id("a"), BinaryOp("=", BinaryOp("&&", Id("b"), BooleanLiteral(False)), BooleanLiteral(True)))]))])
                
        expect = "Not Left Value: BinaryOp(&&,Id(b),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,486))

    ########################################
    #         FUNCTION NOT RETURN ()
    ########################################
    
    def test_func_not_return_simple(self):
        input = """ 
                int main(){
                    int a;
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_func_not_return_twopath(self):
        input = """ 
                int main(){
                    int a;
                    a = 10;
                    if (a==0){
                        putInt(10);
                    }
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_func_not_return_twopath2(self):
        input = """ 
                int main(){
                    int a;
                    a = 10;
                    if (a==0){
                        return 0;
                    }
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_func_not_return_twopath3(self):
        input = """ 
                int main(){
                    int a;
                    a = 100;
                    if (a==0){
                        return 0;
                    } else {
                        a = 0;
                    }
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_func_not_return_twopath4(self):
        input = """ 
                int main(){
                    int a;
                    a = 20;
                    if (a==0){
                        a = 0;
                    } else {
                        return 0;
                    }
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,491))
        
    def test_func_not_return_twopath5(self):
        input = """ 
                int main(){
                    int a;
                    if (a==0){
                        return 0;
                    } else {
                        return 0;
                    }
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_func_not_return_for(self):
        input = """ 
                int main(){
                    int a;
                    for(a=1; a<10; a=a+1)
                        return 0;
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_func_not_return_for_if(self):
        input = """ 
                int main(){
                    int a;
                    for(a=1; a<10; a=a+1){
                        if (a%2==0)
                            return 1;
                    }
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_func_not_return_dowhile(self):
        input = """ 
                int main(){
                    int a;
                    a = 15;
                    do
                        return 0;
                    while(a!=0);
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_func_not_return_dowhile_if(self):
        input = """ 
                int main(){
                    int a;
                    a = 15;
                    do
                        if (a==0){
                            return 0;
                        }
                        a = a-1;
                    while(a!=0);
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,496))


    def test_func_not_return_dowhile_ifelse(self):
        input = """ 
                int main(){
                    int a, b;
                    a = 1;
                    b = 2;
                    do{
                        a;
                        if (a==0)
                            return 0;
                        else
                            if (a == 1)
                                return 1;
                            else
                                return 2;
                    }
                    while (a>0);
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_func_not_return_dowhile_ifelse2(self):
        input = """ 
                int main(){
                    int a, b;
                    a = 1;
                    b = 2;
                    do{
                        a;
                        if (a==0)
                            return 0;
                        else
                            if (a == 1)
                                return 1;
                            else
                                a = 2;
                    }
                    while (a>0);
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_func_not_return_dowhile_ifelse3(self):
        input = """ 
                int main(){
                    int a, b;
                    a = 1;
                    b = 2;
                    do{
                        a;
                        if (a==0)
                            return 0;
                        else
                            if (a == 1)
                                a = 1;
                            else
                                a = 2;
                    }
                    while (a>0);
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_func_not_return_dowhile_ifelse4(self):
        input = """ 
                int main(){
                    int a, b;
                    a = 1;
                    b = 2;
                    do{
                        a;
                        if (a==0)
                            a = 0;
                        else
                            if (a == 1)
                                return 1;
                            else
                                return 2;
                    }
                    while (a>0);
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,500))
