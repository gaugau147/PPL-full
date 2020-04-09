import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    
    def test_redecl_func_diff_return_type_1(self):
        input = Program([FuncDecl(Id('main'),[],VoidType(),Block([])),FuncDecl(Id('foo'),[],FloatType(),Block([Return(FloatLiteral(4.9))])),FuncDecl(Id('foo'),[],IntType(),Block([Return(FloatLiteral(4))]))])
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redecl_para_diff_var_type(self):
        input = """int main(int a,int a){
            return 1;
        }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redecl_para_diff_var_type_2(self):
        input = """int foo(int a,string b, float a){
        }
        void main(){
            foo(1,"ab",1.9);
        }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,403))
    
    def test_redecl_vardecl_diff_vartype(self):
        input = """int a;
        float a;
        void main(){}"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redecl_vardecl_diff_vartype_2(self):
        input = """int a;
        int b;
        string a;
        void main(){}"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redecl_vardecl_same_vartype(self):
        input = """int a;
        int a;
        void main(){}"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,406))
    
    def test_redecl_vardecl_local_same_vartype(self):
        input = """int main(){
            int foo;
            int foo;
            return 1;
        }"""
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redecl_vardecl_local_diff_vartype(self):
        input = """int main(){
            int foo;
            int foo[5];
            return 0;
        }"""
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redecl_vardecl_local_diff_vartype_2(self):
        input = """int main(){
            int d;
            float b;
            string d[5];
            return 3;
        }"""
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_redecl_mix_para_and_funcbody(self):
        input = """int main(int a, int b){
            int a;
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,410))
    
    def test_redecl_mix_para_and_global(self):
        input = """int main(int a, int b){
            a =1;
            b =2;
            return a+b;
        }
        int a;"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redecl_mix_global_and_funcblock(self):
        input = """
        int a;
        int main(){
            {
                int a;
                a=0;
                return a;
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_redecl_mix_global_var_and_func(self):
        input = """
        int a;
        int a(){
        }
        void main(){}"""
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_undecl_use_expr_before_decl(self):
        input = """
        void main(){
            a;
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_undecl_use_return_id_stm_in_block_before_decl(self):
        input = """
        void main(){
            {
                a= a + a;
            }
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_undecl_use_expr_before_block_vardecl(self):
        input = """
        void main(){
            foo();
        }
        void foo(){
            var;
            int var;
        }"""
        expect = "Undeclared Identifier: var"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_undecl_use_expr_in_block_before_block_vardecl(self):
        input = """
        void foo(){
            {
                a;
            }
            int a;
        }
        void main(){
            foo();
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undecl_use_callexpr_stm(self):
        input = """
        void foo(){
            foo2();
        }
        void main(){
            foo();
        }"""
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,418))

    
    def test_undecl_use_callexpr_stm_without_decl(self):
        input = """
        void main(){
            foo1();
        }
        """
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undecl_use_callexpr_stm_with_vardecl(self):
        input = """
        int foo;
        void main(){
            foo1();
        }"""
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undecl_one_para(self):
        input = """
        int foo(int a){
            a = 2;
            return a+1;
        }
        void main(){
            foo(a);
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_undecl_many_para(self):
        input = """
        void foo(int a,int b,int c){}
        void main(){
            foo(a,b,c);
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_undecl_mix_redecl(self):
        input = """
        int var(int a){
            return 1;
        }
        void main(int a){
            a = 1111;
            var(a);
            int a;
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_redecl_with_callexpr_num_para(self):
        input = """
        int var(int a){
            a = 2;
            return a;
        }
        void main(int a){
            var(2);
            int a;
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_undecl_use_expr_stm_without_decl(self):
        input = """
        void main(){
            foo();
        }
        void foo(){
            fo;
            int x;
        }"""
        expect = "Undeclared Identifier: fo"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_mismatch_with_int(self):
        input = """
        void main(){
            int a;
            a=6.7;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(6.7))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_undecl_expr_before_global_vardecl(self):
        input = """
        void main(){
            int var;
        }
        int var;"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_undecl_use_callexpr_stm_recur(self):
        input = """
        void main(){
            foo();
        }
        void foo(){
            foo();
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_undecl_use_callexpr_stm_before_decl(self):
        input = """
        void main(){
            foo1();
        }
        int foo1(){
            return 1;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_undecl_use_callexpr_stm_in_block(self):
        input = """
        void main(){
            {
                foo1();
                return;
            }
        }

        string foo1(){
            string a;
            a = "cc";
            return a;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_undecl_use_callexpr_stm_befor_decl(self):
        input = """
        void main(){
            foo1();
        }
        float foo1(){
            return 1.9;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_undecl_use_callexpr_stm_with_recursive(self):
        input = """
        int main(){
            foo();
            return 1;
        }
        void foo(){
            foo();
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_mismatch_stm_correct_case_with_if_no_else_1(self):
        input = """
        void main(){
            if(true){
                int a;
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_mismatch_stm_correct_case_with_if_else(self):
        input = """
        void main(){
            if(false){
                int b;
            }
            else{
                int c;
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_mismatch_stm_with_if_no_else_2(self):
        input = """
        void main(){
            int a;
            int b;
            a=0;
            b=1;
            if(a+b){
                int b;
            }
        }"""
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),Id(b)),Block([VarDecl(b,IntType)]))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_mismatch_stm_with_num_and_if_else(self):
        input = """
        void main(){
            int a;
            int b;
            if(2){
                int b;
            }
            else{
                int b;
            }
        }"""
        expect = "Type Mismatch In Statement: If(IntLiteral(2),Block([VarDecl(b,IntType)]),Block([VarDecl(b,IntType)]))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_mismatch_stm_correct_case_with_return(self):
        input = """
        int main(){
            foo2();
            foo3();
            foo4();
            return 2;
        }
        void foo2(){
            return ;
        }
        string foo3(){
            return "a";
        }
        float foo4(){
            return 6.9;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,437))
    
    def test_mismatch_stm_correct_case_with_return_diff_type_arr(self):
        input = """
        int[] main(){
            float arr[5];
            return arr;
        }"""
        expect = "Type Mismatch In Statement: Return(Id(arr))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_mismatch_stm_correct_case_with_return_arrpnt(self):
        input = """
        int[] main(float b){
            b = 1.2;
            return b;
        }"""
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_func_not_rett_with_if_no_else(self):
        input = """
        int a;
        int main(){
            if (true){
                int a;
            }
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_continue_in_loop_for_correct_case(self):
        input = """
        int a;
        int main(){
            a= 2;
            for(a;a>5;5){
                continue;
            }
            return 1;           
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_continue_in_loop_dowhile_correct_case(self):
        input = """
        void main(){
            do
                continue;
            while(true);    
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_continue_not_in_loop(self):
        input = """
        void main(){
            continue;   
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_break_not_in_loop(self):
        input = """
        void main(){
            {
                {
                    break;
                }
            }  
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_unreach_func(self):
        input = """
        void main(){
            return;
        }
        int foo(int a){
            a = 0;
            return a+1;
        }"""
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_type_mismatch_expr_in_callexpr_para(self):
        input = """
        void main(){
            int a;
            a = foo(2.9);
            return; 
        
        }
        int foo(int a){
            return a+1;
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[FloatLiteral(2.9)])"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_type_mismatch_expr_in_callexpr_para_corr_case(self):
        input = """
        void main(){
            int a;
            a = foo(2.9);
            return; 
        
        }
        int foo(float a){
            return 1;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_unreach_stm_with_break_in_dowhile(self):
        input = """
        void main(){
            int a;
            a = 0;
            do break; 1; while true;
        }"""
        expect = "Unreachable Statement: IntLiteral(1)"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_unreach_stm_with_break_in_dowhile_2(self):
        input = """
        int b;
        void main(){
            int a;
            int b;
            {
                int b;
                b = 0;
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_unreach_stm_with_only_return(self):
        input = """
        void main(){
            int a;
            return;
            a=0;
        }"""
        expect = "Unreachable Statement: BinaryOp(=,Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,450))


    def test_unreach_stm_with_return_in_block_1(self):
        input = """
        void main(){
            int a;
            {
                return;
            }
            a=0;
        }"""
        expect = "Unreachable Statement: BinaryOp(=,Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_unreach_stm_with_return_in_block_2(self):
        input = """
        void main(){
            int a;
            {
                return;
            }
            {
                a=0;
            }
        }"""
        expect = "Unreachable Statement: Block([BinaryOp(=,Id(a),IntLiteral(0))])"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_unreach_stm_with_if_no_else(self):
        input = """
        void main(){
            int a;
            if (true){
                return;
            }
            a = 0;
            a = 1+2;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_unreach_stm_with_if_else(self):
        input = """
        void main(){
            int a;
            if (true){
                return;
            }
            else {
                return;
            }
            a = 0;
            a = 1+2;
        }"""
        expect = "Unreachable Statement: BinaryOp(=,Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_unreach_stm_with_for(self):
        input = """
        void main(){
            int a;
            a=0;
            for(a;true;a+1)
            {
                return;
            }
            a = 0;
            a = 1+2;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_unreach_stm_with_for_crr_case(self):
        input = """
        void main(){
            int a;
            a = 1+2;
            for(a;true;a+1)
            {
                return;
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_unreach_stm_with_return_crr_case(self):
        input = """
        void main(){
            int a;
            a = 1+2;
            return;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_unreach_stm_with_if_else_crr_case(self):
        input = """
        void main(){
            if(true){
                return;
            }
            else{
                return;
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test_unreach_stm_with_if_else_crr_case_2(self):
        input = """
        void main(){
            if(true){
                return 1;
            }
            else{
                return;
            }
        }"""
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_unreach_stm_with_do_while_crr_case(self):
        input = """
        void main(){
            int a;
            int b;
            b = 0;
            a = b +2 ;
            do return; while (true);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_index_out_of_range(self):
        input = """
        void main(){
            int a[5];
            int b;
            a[6] = 0;
        }"""
        expect = "Index Out Of Range: ArrayCell(Id(a),IntLiteral(6))"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_index_out_of_range_with_plus(self):
        input = """
        void main(){
            int a[2];
            a[5+5] = 0;
        }"""
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(+,IntLiteral(5),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_index_out_of_range_with_minus(self):
        input = """
        void main(){
            int a[4];
            a[20-5] = 0;
        }"""
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(-,IntLiteral(20),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_index_out_of_range_with_mul(self):
        input = """
        void main(){
            int a[1];
            a[5*5] = 0;
        }"""
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(*,IntLiteral(5),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_index_out_of_range_with_dev(self):
        input = """
        void main(){
            int a[5];
            a[25/5] = 0;
        }"""
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(/,IntLiteral(25),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_index_out_of_range_with_minus_and_add(self):
        input = """
        void main(){
            int a[7];
            a[0+5-2+6] = 0;
        }"""
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLiteral(0),IntLiteral(5)),IntLiteral(2)),IntLiteral(6)))"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_index_out_of_range_with_mul_minus_add(self):
        input = """
        void main(){
            int a[6];
            a[0*5-2+9] = 0;
        }"""
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(+,BinaryOp(-,BinaryOp(*,IntLiteral(0),IntLiteral(5)),IntLiteral(2)),IntLiteral(9)))"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_index_out_of_range_with_mol(self):
        input = """
        void main(){
            int a[5];
            a[29%10] = 0;
        }"""
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(%,IntLiteral(29),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_index_out_of_range_with_unary(self):
        input = """
        void main(){
            int a[5];
            a[-1] = 0;
        }"""
        expect = "Index Out Of Range: ArrayCell(Id(a),UnaryOp(-,IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_index_out_of_range_with_multi_op_1(self):
        input = """
        void main(){
            int a[5];
            a[29%10 + 4 * 2 -5] = 15;
        }"""
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(-,BinaryOp(+,BinaryOp(%,IntLiteral(29),IntLiteral(10)),BinaryOp(*,IntLiteral(4),IntLiteral(2))),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_index_out_of_range_with_multi_op_2(self):
        input = """
        int a[4];
        void main(){
            a[9*3-6*2 + 4 * 2 -5] = 15;
        }"""
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(-,BinaryOp(+,BinaryOp(-,BinaryOp(*,IntLiteral(9),IntLiteral(3)),BinaryOp(*,IntLiteral(6),IntLiteral(2))),BinaryOp(*,IntLiteral(4),IntLiteral(2))),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_getInt_func(self):
        input = """
        int main(){
            int b;
            b = getInt();
            return b;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_unreachable_function_recursive(self):
        input = """
        int main(){
            int temp;
            temp = 0;
            return temp;
        }
        int foo(){
            return foo();
        }"""
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_putInt_func(self):
        input = """
        int main(){
            int temp;
            putInt(temp);
            temp = 0;
            return temp;
        }"""
        expect = "Uninitialized Variable: temp"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_putIntLn_func(self):
        input = """
        int main(){
            int temp;
            temp = 0;
            putIntLn(temp);
            return temp;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,475))
    
    def test_getFloat_func(self):
        input = """
        int main(){
            int temp;
            temp =2;
            temp = getFloat(temp);
            return temp;
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(getFloat),[Id(temp)])"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_putFloat_func(self):
        input = """
        int main(){
            int temp;
            temp =10;
            putFloat(temp);
            return temp;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,477))
    
    def test_putFloatLn_func(self):
        input = """
        int main(){
            int temp;
            temp  = 6;
            putFloatLn(temp);
            return temp;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_putBool_func(self):
        input = """
        float main(){
            float flo;
            flo = 0.1;
            putBool(flo);
            return flo;
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(putBool),[Id(flo)])"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_putBoolLn_func(self):
        input = """
        float main(){
            string str;
            str = "asdasdasd";
            putBoolLn(str);
            return 2.0;
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(putBoolLn),[Id(str)])"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_putString_func(self):
        input = """
        float main(){
            string str;
            str = "";
            putString(str);
            return 2.0;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,481))
    
    def test_putStringLn_func(self):
        input = """
        float main(){
            string str;
            {
                str = "a";
                putStringLn(str);
            }
            return 2.0;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_putLn_func(self):
        input = """
        void main(){
            int a;
            a=0;
            putLn(a);
            return;
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(putLn),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_unreach_stm_with_continue_in_dowhile(self):
        input = """
        void main(){
            int a;
            a=0;
            do 
                a = 2;
                continue;
                a = 0;
             while (true);
        }"""
        expect = "Unreachable Statement: BinaryOp(=,Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_unreach_stm_vardecl_block(self):
        input = """
        void main(){
            int a;
            a=0;
            return;
            int b;
            b=2;
        }"""
        expect = "Unreachable Statement: BinaryOp(=,Id(b),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_cotinue_in_do_while_block(self):
        input = """
        void main(){
            do{
                continue;
                int a;
                int b;
                int c;
            } while(false);
            return;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_unreach_stm_with_for_and_vardecl(self):
        input = """
        void main(){
            int a;
            for (a =0;a<5;a=a+1){
                continue;
                int b;
                b=0;
            }
        }"""
        expect = "Unreachable Statement: BinaryOp(=,Id(b),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_unreach_stm_with_for_and_vardecl_2(self):
        input = """
        void main(){
            int a;
            for (a =0;a<5;a=a+1){
                return;
            }
            int c;
            c = 2;
            a = c-3;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_unreach_stm_and_redecl(self):
        input = """
        void main(){
            int a;
            boolean b;
            b = true;
            do{
                break;
            } while (b);
            int a;
            a = 2;
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_unreach_stm_with_block(self):
        input = """
        int main(){
            return 1;
            {
                int a;
                a = 0;
            }
        }"""
        expect = "Unreachable Statement: Block([VarDecl(a,IntType),BinaryOp(=,Id(a),IntLiteral(0))])"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_no_entry_point(self):
        input = """
        int foo(int a,int b){
            a = 2;
            b = 3;
            return a+b;
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_complicated_program_with_func_not_return(self):
        input = """
        int foo(int a,int b){
            a = 2;
            b = 3;
            return a+b;
        }
        void print(string a){}
        int main(){
                int a,b,c,d;
                a = 2;
                b = 5;
                c = 6;
                d = 9;
                do {
                    if (a==b && c>=d){
                        print("I Love PPL");
                    }
                    else print("I Hate PPL");
                } while (true);
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_complicated_program_crr_case(self):
        input = """
        int main(){   
                int n, reversedNumber, remainder;
                n = 10;reversedNumber = 11;remainder = -13;
                do
                {
                    remainder = n%10;
                    reversedNumber = reversedNumber*10 + remainder;
                    n / 10;
                } while n != 0;
                return 0;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_complicated_program_undeclare_func(self):
        input = """
        int main() {
                int exponent;
                float base, result;
                exponent = 0;
                base = 1;
                result = 2;
                if (exponent != 0) {
                    result = base;
                    --exponent;
                }
                print(result);
                return 0;
            }"""
        expect = "Undeclared Function: print"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_complicated_program_crr_case_2(self):
        input = """
        void main(){
                int a;
                a = 1;
                do{
                    int k;
                    k=2;
                    if (k==0) break;
                    else continue;
                } while(a<0);
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_complicated_program_with_undecl(self):
        input = """
        void main(){
                {
                    do{
                        main();
                    } while(x<5);
                }
            }"""
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_complicated_program_with_redecl(self):
        input = """
        void main(){
                string hello;
                {
                    int a,b,d;
                    float a[5],c;
                }

            }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_complicated_program_with_type_mismatch_in_return(self):
        input = """
        int main(){
                int a,b,c;
                a = 2;b=7;c=0;
                if (a>b)
                    do {
                        a=c;
                        return 1;
                    } while true;
                else return false;
            }"""
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_complicated_program_with_type_mismatch_in_exp(self):
        input = """
        void main(){
                int a,b;
                a =2;
                b=3;
                int temp;
                temp =2;
                if (a>b){
                    b=temp;
                    if (a==b)
                        a = true;
                }
                else a= temp;
            }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_complicated_program_with_no_entry_point(self):
        input = """
       int foo(){
                putString("I Love PPL");
                putString("I Love Dr.NHP");
                return 1;
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,500))