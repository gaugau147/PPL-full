import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_redeclared_global_variable_different_type(self):
        """test global variable declare with different type"""
        input = """
        int intVar;
        string intVar[5];
        void main(){
        }"""
        expected = "Redeclared Variable: intVar"
        self.assertTrue(TestChecker.test(input,expected,400))
    def test_redeclared_global_variable_same_type(self):
        """test global variable declare with same type"""
        input = """
        int interger;
        int interger;
        void main(){
        }"""
        expected = "Redeclared Variable: interger"
        self.assertTrue(TestChecker.test(input,expected,401))
    def test_redeclared_variable_in_function_same_type(self):
        """test redeclared variable in fuction with same type"""
        input = """
        void main(){
            int factor;
            int factor;
        }"""
        expected = "Redeclared Variable: factor"
        self.assertTrue(TestChecker.test(input,expected,402))
    def test_redeclared_variable_in_function_different_type(self):
        """test redeclared varibale in function with diffenrent type"""
        input = """
        void main(){
            int intVar;
            float intVar;
        }"""
        expected = "Redeclared Variable: intVar"
        self.assertTrue(TestChecker.test(input,expected,403))
    def test_redeclared_variable_in_if_statement(self):
        """redeclared varibale in if stmt """
        input = """
        void main(int x){
            if(true) 
            {
                int x;
                int x;
            }
        }"""
        expected = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expected,404))
    def test_redeclared_fucntion_same_type(self):
        """test redeclared function"""
        input = """
        void main(){
        }
        void main(){           
        }"""
        expected = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expected,405))
    def test_redeclared_function_diffrent_type(self):
        """redeclared function different type"""
        input = """
        void sum(){
        }
        int sum(){
            return 1;
        }
        void main(){
        }"""
        expected = "Redeclared Function: sum"
        self.assertTrue(TestChecker.test(input,expected,406))
    def test_redeclared_parameter_function_declare_same_type(self):
        """redeclare parameter"""
        input = """
        void foo(int a, int a){
        }
        void main(){
        }"""
        expected = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expected,407))

    def test_redeclared_parameter_function_declare_diff_type(self):
        """test redeclare parameter different type"""
        input = """
        void sub(int a[], int a){
        }
        void main(){
        }"""
        expected = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expected,408))

    def test_redeclared_local_variable_parameter_function_declare(self):
        """test local variable,parameter declare"""
        input = """
        void reduce(int a, int b,string c){
            int a;
        }
        void main(){
        }"""
        expected = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expected,409))
    def test_redeclared_variable_function(self):
        """redecalre variable-function"""
        input = """
        int foo;
        void foo(){}
        void main(){
        }"""
        expected = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expected,410))

    def test_redeclared_variable_function_sum(self):
        """redeclare vairable in sum"""
        input = """
        int foo;
        int sum(int a,int b){
            return a+b;
        }
        void main(){
        }
        int sum;
        """
        expected = "Redeclared Variable: sum"
        self.assertTrue(TestChecker.test(input,expected,411))
    def test_redeclared_variable_getInt_function(self):
        """redecalre variable built in function"""
        input = """
        int getInt;
        void main(){    
        }
        """
        expected = "Redeclared Variable: getInt"
        self.assertTrue(TestChecker.test(input,expected,412))

    def test_redeclared_build_in_function_getInt_function(self):
        """redeclare function built in"""
        input = """
        void getInt(){}
        void main(){    
        }
        """
        expected = "Redeclared Function: getInt"
        self.assertTrue(TestChecker.test(input,expected,413))
    def test_redeclare_in_scope(self):
        """redeclare in local scope"""
        input = """
        void main(){
            int a;
            {
               int a;
               int a;
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_redeclare_in_function_scope_declare_after(self):
        """reclare variable"""
        input = """
        void main(){
            int key;
            {
               int key;
            }
            int key;
        }
        """
        expect = "Redeclared Variable: key"
        self.assertTrue(TestChecker.test(input,expect,415))
    def test_undeclared_function(self):
        """undeclared functin in function main"""
        input = """void main()
        {
            foo();
        }"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,416))
    def test_undeclared_function_in_return(self):
        """undeclared function in return stmt"""
        input = """int main()
        {
            return foo();
        }"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,417))
    def test_undeclared_variable(self):
        """undeclared variable in main function"""
        input = """
        void main(){
            xfactor;
        }
        """
        expect = """Undeclared Identifier: xfactor"""
        self.assertTrue(TestChecker.test(input,expect,418))
    def test_undeclared_variable_in_binary_expr(self):
        """undeclare variable"""
        input = """
        float a;
        void main(){
            a*b;
        }
        """
        expect = """Undeclared Identifier: b"""
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undeclared_variable_in_binary_unary_expr(self):
        """undeclare var"""
        input = """
        float floatVariable;
        void main(){
            !variable;
        }
        """
        expect = """Undeclared Identifier: variable"""
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undeclared_variable_is_a_array_cell(self):
        input = """
        void main(){
            a[1];
        }
        """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_undeclared_variable_in_call_expr(self):
        input = """
        void foo(int intVar){}
        void main(){
            foo(intVar);
        }
        """
        expect = """Undeclared Identifier: intVar"""
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_undeclared_variable_in_return_statement(self):
        """undeclare var in return stmt"""
        input = """
        int main(){
            int b;
            return a+b;
        }
        """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_undeclare_in_scope_(self):
        """undeclare var"""
        input = """
        void main(){
            int poo;
            {
                poo;
                boo;
            }
        }
        """
        expect = "Undeclared Identifier: boo"
        self.assertTrue(TestChecker.test(input,expect,424))
    def test_undeclare_in_scope_vardec_after(self):
        """More complex program"""
        input = """
        void main(){
            int a;
            {
                a;
                b;
            }
            int b;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,425))
    def test_undeclare_scope_with_array_type(self):
        """undeclare array var"""
        input = """
        void main(){
            int arra[5];
            {
                array[1];
            }
            float a[5];
        }
        """
        expect = "Undeclared Identifier: array"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_function_not_return(self):
        """function int main() not return"""
        input = """
        int main(){
          
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_function_not_return_if_stmt(self):
        """function not return with if stmt else not return"""
        input = """
        int main(){
            int x;
            if(x==1){
                return 1;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_function_not_return_if_stmt_return(self):
        """function float main not return"""
        input = """
        float main(){
            int inVar;
            if(inVar==1){
                return 1.0;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_function_not_return_if_stmt_return_else(self):
        """function string main not return in else stmt"""
        input = """
        string main(){
            int x;
            if(x==1){
                return "a";
            }
            else{

            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,430))
    def test_function_not_return_complex_if(self):
        """function not return with complex if"""
        input = """
        int main(){
            int integerVar;
            integerVar=1;
            if(integerVar==1){
                if(true){
                    return 1;
                }
                else{
                    return 1;
                }
                return 1;
            }
            else{
                if(true){
                    return 1;
                }
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_function_not_return_more_complex_if(self):
        """function not return with more complex if"""
        input = """
        int main(){
            int a;
            boolean b;
            b=true;
            if(b){
                return 1;
            }
            if(b){
                return 1;
            }
            if(!b){
                return 1;
            }
            else{
                if(b&&true){
                    return 1;
                }
                else{
                    if(b){
                        return 1;
                    }
                }
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_function_not_return_more_more_complex_if(self):
        """function not return with more more complex if"""
        input = """
        boolean main(){
            boolean a;
            a=true;
            boolean b;
            b=false;
            do if(a&&b){
                if(a){
                    return b;
                }
                if(b){
                    return a;
                }
                if(a||b){
                    return a||b;
                }
                return a;
            }
            while true;
            if(a==false){
                return true;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,433))
    def test_break_not_in_loop_for(self):
        """break not in for"""
        input = """
        void main(){
            int x;
            for(x=1;x<5;x=x+1){
            }
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,434))
    def test_break_not_in_loop_for_nested(self):
        """break not in for nested"""
        input = """
        void main(){
            int x;
            for(x=1;x<1;x=x+1){
                for(x=1;x<1;x=x+1){

                }
            }
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,435))
    def test_break_not_in_loop_do_while(self):
        """break not in do while stmt"""
        input = """
        void main(){
            int x;
            do x=1; while x==1;
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,436))
    def test_break_not_in_loop_do_while_nested(self):
        """break not in do while stmt nested"""
        input = """
        void main(){
            int x;
            do {do x=1; while x==1;} while x==1;
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,437))
    def test_continue_not_in_loop_for(self):
        """continue not in for loop"""
        input = """
        void main(){
            int x;
            for(x=1;x<5;x=x+1){
            }
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,438))
    def test_continue_not_in_loop_for_nested(self):
        """continue not in for loop nested"""
        input = """
        void main(){
            int x;
            for(x=1;x<1;x=x+1){
                for(x=1;x<1;x=x+1){

                }
            }
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,439))
    def test_continue_not_in_loop_do_while(self):
        """continue not in do while stmt"""
        input = """
        void main(){
            int x;
            do x=1; while x==1;
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_continue_not_in_loop_do_while_nested(self):
        """continue not in do while loop nested"""
        input = """
        void main(){
            int x;
            do {do x=1; while x==1;} while x==1;
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,441))
    def test_unreachable_function(self):
        """function foo must be invoke by another function"""
        input = """
        void foo(){
        }
        void main(){

        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,442))
    def test_unreachable_function_declare_after(self):
        """function foo must be invoke by another function"""
        input = """
        void main(){
        }
        void foo(){
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,443))
    def test_not_left_value_float_type(self):
        """left value must accessible storage"""
        input = """
        
        void main(){
            1.5=1.5;
        }  
        """
        expect = "Not Left Value: FloatLiteral(1.5)"
        self.assertTrue(TestChecker.test(input,expect,444))
    def test_not_left_value_string_type(self):
        """left value==string"""
        input = """
        void main(){
            string abc;
            "abc"=abc;
        }
        
        """
        expect = "Not Left Value: StringLiteral(abc)"
        self.assertTrue(TestChecker.test(input,expect,445))
    def test_not_left_value_int_type(self):
        """left value=>int"""
        input = """
        void main(){
            int intvar;
            123=intvar;
        }
        
        """
        expect = "Not Left Value: IntLiteral(123)"
        self.assertTrue(TestChecker.test(input,expect,446))
    def test_not_left_boolean_type(self):
        """left value boolean"""
        input = """
        void foo(){
        }
        void main(){
            boolean a;
            true=a;
        }
        
        """
        expect = "Not Left Value: BooleanLiteral(true)"
        self.assertTrue(TestChecker.test(input,expect,447))
    def test_not_left_value_complex(self):
        """complex left value"""
        input = """
        void foo(){
        }
        void main(){
            int xyz;
            1+1=xyz;
        }
        
        """
        expect = "Not Left Value: BinaryOp(+,IntLiteral(1),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,448))
    def test_left_varlue_with_expresion(self):
        """expresion in left value"""
        input = """
        void main(){
            int a;
            int b;
            a=5;
            if(a==5)
                a+b=10;
            return;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,449))
    def test_left_varlue_with_expresion_complex(self):
        """left value complex"""
        input = """
        void main(){
            true&&true||false=true;
        }
        """
        expect = "Not Left Value: BinaryOp(||,BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(true)),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,450))
    def test_type_mismatch_in_if_statement(self):
        """if statement expr must booltype"""
        input = """
        void main(){
            int interger;
            if(interger){
                return;
            }
        }
        
        """
        expect = "Type Mismatch In Statement: If(Id(interger),Block([Return()]))"
        self.assertTrue(TestChecker.test(input,expect,451))
    def test_type_mismatch_in_for_statement_expr2(self):
        """for statemet expr2 must booltype"""
        input = """
        void main(){
            int exp1;
            int exp2;
            int exp3;
            for(exp1;exp2;exp3){
            }
        }    
        """
        expect = "Type Mismatch In Statement: For(Id(exp1);Id(exp2);Id(exp3);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,452))
    def test_type_mismatch_in_for_statement_expr1(self):
        """for statement exp1 must inttype"""
        input = """
        void main(){
            boolean exp1;
            int exp2;
            int exp3;
            for(exp1;exp2;exp3){
            }
        }    
        """
        expect = "Type Mismatch In Statement: For(Id(exp1);Id(exp2);Id(exp3);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,453))
    def test_type_mismatch_in_for_statement_expr3(self):
        """for statement exp3 must inttype"""
        input = """
        void main(){
            int exp1;
            int exp2;
            string exp3;
            for(exp1;exp2;exp3){
            }
        }    
        """
        expect = "Type Mismatch In Statement: For(Id(exp1);Id(exp2);Id(exp3);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_type_mismatch_in_statement_in_return(self):
        """type of return must be equal to or be coerced to the return type of the function"""
        input = """
        void main(){
            return 1;
        }    
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,455))
    def test_type_mismatch_in_statement_in_return_1(self):
        """type of return must be equal to or be coerced to the return type of the function"""
        input = """
        int foo(){
            return;
        }
        void main(){
        }    
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,456))
    def test_type_mismatch_in_statement_in_return_2(self):
        """type of return must be equal to or be coerced to the return type of the function"""
        input = """
        int foo(){
            return 1.0;
        }
        void main(){
            foo();
        }    
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,457))
    def test_type_mismatch_in_statement_in_return_3(self):
        """type of return must be equal to or be coerced to the return type of the function"""
        input = """
        int main(){
            int main;
            {
                main = 1;
            }
            main=2;
            float a[5];
            return a[5];
        }
        """
        expect = "Type Mismatch In Statement: Return(ArrayCell(Id(a),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input,expect,458))
    def test_type_mismatch_in_statement_in_return_4(self):
        """type of return must be equal to or be coerced to the return type of the function"""
        input = """
        int[] main(){
            float b[5];
            return b;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,459))
    def test_mismatch_in_array(self):
        """array e1[e2] e1 must be in array type or array pointer type"""
        input = """
        void main(){
            int a[5];
            int b;
            b[5];
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,460))
    def test_mismatch_in_array_e2(self):
        """array e1[e2] e2 must be interger"""
        input = """
        void main(){
            int a[5];
            a[5.0];
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(5.0))"
        self.assertTrue(TestChecker.test(input,expect,461))
    def test_mismatch_in_array_unary(self):
        """!expr expr must boolean type"""
        input = """
        void main(){
            int a[5];
            a[5]=5;
            !a[5];
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,ArrayCell(Id(a),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input,expect,462))
    def test_mismatch_in_array_unary_diff_in_if_stm(self):
        """!expr expr must boolean type"""
        input = """
        void main(){
            int avariableInt;
            int array[10];
            array[1]=5;
            if(array[1]<5) return;
            else {
                !array[1];
            }
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,ArrayCell(Id(array),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,463))
    def test_mismatch_in_array_unary_nagative(self):
        """-expr expr must be integer or float"""
        input = """
        void main(){
            string a;
            -a;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,464))
    def test_mismatch_in_array_binary_expression_add(self):
        """expr1+expr2 expr1,expr2 must be integer or float"""
        input = """
        void main(){
            int a;
            boolean b;
            int c;
            c=a+b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,465))
    def test_mismatch_in_array_binary_expression_sub(self):
        """expr1-expr2 expr1,expr2 must be integer or float"""
        input = """
        void main(){
            int a[5];
            boolean b[5];
            float c;
            c=a[5]-b[5];
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(-,ArrayCell(Id(a),IntLiteral(5)),ArrayCell(Id(b),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input,expect,466))
    def test_mismatch_in_array_binary_expression_mul(self):
        """expr1*expr2 expr1,expr2 must be integer or float"""
        input = """
        void main(){
            int intArr[10];
            boolean booleanArr[6];
            float f;
            f=intArr[5]*booleanArr[5];
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,ArrayCell(Id(intArr),IntLiteral(5)),ArrayCell(Id(booleanArr),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input,expect,467))
    def test_mismatch_in_array_binary_expression_div(self):
        """expr1/expr2 expr1,expr2 must be integer or float"""
        input = """
        void main(){
            int a[5];
            boolean b[5];
            float c;
            c=a[5]-b[5];
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(-,ArrayCell(Id(a),IntLiteral(5)),ArrayCell(Id(b),IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_mismatch_in_array_binary_expression_mod(self):
        """expr1%expr2 expr1,expr2 must be integer"""
        input = """
        void main(){
            int intvar;
            float floatvar;
            intvar%floatvar;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(intvar),Id(floatvar))"
        self.assertTrue(TestChecker.test(input,expect,469))
    def test_mismatch_in_array_binary_expression_less_than(self):
        """expr1<expr2 expr1,expr2 must be integer or float"""
        input = """
        void main(){
            float x;
            string y;
            boolean z;
            z=x<y;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<,Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input,expect,470))
    def test_mismatch_in_array_binary_expression_less_equal(self):
        """expr1<=expr2 expr1,expr2 must be integer or float"""
        input = """
        void main(){
            float abc;
            boolean xyz;
            boolean z;
            z=abc<=xyz;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<=,Id(abc),Id(xyz))"
        self.assertTrue(TestChecker.test(input,expect,471))
    def test_mismatch_in_array_binary_expression_great_than(self):
        """expr1>expr2 expr1,expr2 must be integer or float"""
        input = """
        void main(){
            float floatVars1;
            float floatVars2;
            floatVars1=1;
            floatVars2=2;
            string stringVars;
            floatVars1>floatVars2;
            stringVars>floatVars1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(stringVars),Id(floatVars1))"
        self.assertTrue(TestChecker.test(input,expect,472))
    def test_mismatch_in_array_binary_expression_great_equal(self):
        """expr1>=expr2 expr1,expr2 must be integer or float"""
        input = """
        void main(){
            int check1;int check2;
            check1=1;check2=2;
            if(check1==check2){
                boolean x;
                x=check1>="a";
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>=,Id(check1),StringLiteral(a))"
        self.assertTrue(TestChecker.test(input,expect,473))
    def test_mismatch_in_array_binary_expression_equal(self):
        """expr1==expr2 expr1,expr2 must be integer or float and must the same type"""
        input = """
        void main(){
            float a;
            int b;
            a=5;
            b=1;
            do a=6; while (a==b);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,474))
    def test_mismatch_in_array_binary_expression_not_equal(self):
        """expr1==expr2 expr1,expr2 must be integer or float and must the same type"""
        input = """
        void main(){
            int intVar;
            float floatVar;
            intVar=1;
            floatVar=2;
            if(intVar!=floatVar) return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(intVar),Id(floatVar))"
        self.assertTrue(TestChecker.test(input,expect,475))
    
    def test_mismatch_in_array_binary_expression_and(self):
        """expr1&&expr2 expr1,expr2 must be boolType"""
        input = """
        void main(){
            boolean x;
            boolean y;
            int z;
            if(x&&y) return;
            if(x&&z) return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(x),Id(z))"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_mismatch_in_array_binary_expression_or(self):
        """expr1||expr2 expr1,expr2 must be boolType"""
        input = """
        void main(){
            int a;
            boolean b;
            boolean c;
            if(b||c){
                if(a||b){
                    c=b;
                }
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,477))


    def test_mismatch_in_array_binary_expression_assign(self):
        """expr1=expr2 LHS can be in any type except void, arrtype,arraypointertype"""
        input = """
        void main(){
            int a[1];
            a=1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_mismatch_in_array_binary_expression_assign_1(self):
        """expr1=expr2 RHS is either in the same type as that of LHS
        or coerce LHS type"""
        input = """
        void main(){
            int a;
            a=5;
            int b;
            do {
                b="5";
                a=a+1;
            } while a==1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),StringLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,479))
    def test_mismatch_in_array_binary_expression_assign_2(self):
        """expr1=expr2 RHS is either in the same type as that of LHS
        or coerce LHS type"""
        input = """
        void main(){
            int Variable;
            Variable=1;
            int var;
            if(Variable==1) var=2;
            if(Variable==2) var=1.0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(var),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,480))
    def test_mismatch_in_function_call_number_of_para(self):
        """the number of the actual parameters must be the same as 
        that of the formal parameters..."""
        input = """
        void foo(int a,int b){}
        void main(){
            int a;
            int b;
            a=1;
            b=2;
            foo(a,b);
            foo(a);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,481))
    def test_mismatch_in_function_call_type(self):
        """"""
        input = """
        void foo(int a[],float b[]){}
        void main(){
            int a[5]; int b[5];
            foo(a,b);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_mismatch_in_built_in_function(self):
        """mismatch in built in function"""
        input = """
        void main(){
            putIntLn(1);
            putIntLn(1.2);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[FloatLiteral(1.2)])"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_mismatch_in_expresion_in_assign_built_in_func(self):
        """mismatch in built in function"""
        input = """
        void main(){
            int a;
            float b;
            b=getFloat();
            a=getFloat();
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),CallExpr(Id(getFloat),[]))"
        self.assertTrue(TestChecker.test(input,expect,484))
    def test_no_entry_point_one_function(self):
        """no entry point no main function"""
        input = """
        void foo(){
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,485))
    def test_no_entry_point_no_function(self):
        """no entry point"""
        input = """
        int function;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,486))
    def test_no_entry_point_variable_main(self):
        """no entry point with variable main"""
        input = """
        int main;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_no_entry_point_mult_function(self):
        """no entry point with variable main"""
        input = """
        int sum(int a, int b){
            return a+b;
        }
        int sub(int a, int b){
            return a-b;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,488))
    def test_type_mismach_in_fucntion_call(self):
        """type mismatch in function call"""
        input = """
        void sum(){
        }
        void main(int a, int b){
            sum();
            sum;
        }
        """
        expect = "Type Mismatch In Expression: Id(sum)"
        self.assertTrue(TestChecker.test(input,expect,489))
    def test_type_mismatch_in_stmt_complex_do_while_if(self):
        """type mismatch in stmt complex"""
        input = """
        void main(){
            do {
                int a;
                if(false){
                    if(a){
                        return;
                    }
                }
            }while (true);
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),Block([Return()]))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_type_mismatch_in_stmt_complex_do_while_if_for(self):
        """type mismatch in stmt complex"""
        input = """
        void main(){
            int x;
            for(x=0;x<5;x=x+1){
                do{
                    if(x==2) return;
                }while x;
            }
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([If(BinaryOp(==,Id(x),IntLiteral(2)),Return())])],Id(x))"
        self.assertTrue(TestChecker.test(input,expect,491)) 
    def test_not_return_complex(self):
        """type mismatch in stmt complex"""
        input = """
        int main(){
            int x;
            for(x=0;x<5;x=x+1){
                do{
                    if(x==2) return 1;
                    else{
                        
                    }
                }while x==1;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,492))
    def test_function_not_return_complex_dowhile_nested(self):
        """function not return with nested dowhile"""
        input = """
            int sum(){
            }
            void main(){
               int a;
               function(a);
            }
            int function(float a){
                do {
                    do{
                        do{
                            return 1;
                        }while (true);
                    }while true;
                }
                while true;
                
            }    
        """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input,expect,493))
    def test_type_mismatch_compex_with_function_call(self):
        """unreachable function complex"""
        input = """
            int xyz(){
                return 123;
            }
            void main(){
                xyz()+xyz();
                xyz()+"123";
                abc(xyz(),123,true);
            }
            int abc(int a,int b,boolean c){
                if(c){
                    return a;
                }
                return b;
            }
           
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(xyz),[]),StringLiteral(123))"
        self.assertTrue(TestChecker.test(input,expect,494))
    def test_type_mismatch_return_complex(self):
        """unreachable function complex"""
        input = """
            int sum(int a,int b){
                return a+b;
            }
            int sub(int a,int b){
                return a-b;
            }
            int main(){
                int a;
                int b;
                a=1;
                b=1;
                sum(a,b);
                sub(a,b);
                return foo()+sum(a,b);
            }
            float foo(){
                int intVar;
                intVar=foo()+1;
                return 2.0;
            }
        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(+,CallExpr(Id(foo),[]),CallExpr(Id(sum),[Id(a),Id(b)])))"
        self.assertTrue(TestChecker.test(input,expect,495))
    def test_unreachable_function_complex(self):
        """unreachable function complex"""
        input = """
            int mul(int a,int b){
                return a*b;
            }
            int div(int a,int b){
                return a/b;
            }
            float caculator(int a,int b){
                return mul(a,b)*div(a,b);
            }
            float sum(int a,int b){
                return a+b;
            }
            void main(){
                int a;
                int b;
                a=5;
                b=a;
                caculator(a,b);
            }
        """
        expect = "Unreachable Function: sum"
        self.assertTrue(TestChecker.test(input,expect,496))
    def test_unreachable_function_complex_with_recursive(self):
        """unreachable function complex"""
        input = """
            int sum(int a[]){
                return sum(a);
            }
            void main(){
            }
        """
        expect = "Unreachable Function: sum"
        self.assertTrue(TestChecker.test(input,expect,497))
    def test_unreachable_function_more_complex(self):
        """unreachable function complex"""
        input = """
            float foo(){
                return 1;
            }
            float fuu(){
                return foo();
            }
            float functioncall(){
                return fuu();
            }
            int sum(int a[]){
                return sum(a);
            }
            void main(){
                functioncall();
            }
        """
        expect = "Unreachable Function: sum"
        self.assertTrue(TestChecker.test(input,expect,498))
    def test_complex_overall(self):
        """overall test"""
        input = """
            int[] foo(){
                int a[5];
                int b[5];
                return a;
            }
            int main(){
                int a;
                float b;
                string c;
                boolean d;
                if(d==true) return 1;
                for(a=0;a<5;a=a+1){
                    if(true)
                        return 1;
                }
                int x;
                do{
                    int x;
                    x=x+1;
                }while x<5;
                foo();
                check(a,c);
            }
            float check(int a,string b){
                return 1.0;
            }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,499))
