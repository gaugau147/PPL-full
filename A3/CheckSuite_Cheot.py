import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):

    ############# Test Redeclared Variable ###############
    def test_redeclared_variable_1(self):
        input = """
        int a;
        int a;
        int main() {
            a = 1;
            return 0;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared_variable_2(self):
        input = """
        int main() {
            int b;
            b = 1;
            int b;
            b = 2;
            return 9;
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared_variable_3(self):
        input = """
        void main() {
            {
                int a;
                a = 1;
                int a;
                a = 2;
            }
            return;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared_variable_4(self):
        input = """
        void main(int a) {
            int a;
            a = 1;
            return;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared_variable_5(self):
        input = """
        void main(int a) {
            a = 1;
            int b;
            b = 2;
            {
                int c;
                c = 3;
                {
                    int d;
                    d = 4;
                    int d;
                    d = 5;
                }
            }
            return;
        }
        """
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared_variable_6(self):
        input = """
        void main(int a) {
            a = 0;
            {
                {
                    int x;
                    x = 1;
                }
                int x;
                x = 2;
            }
            int a;
            a = 3;
            return;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_redeclared_variable_7(self):
        input = """
        int a;
        void main() {
            a = 1;
            return;
        }
        int a;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 406))

    ############# Test Redeclared Parameter ###############
    def test_redeclared_parameter_1(self):
        input = """
        void main() {return;}
        int foo(int a, int a[]){return 1;}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redeclared_parameter_2(self):
        input = """
        void main() {return;}
        int foo(int b, boolean b){return 1;}
        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redeclared_parameter_3(self):
        input = """
        void main() {return;}
        int foo(int a[], boolean b, string a){
            return 1;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 409))

    ############# Test Redeclared Function ###############
    def test_redeclared_function_1(self):
        input = """
        void main() {return;}
        int foo(int a){return 1;}
        int foo(int a){return 0;}
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_redeclared_function_2(self):
        input = """
        void main() {return;}
        int foo(int a){return 1;}
        int foo(int a, int b){return 0;}
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_redeclared_function_3(self):
        input = """
        void main() {return;}
        int foo2(){return;}
        boolean foo2(int a, int b){return 0;}
        """
        expect = "Redeclared Function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_redeclared_function_4(self):
        input = """
        string[] foo3(){return;}
        boolean[] foo3(int a, int b){return 0;}
        void main() {return;}
        """
        expect = "Redeclared Function: foo3"
        self.assertTrue(TestChecker.test(input, expect, 411))

    ############# Test Undeclared Identifier ###############
    def test_undeclared_identifier_1(self):
        input = """
        int a;
        void main() {b = 2; return;}
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_undeclared_identifier_2(self):
        input = """
        int a;
        void main() {
            a = 5;
            c = 6;
            return;
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_undeclared_identifier_3(self):
        input = """
        int a;
        int c;
        void main() {
            a = 5;
            c = 6;
            {
                d = 6;
            }
            return;
        }
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 412))

    ############# Test Undeclared Function ###############
    def test_undeclared_function_1(self):
        input = """
        int main(){
            return foo();
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_undeclared_function_2(self):
        input = """
        int foo(int a){
            return 1;
        }

        void main(){
            foo(b(1));
            return;
        }
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_undeclared_function_3(self):
        input = """
        string a;
        int main(){
            a = foo2("bcd");
            return 0;
        }
        """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 414))

    ############# Test Type Mismatch In Statement ###############
    # IF stmt
    def test_type_mismatch_in_statement_if_1(self):
        input = """
        int main(){
            int a;
            a = 1;
            if (a)
                a = a + 1;
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_type_mismatch_in_statement_if_2(self):
        input = """
        int main(){
            string a;
            a = "hhihi";
            if (a)
                a = "test ne````";
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),BinaryOp(=,Id(a),StringLiteral(test ne````)))"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_type_mismatch_in_statement_if_3(self):
        input = """
        int main(){
            float a;
            a = 1e-5;
            if (a)
                a = 1;
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),BinaryOp(=,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_type_mismatch_in_statement_if_4(self):
        input = """
        int main(){
            float a;
            a = 1e-5;
            if (a)
                a = 1;
            else
                a = 1.2;
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(=,Id(a),FloatLiteral(1.2)))"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_type_mismatch_in_statement_if_6(self):
        input = """
        int fooInt() {return 1;}
        int main(){
            if (fooInt()) {
                return 1;
            }
            else {
                return 2;
            }
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(fooInt),[]),Block([Return(IntLiteral(1))]),Block([Return(IntLiteral(2))]))"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_type_mismatch_in_statement_if_7(self):
        input = """
        string fooString() {return "abc";}
        int main(){
            if (fooString())
                return 1;
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(fooString),[]),Return(IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_type_mismatch_in_statement_if_8(self):
        input = """
        void fooVoid() {return;}
        int main(){
            if (fooVoid())
                return 1;
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(fooVoid),[]),Return(IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 416))

        input = """
        int main(){
            if ("boolean")
                return 1;
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: If(StringLiteral(boolean),Return(IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 417))

    # FOR stmt
    def test_type_mismatch_in_statement_for_1(self):
        # condi2 == IntType
        input = """
        void main() {
            for (1; 2; 3) {}
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);IntLiteral(2);IntLiteral(3);Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_type_mismatch_in_statement_for_2(self):
        # condi2 == StringType
        input = """
        void main() {
            for (1; "boolean"; 3) {}
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);StringLiteral(boolean);IntLiteral(3);Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_type_mismatch_in_statement_for_3(self):
        # condi2 == FloatType
        input = """
        void main() {
            for (1; 1.2e-9; 3) {}
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);FloatLiteral(1.2e-09);IntLiteral(3);Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_type_mismatch_in_statement_for_4(self):
        # condi1 == BoolType
        input = """
        void main() {
            for (true; true; 3) {}
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(BooleanLiteral(true);BooleanLiteral(true);IntLiteral(3);Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_type_mismatch_in_statement_for_5(self):
        # condi1 == FloatType
        input = """
        void main() {
            for (1.0; false; 3) {}
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(FloatLiteral(1.0);BooleanLiteral(false);IntLiteral(3);Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_type_mismatch_in_statement_for_6(self):
        # condi1 == StringType
        input = """
        void main() {
            for ("condi1"; false; 3) {}
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(StringLiteral(condi1);BooleanLiteral(false);IntLiteral(3);Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_type_mismatch_in_statement_for_7(self):
        # condi3 == StringType
        input = """
        void main() {
            for (1; false; "condi3") {}
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);BooleanLiteral(false);StringLiteral(condi3);Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_type_mismatch_in_statement_for_8(self):
        # condi3 == BoolType
        input = """
        void main() {
            for (1; false; true) {}
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);BooleanLiteral(false);BooleanLiteral(true);Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_type_mismatch_in_statement_for_9(self):
        # condi3 == FloatType
        input = """
        void main() {
            for (1; false; 1.2) {}
            return;
        }
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);BooleanLiteral(false);FloatLiteral(1.2);Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    # DO-WHILE stmt
    def test_type_mismatch_in_statement_dowhile_1(self):
        # condi == StringType
        input = """
        void main() {
            do {} while("trueorFalse");
            return;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],StringLiteral(trueorFalse))"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_type_mismatch_in_statement_dowhile_2(self):
        # condi == IntType
        input = """
        void main() {
            do {} while(1);
            return;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_type_mismatch_in_statement_dowhile_3(self):
        # condi == FloatType
        input = """
        void main() {
            do {} while(1.2);
            return;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],FloatLiteral(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 419))

    # RETURN stmt
    def test_type_mismatch_in_statement_return_1(self):
        # VoidType <- IntType
        input = """
        void main() {
            return 5;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(5))"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_type_mismatch_in_statement_return_2(self):
        # VoidType <- BoolType
        input = """
        void main() {
            return true;
        }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_type_mismatch_in_statement_return_3(self):
        # VoidType <- FloatType
        input = """
        void main() {
            return 1.2e-5;
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.2e-05))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_type_mismatch_in_statement_return_5(self):
        # IntType <- VoidType
        input = """
        int main() {
            return;
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_type_mismatch_in_statement_return_6(self):
        # IntType <- BoolType
        input = """
        int main() {
            return true;
        }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_type_mismatch_in_statement_return_8(self):
        # IntType <- StringType
        input = """
        int main() {
            return "return";
        }
        """
        expect = "Type Mismatch In Statement: Return(StringLiteral(return))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_type_mismatch_in_statement_return_9(self):
        # IntType <- StringType
        input = """
        int main() {
            return "return";
        }
        """
        expect = "Type Mismatch In Statement: Return(StringLiteral(return))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_type_mismatch_in_statement_return_10(self):
        # StringType <- VoidType
        input = """
        string main() {
            return;
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_type_mismatch_in_statement_return_13(self):
        # StringType <- BoolType
        input = """
        string main() {
            return false;
        }
        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_type_mismatch_in_statement_return_15(self):
        # FloatType <- StringType
        input = """
        float main() {
            return "false";
        }
        """
        expect = "Type Mismatch In Statement: Return(StringLiteral(false))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_type_mismatch_in_statement_return_18(self):
        # BoolType <- VoidType
        input = """
        boolean main() {
            return;
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_type_mismatch_in_statement_return_19(self):
        # BoolType <- IntType
        input = """
        boolean main() {
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 425))

        # BoolType <- StringType
        input = """
        boolean main() {
            return "hihihi";
        }
        """
        expect = "Type Mismatch In Statement: Return(StringLiteral(hihihi))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    ########## Test Type Mismatch In Expression #########
    # Array subscripting
    def test_type_mismatch_in_expression_subscripting_1(self):
        input = """
        int main() {
            int a[5];
            int b;
            b = a[true];
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_type_mismatch_in_expression_subscripting_2(self):
        input = """
        int main() {
            int a[5];
            int b;
            b = a["hihi"];
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),StringLiteral(hihi))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_type_mismatch_in_expression_subscripting_3(self):
        input = """
        int main() {
            int a[5];
            int b;
            b = a[1.2];
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_type_mismatch_in_expression_subscripting_4(self):
        input = """
        int main() {
            int a;
            a[1] = 2;
            return 1;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_type_mismatch_in_expression_subscripting_5(self):
        input = """
        string[] foo(){
            string a[5];
            return a;
        }
        int main() {
            boolean foo;
            foo[1] = 2;
            return 1;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(foo),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    # Binary and Unary Operator
    def test_type_mismatch_in_expression_op_1(self):
        input = """
        void main() {
            int a;
            a = 1;
            float b;
            b = 2.0;
            b = a; // Type coerce
            a % b; // WRONG
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_type_mismatch_in_expression_op_2(self):
        input = """
        void main() {
            string _string;
            _string = "123";
            float _float;
            _float = 2.7;
            _string == _float; // WRONG
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(_string),Id(_float))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_type_mismatch_in_expression_op_3(self):
        input = """
        void main() {
            int a[5];
            a[1] = 1;
            string b[10];
            b[2] = "abc";

            a[1] != b[2]; // WRONG

            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,ArrayCell(Id(a),IntLiteral(1)),ArrayCell(Id(b),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_in_expression_op_4(self):
        input = """
        void main() {
            boolean a;
            a = (true && false);
            boolean b;
            b = (true == false);
            a == b;
            a != b;
            !a;
            a && b;
            a || b;
            a = b;

            a+b; // WRONG
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_in_expression_op_5(self):
        input = """
        void main() {
            boolean a;
            a = (true || false);
            boolean b;
            b = !false;

            a*b; // WRONG
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_in_expression_op_6(self):
        input = """
        void main() {
            boolean a;
            a = true;
            boolean b;
            b = true && true;

            a/b; // WRONG
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_in_expression_op_7(self):
        input = """
        void main() {
            boolean a;
            boolean b;
            a = true && !true;
            b = false || false;

            a%b; // WRONG
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_in_expression_op_8(self):
        input = """
        void main() {
            boolean a;
            boolean b;
            a = true && !true;
            b = false || false;

            a-b; //WRONG
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_in_expression_op_9(self):
        input = """
        void main() {
            boolean a;
            boolean b;
            a = true && !true;
            b = false || false;

            a < b; // WRONG
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_in_expression_op_10(self):
        input = """
        void main() {
            boolean booVar;
            string stringVar;
            float floatVar;
            int intVar;
            booVar = true;
            stringVar = "example";
            floatVar = 3.6;
            intVar = 9;
            intVar + intVar;
            intVar - intVar;
            intVar * intVar;
            intVar / intVar;
            intVar % intVar;
            intVar < intVar;
            intVar <= intVar;
            intVar >= intVar;
            intVar > intVar;
            intVar == intVar;
            intVar != intVar;
            intVar = intVar;

            !intVar; // WRONG
            return;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(intVar))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_in_expression_op_11(self):
        input = """
        void main() {
            boolean booVar;
            string stringVar;
            float floatVar;
            int intVar;

            booVar = true;
            stringVar = "example";
            floatVar = 3.6;
            intVar = 9;

            intVar || intVar; // WRONG
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(intVar),Id(intVar))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_in_expression_op_12(self):
        input = """
        void main() {
            boolean booVar;
            string stringVar;
            float floatVar;
            int intVar;

            booVar = true;
            stringVar = "example";
            floatVar = 3.6;
            intVar = 9;

            intVar && intVar;
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(intVar),Id(intVar))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_in_expression_op_13(self):
        input = """
        void main() {
            boolean booVar;
            string stringVar;
            float floatVar;
            int intVar;
            booVar = true;
            stringVar = "example";
            floatVar = 3.6;
            intVar = 9;

            floatVar + floatVar;
            floatVar - floatVar; 
            floatVar * floatVar; 
            floatVar / floatVar; 
            -floatVar;
            floatVar < floatVar; 
            floatVar <= floatVar; 
            floatVar > floatVar; 
            floatVar >= floatVar; 
            floatVar = floatVar;

            !floatVar;
            return;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(floatVar))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_type_mismatch_in_expression_op_14(self):
        input = """
        void main() {
            boolean booVar;
            string stringVar;
            float floatVar;
            int intVar;

            booVar = true;
            stringVar = "example";
            floatVar = 3.6;
            intVar = 9;

            floatVar == floatVar;
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(floatVar),Id(floatVar))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_type_mismatch_in_expression_op_15(self):
        input = """
        void main() {
            boolean booVar;
            string stringVar;
            float floatVar;
            int intVar;

            booVar = true;
            stringVar = "example";
            floatVar = 3.6;
            intVar = 9;

            floatVar != floatVar;
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(floatVar),Id(floatVar))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_type_mismatch_in_expression_op_16(self):
        input = """
        void main() {
            boolean booVar;
            string stringVar;
            float floatVar;
            int intVar;

            booVar = true;
            stringVar = "example";
            floatVar = 3.6;
            intVar = 9;

            floatVar || floatVar;
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(floatVar),Id(floatVar))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_type_mismatch_in_expression_op_17(self):
        input = """
        void main() {
            boolean booVar;
            string stringVar;
            float floatVar;
            int intVar;

            booVar = true;
            stringVar = "example";
            floatVar = 3.6;
            intVar = 9;

            floatVar && floatVar;
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(floatVar),Id(floatVar))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_type_mismatch_in_expression_op_18(self):
        input = """
        void main() {
            boolean booVar;
            string stringVar;
            float floatVar;
            int intVar;

            booVar = true;
            stringVar = "example";
            floatVar = 3.6;
            intVar = 9;

            stringVar = stringVar;
            putString(stringVar);
            putStringLn(stringVar);

            stringVar + stringVar;
            return;

        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(stringVar),Id(stringVar))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_type_mismatch_in_expression_op_19(self):
        input = """
        void main() {
            boolean booVar;
            string stringVar;
            float floatVar;
            int intVar;
            booVar = true;
            stringVar = "example";
            floatVar = 3.6;
            intVar = 9;
            stringVar = stringVar;
            putString(stringVar);
            putStringLn(stringVar);

            stringVar && stringVar;
            return;

        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(stringVar),Id(stringVar))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    # Function call
    def test_type_mismatch_in_expression_functioncall_1(self):
        input = """
        void foo(int a) {
            return;
        }
        void main() {
            foo();
            return;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_type_mismatch_in_expression_functioncall_2(self):
        input = """
        void foo(int a) {
            return;
        }
        void main() {
            int a, b, c;
            foo(a, b, c);
            return;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a),Id(b),Id(c)])"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_type_mismatch_in_expression_functioncall_3(self):
        input = """
        int foo(int a) {
            return 1;
        }
        void main() {
            string _string;
            foo(_string);
            return;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(_string)])"
        self.assertTrue(TestChecker.test(input, expect, 432))

    ########## Test Funtion Not Return #########
    def test_function_not_return_1(self):
        input = """
        int main() {
            int a;
            a = 1;
            a;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_function_not_return_2(self):
        input = """
        string foo(string a, string b[]) {
            string _string;
        }
        int main() {
            int a;
            a = 2;
            return a;
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_function_not_return_3(self):
        input = """
        int main() {
            int a;
            a = 3;
            if (true)
                return 0;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_function_not_return_4(self):
        input = """
        int main() {
            int a;
            a = 4;
            if (true)
                return 0;
            else
                a = 1;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_function_not_return_5(self):
        input = """
        int main() {
            int a;
            a = 5;
            if (true) {} 
            else {
                a = 1;
                return 1;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_function_not_return_6(self):
        input = """
        int main() {
            int a;
            a = 6;
            if (true)
                return 0;
            else {}
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_function_not_return_7(self):
        input = """
        int foo() {
            int a;
            a = 1;
            do {
                a;
                return 0;
            } while false;
        }
        int main() {
            int a;
            a = 1;
            do {
                a;
            } while true;
        }   
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_function_not_return_8(self):
        input = """
        int main() {
            int a;
            a = 1;
            for (a; a < 2; a = a + 1){
                int b;
                b = 1;
                return 1;
            }
        }   
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 441))

    ########## Test Break/Continue Not In Loop #########
    # Continue stmt
    def test_continue_not_in_loop_1(self):
        input = """
        void main() {
            int i;
            i = 1;
            continue;
            for (i; i < 5; i = i + 1) {
                if (i <= 5) return;
                else i;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_continue_not_in_loop_2(self):
        input = """
        void main() {
            int i;
            i = 1;
            for (i; i < 5; i = i + 1) {
                if (i <= 5) return;
                else i;
                do
                    continue; //OK
                while true;
            }
            continue; // WRONG
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_continue_not_in_loop_3(self):
        input = """
        void main() {
            int i;
            i = 1;
            for (i; i < 5; i = i + 1) {
                if (i <= 5) return;
                else i;
                continue; // OK
            }
            continue; // WRONG
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 443))

    # Break stmt
    def test_break_not_in_loop_1(self):
        input = """
        void main() {
            int i;
            i = 1;
            break;
            for (i; i < 5; i = i + 1) {
                if (i <= 5) return;
                else i;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_break_not_in_loop_2(self):
        input = """
        void main() {
            int i;
            i = 1;
            for (i; i < 5; i = i + 1) {
                if (i <= 5) return;
                else i;
                do
                    break; //OK
                while true;
            }
            break; // WRONG
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_break_not_in_loop_3(self):
        input = """
        void main() {
            int i;
            i = 1;
            for (i; i < 5; i = i + 1) {
                if (i <= 5) return;
                else i;
                break; // OK
            }
            break; // WRONG
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 443))

    ########## Test No Entry Point ############
    def test_entry_point_1(self):
        input = """
        int a;
        void foo() {
            a = 1;
            return;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_entry_point_2(self):
        input = """
        int mAin() {
            int a;
            a = 2;
            return 5;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_entry_point_3(self):
        input = """
        void foo(int a) {
            return;
        }

        int a;

        int func() {
            a = 4;
            return 5;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))

    ########## Test Unreachable Function #########
    def test_unreachable_function_1(self):
        input = """
        string fooString() {
            return "return";
        }
        int fooInt() {
            return 1;
        }
        void main() {
            fooInt();
        }
        """
        expect = "Unreachable Function: fooString"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_unreachable_function_2(self):
        input = """
        string fooString() {
            return "return";
        }
        int fooInt() {
            fooString()
            return 1;
        }
        void main() {}
        """
        expect = "Unreachable Function: fooInt"
        self.assertTrue(TestChecker.test(input, expect, 444))

    ########## Test Not Left Value #########

    def test_not_left_value_1_use_ast(self):
        '''
        void main() {
            int a;
            int array[5];

            a = 1; //OK
            array[1] = 1; //OK

            a + 1 = 1; //WRONG
        }
        '''
        input = Program([FuncDecl(Id('main'), [], VoidType(), Block([VarDecl('a', IntType()), VarDecl('array', ArrayType(5, IntType())), BinaryOp('=', Id('a'), IntLiteral(
            1)), BinaryOp('=', ArrayCell(Id('array'), IntLiteral(1)), IntLiteral(1)), BinaryOp('=', BinaryOp('+', Id('a'), IntLiteral(1)), IntLiteral(1))]))])
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_not_left_value_2_use_ast(self):
        '''
        void main() {
            int a;
            int array[5];

            a = 1; //OK
            array[1] = 1; //OK

            foo() = 1; //WRONG
        }
        '''
        input = Program([FuncDecl(Id('foo'), [], IntType(), Block([Return(IntLiteral(0))])), FuncDecl(Id('main'), [], VoidType(), Block([VarDecl('a', IntType()), VarDecl('array', ArrayType(
            5, IntType())), BinaryOp('=', Id('a'), IntLiteral(1)), BinaryOp('=', ArrayCell(Id('array'), IntLiteral(1)), IntLiteral(1)), BinaryOp('=', CallExpr(Id('foo'), []), IntLiteral(1))]))])

        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_not_left_value_3_use_ast(self):
        '''
        void main() {
            int a;
            int array[5];

            a = 1; //OK
            array[1] = 1; //OK

            1 = 1; //WRONG
        }
        '''
        input = Program([FuncDecl(Id('main'), [], VoidType(), Block([VarDecl('a', IntType()), VarDecl('array', ArrayType(5, IntType())), BinaryOp(
            '=', Id('a'), IntLiteral(1)), BinaryOp('=', ArrayCell(Id('array'), IntLiteral(1)), IntLiteral(1)), BinaryOp('=', IntLiteral(1), IntLiteral(1))]))])
        expect = "Not Left Value: IntLiteral(1)"
        self.assertTrue(TestChecker.test(input, expect, 447))