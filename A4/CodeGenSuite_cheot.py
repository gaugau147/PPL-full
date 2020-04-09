import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            int x;
            putInt(100);
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    
    def test_float(self):
        input = """
        void main() {
            putFloat(1.2);
        }
        """
        expect = "1.2"
        self.assertTrue(TestCodeGen.test(input,expect,501))

    def test_string(self):
        input = """
        void main() {
            putString("test");
        }
        """
        expect = "test"
        self.assertTrue(TestCodeGen.test(input,expect,502))

    def test_boolean_1(self):
        input = """
        void main() {
            putBool(true);
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test_boolean_2(self):
        input = """
        void main() {
            putBool(false);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_binop_add_int(self):
        input = """
        void main() {
            putInt(1 + 2);
        }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_binop_sub_int(self):
        input = """
        void main() {
            putInt(1 - 2);
        }
        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_binop_add_float(self):
        input = """
        void main() {
            putFloat(1.2 + 2 + 1.25);
        }
        """
        expect = "4.45"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_binop_sub_float(self):
        input = """
        void main() {
            putFloat(1 - 2.0 - 0.5);
        }
        """
        expect = "-1.5"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_binop_div_int(self):
        input = """
        void main() {
            putInt(3 / 2);
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_bin_op_div_int_show_float(self):
        input = """
        void main() {
            putFloat(3 / 2);
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,510))

    def test_binop_mul_int(self):
        input = """
        void main() {
            putInt(3 * 2 * 3);
        }
        """
        expect = "18"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_binop_div_float(self):
        input = """
        void main() {
            putFloat(3.1 / 2 / 2);
        }
        """
        expect = "0.775"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_binop_mul_float(self):
        input = """
        void main() {
            putFloat(3.1 * 2 * 3);
        }
        """
        expect = "18.599998"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_binop_mod(self):
        input = """
        void main() {
            putIntLn(5 % 3);
            putIntLn(9 % 3);
            putIntLn(2 % 3);
            putIntLn(4 % 3);
        }
        """
        expect = """2
0
2
1
"""
        self.assertTrue(TestCodeGen.test(input,expect,514))

    def test_binop_boolean_1(self):
        input = """
        void main() {
            putBool(true && true)
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test_binop_boolean_2(self):
        input = """
        void main() {
            putBool(true && false)
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test_binop_boolean_3(self):
        input = """
        void main() {
            putBool(true || true)
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test_binop_boolean_4(self):
        input = """
        void main() {
            putBool(true || false)
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,518))

    def test_binop_boolean_5(self):
        input = """
        void main() {
            putBool(true || true && false || true)
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,519))

    def test_binop_boolean_6(self):
        input = """
        void main() {
            putBool(false && (false && true) || false)
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test_binop_compare_int(self):
        input = """
        void main() {
            putBool(1123 > 231424536);
            putBool(1123 < 231424536);
            putBool(1123 == 231424536);
            putBool(1123 == 1123);
            putBool(1123 >= 314245362);
            putBool(1123 <= 314245362);
            putBool(1123 != 314245362);
        }
        """
        expect = "falsetruefalsetruefalsetruetrue"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_binop_compare_float(self):
        input = """
        void main() {
            putBool(545.231 > 231424536.232);
            putBool(545.231 < 231424536);
            putBool(545.231 >= 314245362.23234324);
            putBool(545.231 <= 314245362.123123123);
            putBool(545.231 != 314245362);
        }
        """
        expect = "falsetruefalsetruetrue"
        self.assertTrue(TestCodeGen.test(input,expect,522))

    def test_binop_compare_mix(self):
        input = """
        void main() {
            putBool(1 + 2 + 3 > 1);
            putBool(5 * 2 / (3 % 2) + 1 < 1 * 2);
            putBool(9 * 3 == 9 + 9 + 9);
            putBool(2 * 2.3 > 3 * 9.23);
            putBool(1.212 / 2 + 1 >= 2.3331 / 2 / 2);
            putBool(9.72 * 3 + 5 <= 9.99 * 1 + 2 - 2.0 / 3 + 999);
            putBool(2313 * 2 / 3 + 2 != 2 / 314245362 * 999 + 2);
        }
        """
        expect = "truefalsetruefalsetruetruetrue"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_unop_sub_int(self):
        input = """
        void main() {
            putInt(-5);
        }
        """
        expect = "-5"
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_unop_sub_float(self):
        input = """
        void main() {
            putFloat(-5.55);
        }
        """
        expect = "-5.55"
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test_unop_not_true(self):
        input = """
        void main() {
            putBool(!true);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_unop_not_false(self):
        input = """
        void main() {
            putBool(!false);
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_unop_not_mix_1(self):
        input = """
        void main() {
            putBool(!!false);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,528))

    def test_unop_not_mix_2(self):
        input = """
        void main() {
            putBool(!!true && !false || false);
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_unop_sub_mix_1(self):
        input = """
        void main() {
            putInt(-5 - -2)
        }
        """
        expect = "-3"
        self.assertTrue(TestCodeGen.test(input,expect, 530))

    def test_unop_sub_mix_2(self):
        input = """
        void main() {
            putFloat(-(2*3/6)*(-1))
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect, 531))

    def test_unop_sub_mix_3(self):
        input = """
        void main() {
            putInt(-5 - -2 + (-4))
        }
        """
        expect = "-7"
        self.assertTrue(TestCodeGen.test(input,expect, 532))

    def test_var_decl_global(self):
        input = """
        int x;
        int y;
        int a,b,c;
        void main() {
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,533))

    def test_var_decl_global_and_use_1(self):
        input = """
        int x;
        int y;
        int a,b,c;
        void main() {
            x = 1;
            putInt(x);
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,534))

    def test_var_decl_global_and_use_2(self):
        input = """
        int x;
        int y;
        int a,b,c;
        void main() {
            x = 1;
            putInt(x);
            putInt(foo());
        }
        int foo(){
            x = 9;
            return x;
        }
        """
        expect = "19"
        self.assertTrue(TestCodeGen.test(input,expect,535))

    def test_var_decl_local(self):
        input = """
        void main() {
            int x;
            int y;
            int a,b,c;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,536))

    def test_assign_integer(self):
        input = """
        void main() {
            int x;
            x = 1;
            putInt(x);
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,537))
    
    def test_assign_string(self):
        input = """
        void main() {
            string x;
            x = "Hello World";
            putString(x);
        }
        """
        expect = "Hello World"
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_assign_float(self):
        input = """
        void main() {
            float x;
            x = 1.0009;
            putFloat(x);
        }
        """
        expect = "1.0009"
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_assign_multiple(self):
        input = """
        void main() {
            // int var;
            // var = 1;
            int x, y, z, t;
            x = y = z = t = 1;
            putInt(x);
            putInt(y);
            putInt(z);
            putInt(t);
        }
        """
        expect = "1111"
        self.assertTrue(TestCodeGen.test(input,expect,540))

    def test_assign_mix(self):
        input = """
        void main() {
            int x, y;
            x = 1;
            y = 2;
            int z;
            z = y*y + x;
            putInt(z);
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,541))

    def test_assign_global_var_declare(self):
        input = """
        int x;
        int y;
        void main() {
            x = 1;
            y = x + 2;
            putIntLn(x);
            putIntLn(y);
        }
        """
        expect = """1
3
"""
        self.assertTrue(TestCodeGen.test(input,expect,542))

    
    def test_block_var_delcare(self):
        input = """
        void main() {
            string x;
            x = "outter";
            putStringLn(x);
            {
                string y;
                y = "inner";
                putStringLn(y);
            }
            putStringLn(x);
        }
        """
        expect = """outter
inner
outter
"""
        self.assertTrue(TestCodeGen.test(input,expect,543))

    def test_var_scope_1(self):
        input = """
        void main() {
            string x;
            x = "original";
            putStringLn(x);
            {
                x = "new value";
                putStringLn(x);
            }
            putStringLn(x);
        }
        """
        expect = """original
new value
new value
"""
        self.assertTrue(TestCodeGen.test(input,expect,544))

    def test_var_scope_2(self):
        input = """
        void main() {
            {
                int a;
                a = 1;
                putInt(1);
            }
            {
                boolean b;
                b = true;
                putBool(b);
            }
        }
        """
        expect = """1true"""
        self.assertTrue(TestCodeGen.test(input,expect,545))

    def test_var_scope_3(self):
        input = """
        void main() {
            boolean b;
            b = false;
            putBool(b);
            {
                int a;
                a = 1;
                putInt(a);
            }
            {
                 b = true;
                 putBool(b);
            }
            putBool(b);
            //putStringLn("This program will raise error!");

        }
        """
        expect = """false1truetrue"""
        self.assertTrue(TestCodeGen.test(input,expect,546))

    def test_simple_program_1(self):
        input = """
        void main() {
            int a;
            a = 1;
            putIntLn(a);
            int b;
            b = 2;
            a = b;
            putIntLn(b);
            putIntLn(a);
            return;
        }
        """
        expect = """1
2
2
"""
        self.assertTrue(TestCodeGen.test(input,expect,547))


    def test_simple_program_2(self):
        input = """
        void main() {
            float a;
            a = 1.1 * 2 + 3 / 4;
            putFloatLn(a);
            float b;
            b = 3.6;
            a = b * 2 + 4.7 / 2 * a * a / b + 2 / 4;
            putFloatLn(b);
            putFloatLn(a);
            return;
        }
        """
        expect = """2.2
3.6
10.359445
"""
        self.assertTrue(TestCodeGen.test(input,expect,548))

    def test_func_declare_1(self):
        input = """
        void foo(){
            putString("This is foo!");
        }

        void main() {
            foo();
        }
        """
        expect = """This is foo!"""
        self.assertTrue(TestCodeGen.test(input,expect,549))

    def test_func_declare_2(self):
        input = """
        void foo(){
            putStringLn("This is foo!");
        }

        void main() {
            foo();
            putStringLn("This is main");
            return;
        }
        """
        expect = """This is foo!
This is main
"""
        self.assertTrue(TestCodeGen.test(input,expect,550))

    def test_func_declare_3(self):
        input = """
        string foo() {
            return "hello";
        }

        void main() {
            putString(foo());
        }
        """
        expect = """hello"""
        self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_func_declare_4(self):
        input = """
        string foo(string a, string b) {
            putString(a);
            putString(b);
            return "hello";
        }

        void main() {
            putString(foo("hihi", "haha"));
        }
        """
        expect = """hihihahahello"""
        self.assertTrue(TestCodeGen.test(input,expect,552))

    def test_func_declare_5(self):
        input = """
        int foo(int a, int b) {
            return a + b;
        }

        void main() {
            int a;
            a = foo(2, 3);
            putIntLn(foo(2, 3));
            putIntLn(a);
        }
        """
        expect = """5
5
"""
        self.assertTrue(TestCodeGen.test(input,expect,553))

    def test_func_declare_6(self):
        input = """
        float foo(int a, int b) {
            return (a + b)/2;
        }

        void main() {
            float a;
            a = foo(2, 3);
            putFloatLn(foo(2, 3));
            putFloatLn(a);
        }
        """
        expect = """2.0
2.0
"""
        self.assertTrue(TestCodeGen.test(input,expect,554))

    def test_func_call_in_func_call_1(self):
        input = """
        int foo() {
            return 2 + 3 + 4;
        }

        void main() {
            int x;
            x = foo();
            putInt(foo());
        }
        """
        expect = """9"""
        self.assertTrue(TestCodeGen.test(input,expect,555))

    def test_func_call_in_func_call_2(self):
        input = """
        int foo1() {
            return 2 + 3 + 4;
        }

        int foo2() {
            return 2 + 3 + 4;
        }

        void main() {
            putInt(foo1() + foo2());
        }
        """
        expect = """18"""
        self.assertTrue(TestCodeGen.test(input,expect,556))

    def test_func_call_in_func_call_3(self):
        input = """
        int foo1(int x) {
            return x*x;
        }

        int foo2(int x) {
            return 2*x;
        }

        void main() {
            putInt(foo1(foo2(1)));
        }
        """
        expect = """4"""
        self.assertTrue(TestCodeGen.test(input,expect,557))

    def test_func_call_in_func_call_4(self):
        input = """
        int foo1(int x) {
            return x*x;
        }

        int foo2(int x, int y) {
            return 2*x + y;
        }

        void main() {
            putInt(foo1(foo2(1, foo1(3))));
        }
        """
        expect = """121"""
        self.assertTrue(TestCodeGen.test(input,expect,558))

    def test_if_else_stmt_both_1(self):
        input = """
        void main() {
            if(true) 
                putInt(1);
            else
                putInt(2);
        }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input,expect,559))

    def test_if_else_stmt_both_2(self):
        input = """
        void main() {
            if (false)  putString("in ra cai nay la tach!");
            else putString("hihi");
        }
        """
        expect = """hihi"""
        self.assertTrue(TestCodeGen.test(input,expect,560))

    def test_if_else_stmt_only_if_1(self):
        input = """
        void main() {
            if (false)  putString("in ra cai nay la tach!");
            putString("in ra cai nay thoi la ok hihi");
        }
        """
        expect = """in ra cai nay thoi la ok hihi"""
        self.assertTrue(TestCodeGen.test(input,expect,561))

    def test_if_else_stmt_only_if_2(self):
        input = """
        void main() {
            if (1 > 3)  putString("1 > 3");
            putString("3 > 1");
        }
        """
        expect = """3 > 1"""
        self.assertTrue(TestCodeGen.test(input,expect,562))
    
    def test_if_else_stmt_mix_1(self):
        input = """
        void main() {
            if (true) putInt(100);
            else if (true) putInt(200);
            else putInt(300);

            if (false) putInt(100);
            else if (true) putInt(200);
            else putInt(300);

            if (false) putInt(100);
            else if (false) putInt(200);
            else putInt(300);
        }
        """
        expect = """100200300"""
        self.assertTrue(TestCodeGen.test(input,expect,563))

    def test_if_else_stmt_block(self):
        input = """
        void main() {
            if (true) {
                putInt(1);
                if (false) putInt(1);
                else if (true) putInt(2);
                else putInt(3);
            } else if (true) 
                putInt(2);
            else 
                putInt(3);

            if (false) {
                putInt(1);
            } else if (true) {
                putInt(2);
                if (false) putInt(1);
                else if (true) putInt(2);
                else putInt(3);
            } else putInt(3);
        }
        """
        expect = """1222"""
        self.assertTrue(TestCodeGen.test(input,expect,564))
    
    def test_do_while_stmt_1(self):
        input = """
        void main() {
            int a;
            a = 5;
            do
                putInt(1);   //5 "1" 4 "1" 3 "1" 2 "1" 1 "1" 0
                a = a - 1;
            while a > 0;
        }
        """
        expect = """11111"""
        self.assertTrue(TestCodeGen.test(input,expect,565))

    def test_do_while_stmt_2(self):
        input = """
        void main() {
            int a;
            a = 5;
            do
                putInt(1);
                a = a - 1;
            while a < 0;
            putInt(a);
        }
        """
        expect = """14"""
        self.assertTrue(TestCodeGen.test(input,expect,566))

    def test_do_while_stmt_3(self):
        input = """
        void main() {
            int loop;
            loop = 4;
            do
                putString("abc ");
                loop = loop - 2;
            while loop >= 1;
        }
        """
        expect = """abc abc """
        self.assertTrue(TestCodeGen.test(input,expect,567))


    def test_for_stmt_1(self):
        input = """
        void main() {
            int i;
            i = 0;
            for (i = 0; i <= 5; i = i + 1) {
                putStringLn("this is sparta!");
            }
        }
        """
        expect = """this is sparta!
this is sparta!
this is sparta!
this is sparta!
this is sparta!
this is sparta!
"""
        self.assertTrue(TestCodeGen.test(input,expect,568))

    def test_for_stmt_2(self):
        input = """
        void main() {
            int i;
            for (i = 0; i <= 5; i = i + 1) {
                putString("a");
            }
        }
        """
        expect = """aaaaaa"""
        self.assertTrue(TestCodeGen.test(input,expect,569))

    def test_for_stmt_3(self):
        input = """
        void main() {
            int i;
            for (i = 0; i <= 5; i = i + 1) {
                putInt(i);
            }
            putInt(i);
        }
        """
        expect = """0123456"""
        self.assertTrue(TestCodeGen.test(input,expect,570))

    def test_for_stmt_4(self):
        input = """
        void main() {
            int i;
            for (i = 0; i <= 5; i = i + 1) {
                putInt(i);
            }
            putInt(i);

            for (i = 0; i <= 0; i = i + 1) {
                putInt(i);
            }
            putInt(i);

            for (i = 0; i <= -2; i = i + 1) {
                putInt(i);
            }
            putInt(i);
        }
        """
        expect = """0123456010"""
        self.assertTrue(TestCodeGen.test(input,expect,571))

    def test_for_stmt_5(self):
        input = """
        void main() {
            int i, sum;
            sum = 0;
            for (i = 0; i <= 5; i = i + 1) {
                sum = sum + i;
            }
            putInt(sum);

        }
        """
        expect = """15"""
        self.assertTrue(TestCodeGen.test(input,expect,572))

    def test_for_stmt_6(self):
        input = """
        void main() {
            int i,j;
            for (i = 0; i <= 1; i = i + 1) {
                for (j = 0; j <= 2; j = j + 1)
                {
                    putInt(i);
                    putInt(j);
                }
            }
        }
        """
        expect = """000102101112"""
        self.assertTrue(TestCodeGen.test(input,expect,573))

    def test_array_vardecl_global(self):
        input = """
        string arrStr[10];
        int arrA[5], arrB[4];
        float arrFloat1[1], arrFloat2[2];
        boolean arrBoo1[2], arrBoo2[3];
        void main() {
        }
        """
        expect = """"""
        self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_array_vardecl_local(self):
        input = """
        void main() {
            string arrStr[10];
            int arrA[5], arrB[4];
            float arrFloat1[1], arrFloat2[2];
            boolean arrBoo1[2], arrBoo2[3];
        }
        """
        expect = """"""
        self.assertTrue(TestCodeGen.test(input,expect,575))

    def test_array_vardecl_and_use_1(self):
        input = """
        void main() {
            int arr[5];
            arr[0] = 1;
            putInt(arr[0]);

            int i;
            i = 1;
            arr[i] = 2;
            arr[i+1] = 3;
            arr[i+2] = 4;
            putInt(arr[i]);
            putInt(arr[i+1]);
            putInt(arr[i+2]);

        }
        """
        expect = """1234"""
        self.assertTrue(TestCodeGen.test(input,expect,576))

    def test_array_vardecl_and_use_2(self):
        input = """
        void main() {
            int a[5];
            a[0] = 9;
            a[1] = a[0];
            putInt(a[0]);
            putInt(a[1]);

        }
        """
        expect = """99"""
        self.assertTrue(TestCodeGen.test(input,expect,577))

    def test_array_vardecl_and_use_3(self):
        input = """
        void main() {
            int a[5];
            a[0] = 9;
            a[1] = a[0]*4 + a[0] - 8;
            putInt(a[0]);
            putInt(a[1]);

        }
        """
        expect = """937"""
        self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_array_vardecl_multi_assign_int(self):
        input = """
        void main() {
            int arr[5];
            arr[0] = arr[1] = arr[2] = 9;
            putInt(arr[0]);
            putInt(arr[1]);
            putInt(arr[2]);
        }
        """
        expect = """999"""
        self.assertTrue(TestCodeGen.test(input,expect,579))

    def test_array_vardecl_multi_assign_float(self):
        input = """
        void main() {
            float arr[5];
            arr[0] = arr[1] = arr[2] = 9.9;
            putFloat(arr[0]);
            putFloat(arr[1]);
            putFloat(arr[2]);
        }
        """
        expect = """9.99.99.9"""
        self.assertTrue(TestCodeGen.test(input,expect,580))

    def test_array_vardecl_multi_assign_string(self):
        input = """
        void main() {
            string arr[5];
            arr[0] = arr[1] = arr[2] = "Hello";
            putString(arr[0]);
            putString(arr[1]);
            putString(arr[2]);
        }
        """
        expect = """HelloHelloHello"""
        self.assertTrue(TestCodeGen.test(input,expect,581))

    def test_array_vardecl_multi_assign_boolean(self):
        input = """
        void main() {
            boolean flag;
            boolean arr[5];
            arr[0] = arr[1] = arr[2] = flag =  3 > 2;
            putBool(arr[0]);
            putBool(arr[1]);
            putBool(arr[2]);
            putBool(flag);
        }
        """
        expect = """truetruetruetrue"""
        self.assertTrue(TestCodeGen.test(input,expect,582))

    def test_break_stmt_in_for(self):
        input = """
        void main() {
            int i;
            for (i = 0; i < 5; i = i + 1) {
                putInt(i);
                break;
            }
        }
        """
        expect = """0"""
        self.assertTrue(TestCodeGen.test(input,expect,583))

    def test_break_stmt_in_dowhile_1(self):
        input = """
        void main() {
            int i;
            i = 1;
            do {
                putInt(i);
                if (i == 5) break;
                i = i + 1;
            } while (true);
        }
        """
        expect = """12345"""
        self.assertTrue(TestCodeGen.test(input,expect,584))

    def test_break_stmt_in_dowhile_2(self):
        input = """
        void main() {
            int index, givenNum;
            index = 0;
            givenNum = 9;
            do {
                if (index == givenNum) break;
                index = index + 1;
            } while true;
            putString("The number is: ");
            putInt(index);
        }
        """
        expect = """The number is: 9"""
        self.assertTrue(TestCodeGen.test(input,expect,585))

    def test_continue_stmt_in_dowhile(self):
        input = """
        void main() {
            int i;
            i = 0;
            do {
                putInt(i)
                i = i + 1;
                if (i < 5) continue;
                putString("hihi")
                if (i == 10) break;
            } while true;
        }
        """
        expect = """01234hihi5hihi6hihi7hihi8hihi9hihi"""
        self.assertTrue(TestCodeGen.test(input,expect,586))

    def test_continue_stmt_in_for(self):
        input = """
        void main() {
            int i;
            for (i = 0; i <= 9; i = i + 1) {
                putInt(i);
                continue;
                putString("printing this is not allowed!");
            }
        }
        """
        expect = """0123456789"""
        self.assertTrue(TestCodeGen.test(input,expect,587))

    def test_mix_program_check_if_greater(self):
        input = """
        boolean isGreater(int a, int b) {
            if (a > b) return true;
            else return false;
        }
        void main() {
            int x, y;
            x = 1;
            y = 2;
            if (isGreater(x, y))
                putString("x is greater than y");
            else
                putString("x is smaller than y");
        }
        """
        expect = """x is smaller than y"""
        self.assertTrue(TestCodeGen.test(input,expect,588))

    def test_mix_program_check_even_or_odd(self):
        input = """
        void main() {
            int num;
            num = 4;
            // True if num is perfectly divisible by 2
            if(num % 2 == 0)
                putString("is even.");
            else
                putString("is odd.");
        }
        """
        expect = """is even."""
        self.assertTrue(TestCodeGen.test(input,expect,589))

    def test_mix_program_find_largest_number(self):
        input = """
        void main() {
            float n1, n2, n3;
            n1 = 1.22;
            n2 = 3.33;
            n3 = 9.99;
            if (n1 >= n2 && n1 >= n3){ 
                putString("n1")
                putString(" is the largest number.");
            }
            if (n2 >= n1 && n2 >= n3){
                putString("n2")
                putString(" is the largest number.");
            }
            if (n3 >= n1 && n3 >= n2){
                putString("n3")
                putString(" is the largest number.");
            }
        }
        """
        expect = """n3 is the largest number."""
        self.assertTrue(TestCodeGen.test(input,expect,590))

    def test_mix_program_find_largest_number_nested(self):
        input = """
        void main() {
            float n1, n2, n3;
            n1 = 1.22;
            n2 = 12.88;
            n3 = 9.99;
            if (n1 >= n2) {
                if (n1 >= n3) {
                    putString("n1");
                    putString(" is the largest number.");
                } else {
                    putString("n3");
                    putString(" is the largest number.");
                }
            } else {
                if (n2 >= n3) {
                    putString("n2");
                    putString(" is the largest number.");
                } else {
                    putString("n3");
                    putString(" is the largest number.");
                }
            }
        }
        """
        expect = """n2 is the largest number."""
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test_mix_program_check_positive_negative(self):
        input = """
        string check(int n) {
            if (n <= 0) {
                if (n == 0)
                    return "The number is ZERO";
                else
                    return "The number is NEGATIVE";
            } else
                return "The number is POSITIVE";
        }

        void main() {
            int n1, n2, n3;
            n1 = -5;
            n2 = 0;
            n3 = 14;
            putStringLn(check(n1));
            putStringLn(check(n2));
            putStringLn(check(n3));
        }
        """
        expect = """The number is NEGATIVE
The number is ZERO
The number is POSITIVE
"""
        self.assertTrue(TestCodeGen.test(input,expect,592))

    def test_mix_program_fibonacci_number(self):
        input = """
        void main() {
            int i, n, t1, t2, nextTerm;
            t1 = 0; t2 = 1;
            n = 9;
            putString("Fibonacci Series: ");
            for (i = 1; i <= n; i = i + 1) {
                putInt(t1); putString(" ");
                nextTerm = t1 + t2;
                t1 = t2;
                t2 = nextTerm;
            }
        }
        """
        expect = """Fibonacci Series: 0 1 1 2 3 5 8 13 21 """
        self.assertTrue(TestCodeGen.test(input,expect,593))
    
    def test_mix_program_simple_two(self):
        input = """
        void main() {
            int x,y,z;
            x = y = z = 1;
            if (x == y && y == z) putBool(2>1); else putBool(2 < 1);
        }
        """
        expect = """true"""
        self.assertTrue(TestCodeGen.test(input,expect,594))

    def test_mix_program_simple_three(self):
        input = """
        void main(){
            int x,y,z;
            x = y = z = 1;
            do {
                putString("hihi");
                break;
                putInt(x);
                putInt(y);
                putInt(z);
            } while(true);
        }
        """
        expect = """hihihihi"""
        self.assertTrue(TestCodeGen.test(input,expect,595))

    def test_program_mix_simple_one(self):
        input = """ void main() {
            int a[10];
            a[0] = a[1] = a[2] = a[3] = a[4] = a[5] = a[6] = a[7] = a[8] = a[9] = a[9] = 1;
            int i;
            for (i = 0; i < 10; i = i + 1)
                putInt(a[i]);
        }

        """
        expect = """1111111111"""
        self.assertTrue(TestCodeGen.test(input,expect,596))


    def test_mix_program_simple_five(self):
        input = """
        int index;
        void main() {
            for (index = 0; index <= 9; index = index + 1) {
                putInt(9);
                if (index == 9) putString("end here");
                else continue;
            }
        }
        """
        expect = """9999999999end here"""
        self.assertTrue(TestCodeGen.test(input,expect,597))

    def test_mix_program_find_largest_element_in_an_array(self):
        input = """
        void main() {
            int i, n;
            n = 10;
            int arr[10];
            arr[0] = -5;
            arr[1] = 1;
            arr[2] = 2;
            arr[3] = 4;
            arr[4] = 9;
            arr[5] = 5;
            arr[6] = 8;
            arr[7] = 10;
            arr[8] = 6;
            arr[9] = 0;
            // storing the largest number to arr[0]
            for (i = 1; i < n; i = i + 1) {
                if (arr[0] < arr[i])
                    arr[0] = arr[i];
            }
            putString("The largest number is: "); putInt(arr[0]);
        }
        """
        expect = """The largest number is: 10"""
        self.assertTrue(TestCodeGen.test(input,expect,598))


    def test_program_mix_find_LCM(self):
        input = """
        void main() {
            int n1, n2, min;
            n1 = 5;
            n2 = 31;
            // maximum number between n1 and n2 is stored in min
            if (n1 > n2) min = n1; else min = n2;
            do {
                if (min % n1 == 0 && min % n2 == 0) {
                    putString("The LCM is: "); putInt(min);
                    break;
                }
                min = min + 1;
            }
            while (true);
        }
        """
        expect = """The LCM is: 155"""
        self.assertTrue(TestCodeGen.test(input,expect,599))


