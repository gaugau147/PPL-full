import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):

    # 2.1 test Redeclare Variable/Function/Parameter
    def test_redeclare_variable1(self):
        input = '''
                int a;
                int a;
                void main(){
                }
           '''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclare_variable2(self):
        input = '''
                   int a;
                   void main(){
                        float b;
                        string b;
                   }
              '''
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclare_variable3(self):
        input = '''
                   int main(){
                   return 0;
                   }
                   int check(){
                        int a;
                        int a;
                   }
              '''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclare_variable4(self):
        input = '''
                   int a;
                   void main(){
                        int a;
                        {
                            int a;
                            int a;
                        }
                        return;
                   }
              '''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclare_variable5(self):
        input = '''
                   void main(){
                   }
                   int foo(){
                        int a;
                        {
                            int a;
                            int a;
                        }
                        return 1;
                   }
              '''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclare_variable6(self):
        input = '''
                   void main(){
                   }
                   int foo(){
                        return 1;
                   }
                   int foo;
              '''
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclare_simple(self):
        """Simple redeclare: int a; int a; """
        input = '''int a;
        int a;
        int main(){
            return 1;
        }'''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_redeclare_different_type(self):
        """Simple redeclare: int a; float a; """
        input = '''int a;
        float a;
        int main(){
            return 1;
        }'''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_redeclare_array_type(self):
        """Simple redeclare: int a; string a[6]; """
        input = '''int a;
        string a[6];
        int main(){
            return 1;
        }'''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_redeclare_para(self):
        """Simple redeclare: void main(int a, int a){
        } """
        input = '''void main(int a, int a){
            return;
        }'''
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redeclare_block(self):
        input = '''void main(int a, int b){
            int c;
            float c;
            return;
        }'''
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_redeclare_block1(self):
        input = '''void main(int a, int b){
            int c;
            float b;
            return;
        }'''
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_redeclare_block2(self):
        input = '''void main(int a, int b){
            int c;
            float d;
            {
                int e;
                string e[8];
            }
            return;
        }'''
        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_redeclare_func(self):
        input = '''
            int main1;
            void main1(int a, int b){
                int c;
                float d;
                {
                    int e;
                    string f[8];
                }
                return;
            }
            int main(){
                main1(1,2);
            return 1;
        }   '''
        expect = "Redeclared Function: main1"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_redeclare_func1(self):
        input = '''
            int a;
            float b;
            void main(){
                return;
            }
            string c[6];
            float main(int a, int b){
                int c;
                return 1.6;
            }'''
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_redeclare_block3(self):
        input = '''void main(int a, int b){
            int c;
            float d;
            {
                int c;
                string e[8];
            }
            return;
        }'''
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_redeclare_block4(self):
        input = '''void main(int a, int b){
            int c;
            float d;
            {
                int f;
                string e[8];
            }
            float c;
            return;
        }'''
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_redeclare_block5(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            {
                int g;
                int h;
                {
                    int i;
                    float i;
                }
            }
            return;
        }'''
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_redeclare_block6(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            {
                int g;
                int h;
                {
                    int i;
                    float j;
                }
                string g;
            }
            return;
        }'''
        expect = "Redeclared Variable: g"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_redeclare_para1(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            {
                int g;
                int h;
                {
                    int i;
                    float j;
                }
            }
            boolean d;
            return;
        }'''
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_redeclare_if(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            if (a>0){
                int e;
                string c;
                float e;
            }
            return;
        }'''
        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_redeclare_if1(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            if (a>0){
                int e;
                string c;
                float a;
            }
            else{
                string m;
                float m;
            }
            return;
        }'''
        expect = "Redeclared Variable: m"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_redeclare_for(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            for(f=0;f<5;f=f+1){
                int f;
                float x;
                string x;
            }
            return;
        }'''
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_redeclare_dowhile(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            do
            {
                int a;
                float a;
            }
            a=1;
            while(false);
            return;
        }'''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_redeclare_dowhile1(self):
        input = '''
        int a;
        float b;
        void main(int c, int d){
            int e;
            int f;
            do
            {
                int e;
                float f;
            }
            {
                string c;
                boolean c;
            }
            a=9;
            while(true);
            return;
        }'''
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_redeclare_function1(self):
        input = '''
                   void main(){
                   }
                   int foo(){
                   return 1;
                   }
                   int foo(){
                   return 1;
                   }
              '''
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_redeclare_function22(self):
        input = '''
                   float foo(){
                        return 1;
                   }
                   void main(){
                   }
                   int foo(){
                        return 1;
                   }
              '''
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_redeclare_function3(self):
        input = '''
                   string str;
                   int main(){
                        return 0;
                   }
                   string str(){
                        return "";
                   }

              '''
        expect = "Redeclared Function: str"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_redeclare_function4(self):
        input = '''
                   int foo1;
                   void main(){
                   }
                   int foo(){
                   return 1;
                   }
                   int foo1(){
                   return 1;
                   }
              '''
        expect = "Redeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_redeclare_parameter1(self):
        input = '''
                   void main(){
                   }
                   int foo(int a, int a){
                        return 1;
                   }
              '''
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_redeclare_parameter2(self):
        input = '''
                   void main(){
                   }
                   int foo(string a, string a){
                        return 1;
                   }
              '''
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_redeclare_parameter3(self):
        input = '''
                   void main(){
                   }
                   void foo(float a, int a){
                        return ;
                   }
              '''
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 431))

    # 2.2 test Undeclared Identifier / Function:

    def test_undeclared_identifier1(self):
        input = """void main(){
               a = a + 1;
           }
           int b;
           """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_undeclared_identifier2(self):
        """ Undeclared Identifier """
        input = """
           int a;
           void main(){
               a = a + 1;
               a = a - b;
           }
           """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_undeclared_identifier3(self):
        """ Undeclared Identifier """
        input = """
           void main(){
               float a;
               int b;
               a = a + 1;
               a = a - b;
               a = a / c;
           }
           """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_undeclare_iden_bina(self):
        input = '''
           int a;
           void main(){
               int m;
               m=9;
               {
                   a=b+m;
               }
               return;
           }
           '''
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_undeclare_iden_una(self):
        input = '''
           int a;
           void main(){
               int m;
               {
                   a=-b;
               }
               return;
           }
           '''
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_undeclare_cell(self):
        input = '''
           int a[6];
           void main(){
               int m;
               {
                   a[c*2+1]=1;
               }
               return;
           }
           '''
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_undeclare_cell1(self):
        input = '''
           int a[6];
           void main(){
               int m;
               m=9;
               {
                   b[m*2+1]=1;
               }
               return;
           }
           '''
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_undeclare_if(self):
        input = '''
           int a[6];
           void main(){
               int m;
               m=-1;
               if(k<m){
                   m=6;
               }
               return;
           }
           '''
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_undeclare_if1(self):
        input = '''
           int a[6];
           void main(){
               int m;
               m=5;
               if(k<m){
                   m=6;
               }
               return;
           }
           '''
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_undeclare_for(self):
        input = '''
           int a[6];
           void main(){
               int m;
               m=9;
               for(x=0;m<6;m+1){
                   a[1]=m;
               }
               return;
           }
           '''
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_undeclare_for1(self):
        input = '''
           int a[6];
           void main(){
               int m;
               for(m=1;m<d;m+1){
                   a[1]=m;
               }
               return;
           }
           '''
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_undeclare_for2(self):
        input = '''
           int a[6];
           void main(){
               int m;
               for(m=1;m<10;m=m+t){
                   a[1]=m;
               }
               return;
           }
           '''
        expect = "Undeclared Identifier: t"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_undeclare_return(self):
        input = '''
           int a[6];
           int main(){
               int m;
               for(m=1;m<10;m=m+1){
                   a[1]=m;
               }
               g=1;
               return 1;
           }
           '''
        expect = "Undeclared Identifier: g"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_undeclare_do(self):
        input = '''
           int a[6];
           int main(){
               string m;
               do b=a[0]+1;
               m="7";
               while(a[3]==6);
               return 1;
           }
           '''
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_undeclare_do1(self):
        input = '''
           int a[6];
           int main(){
               string m;
               do a[1]=a[0]+1;
               m="7";
               while(x==6);
               return 1;
           }
           '''
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def testUndeclaredIdentifier4(self):
        """ Undeclared Function """
        input = """
           void main(){
               print("Hello");
           }
           """
        expect = "Undeclared Function: print"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def testUndeclaredFunction1(self):
        """ Undeclared Function """
        input = """
           void main(){
               int num;
               putInt(num);
               print(getInt());
           }
           """
        expect = "Undeclared Function: print"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def testUndeclaredFunction2(self):
        """ Undeclared Function """
        input = """
           int main(){
               int a;
               int b;
               a = sum(a, b);
               a = sub(a, b);
               return a;
           }
           int sum(int a, int b){
               return a + b;
           }
           """
        expect = "Undeclared Function: sub"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def testUndeclaredFunction3(self):
        """ Undeclared Function """
        input = """
           int main(){
               int a;
               int b;
               a = sub(a, b);
               return a;
           }
           """
        expect = "Undeclared Function: sub"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_undeclared_function_complex(self):
        """PrintVND Program """
        input = """
                void getch() {
                    return;
                }
                int main()
                {
                    int i, j, k;
                    for (i = 0; i <= 200; i = i + 1)
                       {
                            printf(i);
                       }
                    getch();
                    return 0;
                }
                """
        expect = "Undeclared Function: printf"
        self.assertTrue(TestChecker.test(input, expect, 451))

    # 2.3 Type Mismatch In Statement
    def test_type_mis_state_if(self):
        input = '''
           int a;
           int main(){
               string m;
               if(a){
                   a=6;
               }
               return 1;
           }
           '''
        expect = "Type Mismatch In Statement: If(Id(a),Block([BinaryOp(=,Id(a),IntLiteral(6))]))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_type_mis_state_return(self):
        input = '''
           boolean a;
           int main(){
               string m;
               if(a){
                   a=false;
               }
               return true;
           }
           '''
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_type_mis_state_return1(self):
        input = '''
           boolean a;
           int main(){
               string m;
               {
                   a=true;
                   return 1.6;
               }
           }
           '''
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.6))"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_type_mis_state_return2(self):
        input = '''
           boolean a;
           int b;
           int main(){
               string m;
               {
                   a=true;
                   for(b=0;b<1;b=b+1){
                       if(b>0) return 3;
                   }
                   do return "a";
                   while(true);
               }
           }
           '''
        expect = "Type Mismatch In Statement: Return(StringLiteral(a))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_type_mis_state_return_pointer(self):
        input = '''
           int b;
           int a[5];
           int[] main1(){
               return a;
           }
           int[] main(){
               string m;
               return main1();
           }
           '''
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_type_mis_state_return_pointer1(self):
        input = '''
           int b;
           int a[5];
           float[] main1(){
               return a;
           }
           float main(){
               main1();
               return 1;
           }
           '''
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_type_mis_state_return_pointer2(self):
        input = '''
           int b;
           int a;
           int[] main1(){
               return a;
           }
           int main(){
               main1();
               return 1;
           }
           '''
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_type_mis_state_return_pointer3(self):
        input = '''
           int b;
           boolean c[6];
           boolean[] a(){
               return c;
           }
           int[] main1(){
               return a();
           }
           void main(){
               main1();
               return;
           }
           '''
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(a),[]))"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_type_mis_state_return_void(self):
        input = '''
           int a;
           void main(){
               return 1;
           }
           '''
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 460))

    # 2.4 Type Mismatch In Expression:

    def test_equal_operator_in_first_expression_of_array_cell(self):
        """Equal operator in first expression of array cell """
        input = """
                   int a() {
                       int b[24];
                       (b[2] == 4)[2] = 4;
                       return 4;
                   }

                   float main(){
                       float b;
                       a();
                       return 2.4;
                   }
                   """
        expect = "Type Mismatch In Expression: ArrayCell(BinaryOp(==,ArrayCell(Id(b),IntLiteral(2)),IntLiteral(4)),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_assignment_operator_in_first_expression_of_array_cell(self):
        """Assignment operator in first expression of array cell"""
        input = """
                   float main(){
                       float b;
                       (b = 2)[34] = 1;
                       return 2.4;
                   }
                   """
        expect = "Type Mismatch In Expression: ArrayCell(BinaryOp(=,Id(b),IntLiteral(2)),IntLiteral(34))"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_assignment_operator_in_second_expression_of_array_cell(self):
        """Assignment operator in second expression of array cell"""
        input = """
                   int main(){
                       int ti[23];
                       float d;
                       int a, b;
                       int c;
                       c = a - b;
                       c = c + a;
                       if (c == 0)
                           a = ti[d = 2.3];
                       else 
                           c = 3;
                       return c;
                   }
                   """
        expect = "Type Mismatch In Expression: ArrayCell(Id(ti),BinaryOp(=,Id(d),FloatLiteral(2.3)))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_notequal_operator_in_second_expression_of_array_cell(self):
        """NotEqual operator in second expression of array cell"""
        input = """
                   int main(){
                       boolean a;
                       a = true;
                       if (true){
                           if (a == true){
                               if (!a){
                                   a = false;
                                   boolean b[24];
                                   b[2] = a;
                                   a = b[b[24] != false];
                               }
                               else{
                                   boolean b;
                                   b = a;
                               }
                           }
                           else{
                               a = false;
                           }
                       }
                       return 3;
                   }
                   """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),BinaryOp(!=,ArrayCell(Id(b),IntLiteral(24)),BooleanLiteral(false)))"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_not_operator_in_second_expression_of_array_cell(self):
        """Not operator in second expression of array cell """
        input = """
                   int a, b;
                   int main(){
                       for (a=1;a<10;a=a*2){
                           for(b=2;b==10;b=b*2){
                               int a[23];
                               boolean c;
                               int b;
                               b = a[!c];
                           }
                       }
                       return 1999;
                   }
                   """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),UnaryOp(!,Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_assignment_operator_in_binary_expression(self):
        """Assignment operator in binary expression """
        input = """
                   int a() {
                       int b[24];
                       b[2] = 4;
                       return 4;
                   }

                   float main(){
                       float b;
                       b = 2;
                       b = false;
                       return 2.4;
                   }
                   """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_or_operator_in_binary_expression(self):
        """Or operator in binary expression"""
        input = """
                   int a, b, c;
                   int main(){
                       if (a == 1)
                       {
                           a = a + 1;
                           b = 2;
                           if (true)
                               a = 1;
                           else
                               a = 2;
                       }
                       else
                           a = 4;
                       (true || false);
                       (a || b);
                       return 18;
                   }
                   """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_and_operator_in_binary_expression(self):
        """And operator in binary expression """
        input = """
                   int a, b;
                   int main(){
                       if (a == 1)
                           a = a + 1;
                       else
                           a = a + b;
                       (a == 2) && (b == 8);
                       (a && b);
                       return 12;
                   }
                   """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_equal_operator_in_binary_expression(self):
        """Equal operator in binary expression """
        input = """
                   int a;
                   int main(){
                       if (a == 1)
                       {
                           (2 == 3);
                           a == 2;
                           a = 2;
                       }
                       else
                       {
                          boolean b;
                          b == true;
                          float c;
                          c == 2.3;
                       }
                       return 12;
                   }
                   """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(c),FloatLiteral(2.3))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_notequal_operator_in_binary_expression(self):
        """NotEqual operator in binary expression"""
        input = """
                   void main(){
                       boolean a;
                       a = true;
                       if (true){
                           if (a == true){
                               if (!a){
                                   a = false;
                                   boolean b;
                                   b = a;
                               }
                               else{
                                   boolean b;
                                   b = a;
                               }
                           }
                           else{
                               a = false;
                               boolean c;
                               (a != c);
                               float d;
                               d != 2.3;
                           }
                       }
                       return;
                   }
                   """
        expect = "Type Mismatch In Expression: BinaryOp(!=,Id(d),FloatLiteral(2.3))"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_less_than_operator_in_binary_expression(self):
        """Less than operator in binary expression """
        input = """
                   int a;
                   float b;
                   string c;
                   boolean d;
                   int ti() { return 2;}
                   void main() {
                       a = 2;
                       b = 32;
                       c = "312414";
                       d = true;
                       ti();
                       (a < b);
                       (true < a);
                       return;
                   }
                   """
        expect = "Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(true),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_less_than_equal_operator_in_binary_expression(self):
        """Less than equal operator in binary expression"""
        input = """
                   int a; 
                   float b;
                   string c;
                   boolean d;
                   int a1(int foo) {
                       return 3214;
                   } 
                   boolean main() {
                       a1(2);
                       if (a <= b) {
                           a = 2;
                       }
                       else {
                           b = 3;
                       }
                       a <= false;   
                       return (false && true);
                   }
                   """
        expect = "Type Mismatch In Expression: BinaryOp(<=,Id(a),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_greater_than_operator_in_binary_expression(self):
        """Greater than operator in binary expression"""
        input = """
                   int a;
                   int main(){
                       for (a=1; a < 10; a=a+1){
                           if (a == 0){
                               int d;
                               int e;
                               d > e;
                               boolean t;
                               t = (d > false);
                           }
                       }
                       return 32;
                   }
                   """
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(d),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_greater_than_equal_operator_in_binary_expression(self):
        """Greater than equal operator in binary expression"""
        input = """
                   int i, j;
                   int main(){
                       for (i = 1; -i < 10; i = i + 1)
                       {
                           for (j = 1; j < 200; j = j + 1)
                           {
                               if (i == j)
                               {
                                   if (i == 0){
                                       int d;
                                       int e;
                                       d >= e;
                                       boolean t;
                                       t = (d >= "3213");
                                   }
                               }
                           }   
                       }
                       return 23;
                   }
                   """
        expect = "Type Mismatch In Expression: BinaryOp(>=,Id(d),StringLiteral(3213))"
        self.assertTrue(TestChecker.test(input, expect, 474))

    # 2.5 Function not return:
    def test_func_not_return1(self):
        """ Function Not Return """
        input = """
           int main(){
           }
           """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_func_not_return2(self):
        """ Function Not Return """
        input = """
           int main(){
               int a;
               int b;
               int c;
               a = 5;
               c = 1 + a + b;
               if (true)
                   return 0;
           }
           """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_func_not_return_in_ifstmt1(self):
        """ Function Not Return Inside If Statement """
        input = """
           int main(){
               if (true)
                   return 1;
               else{
                   int a;
                   a = a + 1;
               }
           }
           """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_not_return_simple_with_many_for_stmt_and_ifelse(self):
        input = '''
            void main(){f();return;}
            int f(){
                int a;
                a = 1;
                if (a == 1){
                    if (a == 2){
                        return 3;
                    }
                    else{
                        if (a == 4){return 3;}
                    }
                    return 3;
                }
                else{
                    for (a; a > 1; a = a + 1){
                        int b;
                        return 1;
                    }
                }
            }
        '''
        expect = "Function f Not Return "
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_function_return_in_block_stmt(self):
        """Function return in block statement """
        input = """
                int a;
                string d;
                int main(){
                    {
                        int a;
                        if (true) {
                            return 3;
                        }
                    }
                    {
                        int i;
                        float b;
                        for (i = 0; i < b; i = i + 1) {
                            if (true) i = 2;
                            return 4;
                        }
                    }
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_function_return_in_dowhile_stmt(self):
        """Function return in dowhile statement """
        input = """
                int a;
                string d;
                int main(){
                    do 
                        d = "T"; 
                        if (a + 2%4 == 2332) 
                            a = 1; 
                        do 
                            d = "T"; 
                            if (a + 2%4 == 2332) 
                                a = 1; 
                        while(a % 2 == 1);
                    while(a < 2);
                }
                """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 480))

    # 2.6 Break/Continue not in loop:
    def test_continue_loop1(self):
        input = '''
        int a(int b){
            if(b>0){
                b=1;
                continue;
            }
            do continue;
            while (false);
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_continue_loop2(self):
        input = '''
        int a(int b){
            if(b>0){
                b=1;
            }
            else continue;
            do continue;
            while (false);
            return 1;
        }
        void main(){
            a(1);
            return;
        }
        '''
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_break_in_ifelse(self):
        input = '''
            int main(){
                int a;
                a = 1;
                if (a == 1){break;}
                else{a;}
                return 1;
            }
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_break_simple(self):
        input = '''
            int main(){
                break;
                return 1;
            }
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_continue_in_ifelse(self):
        input = '''
            int main(){
                int a;
                a = 1;
                if (a == 1){continue;}
                else{a;}
                return 1;
            }
        '''
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_continue_simple(self):
        input = '''
            int main(){
                continue;
                return 1;
            }
        '''
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 486))

    # 2.7 No Entry Point:
    def test_no_entry(self):
        input = '''
           int a;
           int b;
           '''
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_no_entry1(self):
        input = '''
           int a;
           int b;
           int main;
           '''
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_no_entry2(self):
        input = '''
           int a;
           int b;
           int main;
           int c(){
               e();
               return 2;
           }
           int e(){
               c();
               return 1;
           }
           '''
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_no_entry_point_complex1(self):
        input = """
                int a;
                float main;
                void foo() {
                    hunG();
                    return;
                }
                int hunG(){
                    foo();
                    if (a == 1)
                    {
                        (2 == 3);
                        a == 2;
                        a = 2;
                    }
                    else
                    {
                       boolean b;
                       b == true;
                       float c;
                       c == 2.3;
                    }
                    return 12;
                }
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_no_entry_point_complex2(self):
        input = """
                int hunG1()
                {
                    int a;
                    int x;
                    a = x;
                    x = a;
                    a = 2;
                    int i;
                    for (i = 0; i < i + 1; i = i + 1) hunG1();
                    return 2;
                    kaki();
                }
                void kaki() {
                    int a;
                    int x;
                    int hunG;
                    hunG1();
                    for ( x = 1 ; x < 3 ; x = x + 1 ) {
                        a = a + 2 ;
                        {
                            float b;
                            b = 23.42;
                            hunG = 2;
                        }
                        break;
                    }
                    a = 2;
                    return;
                }
                """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_no_entry_with_main_id(self):
        input = '''
           bool main
           int a;
           int b;
           int main1;
           '''
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 492))

    # 2.8 Unreachable function:
    def test_unreach_func_with_mistake(self):
        input = '''
            int main(boolean a){
                return f();   
            }
            int foo(){
                return 1;
            }
            int f(){
                return f();
            }
        '''
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_redecl_array_and_var(self):
        input = '''
               int a;
               int main(int a, int b){
                   int c[5];
                   int c;
               }
           '''
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_unreach_func1(self):
        """ Unreachale Function """
        input = """
        void main(){}
        int add(int a, int b){
            return a + b;
        }
        """
        expect = "Unreachable Function: add"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_unreach_func2(self):
        """ Unreachale Function """
        input = """
        void main(){
            int a;
            int b;
            a = add(a, b);
        }
        int add(int a, int b){
            return a + b;
        }
        int sub(int a, int b){
            return a - b;
        }
        """
        expect = "Unreachable Function: sub"
        self.assertTrue(TestChecker.test(input, expect, 496))

    # 2.9 Not Left Value:
    def test_not_left_value1(self):
        """ Not Left Value With IntLiteral """
        input = """
        void main(){
            5 = 5;
        }
        """
        expect = "Not Left Value: IntLiteral(5)"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_not_left_value2(self):
        """ Not Left Value With CallExpr """
        input = """
        void main(){
            int a;
            int b;
            add(a, b) = 2;
        }
        int add(int a, int b){
            return a + b;
        }
        """
        expect = "Not Left Value: CallExpr(Id(add),[Id(a),Id(b)])"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_not_left_value_wrong(self):
        input = '''
               int main(boolean a){
                   int b, c,d;
                   b = 1;c = 1;d=1;
                   b + c = c + d;
                   return 1;
               }
           '''
        expect = "Not Left Value: BinaryOp(+,Id(b),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 499))
