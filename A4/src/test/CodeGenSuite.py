import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    ###############################
    #   TEST BUILT-IN FUNCTIONS   #
    ###############################
    '''
    def test_put_int(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 500))
        
    def test_put_int_ln(self):
    	input = """ void main() {putIntLn(10);}"""
    	expect = "10\n"
    	self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_put_float(self):
        input = """ void main() {putFloat(10.1);}"""
        expect = "10.1"
        self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    def test_put_float_ln(self):
        input = """ void main() {putFloatLn(10.1e30);}"""
        expect = "1.01E31\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_put_bool(self):
        input = """ void main() {putBool(true);}"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_put_bool_ln(self):
        input = """ void main() {putBoolLn(true);}"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_put_string(self):
        input = """ void main() {putString("a string");}"""
        expect = "a string"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_put_string_ln(self):
        input = """ void main() {putStringLn("a string");}"""
        expect = "a string\n"
        self.assertTrue(TestCodeGen.test(input, expect, 507))
    '''
    ###############################
    #   TEST PRIMITIVE TYPES      #
    ###############################
    '''
    def test_int(self):
        input = """ void main() {
                        putInt(1000000000);
                    }"""
        expect = "1000000000"
        self.assertTrue(TestCodeGen.test(input, expect, 508))
    
    def test_float_simple(self):
        input = """ void main() {
                        putFloat(1.00001);
                    }"""
        expect = "1.00001"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_float_rounded(self):
        input = """ void main() {
                        putFloat(1.899999999);
                    }"""
        expect = "1.9"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_bool_simple(self):
        input = """ void main() {
                        putBool(false);
                    }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 511))
    
    def test_bool_complex(self):
        input = """ void main() {
                        putBool(false);
                    }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_string_simple(self):
        input = """ void main() {
                        putString("Print this 123456");
                    }"""
        expect = "Print this 123456"
        self.assertTrue(TestCodeGen.test(input, expect, 513))
    
    # def test_int_expr(self):
    #     input = """ void main() {
    #                     putInt(1 + 2 - 3/4 + -3 + 3%2);
    #                 }"""
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_int_expr_add(self):
        input = """ void main() {
                        putInt(1 + 2 + 3 + 4);
                    }"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_int_expr_sub(self):
        input = """ void main() {
                        putInt(1 - 2 + 3 - 4);
                    }"""
        expect = "-2"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_int_expr_mul(self):
        input = """ void main() {
                        putInt(3*-4);
                    }"""
        expect = "-12"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_int_expr_div(self):
        input = """ void main() {
                        putInt(20/5/2);
                    }"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_int_expr_mod(self):
        input = """ void main() {
                        putInt(5%2);
                    }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_float_expr_add(self):
        input = """ void main() {
                        putFloat(1.25 + 2.75);
                    }"""
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_float_expr_sub(self):
        input = """ void main() {
                        putFloat(2.75 - 1.25);
                    }"""
        expect = "1.5"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_float_expr_mul(self):
        input = """ void main() {
                        putFloat(1.0275 * 3.25);
                    }"""
        expect = "3.339375"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_float_expr_div(self):
        input = """ void main() {
                        putFloat(3.0/3);
                    }"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 522))
    
    def test_bool_expr_and(self):
        input = """ void main() {
                        putBool(true && false && true);
                    }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_bool_expr_or(self):
        input = """ void main() {
                        putBool(true || false || true);
                    }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_bool_expr_both(self):
        input = """ void main() {
                        putBool(true || false && true);
                    }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_bool_expr_eq(self):
        input = """ void main() {
                        putBool(3 == 2 + 4 - 5 + 1*2);
                    }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_bool_expr_neq(self):
        input = """ void main() {
                        putBool(true != (false || true));
                    }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_bool_expr_gt(self):
        input = """ void main() {
                        putBool(3.2 > 3.15);
                    }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 528))
    
    def test_bool_expr_gte(self):
        input = """ void main() {
                        putBool(3.1 >= 3);
                    }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_bool_expr_lt(self):
        input = """ void main() {
                        putBool(3.0001 < 3);
                    }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_bool_expr_lte(self):
        input = """ void main() {
                        putBool(3 + 0.0001 <= 3.01);
                    }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 531))
    
    def test_primitive_equation(self):
        input = """ void main() {
                        putIntLn(11 + 22 + 33 / 4);
                        putFloatLn(1.25 + 3.75);
                        putStringLn("Print this one");
                        putBool(false);
                    }"""
        expect = "41\n5.0\nPrint this one\nfalse"
        self.assertTrue(TestCodeGen.test(input, expect, 532))
    
    def test_expr_stmt_1(self):
        input = """ void main() {
                        int a;
                        float b;
                        a = 1;
                        putIntLn(a);
                        b = a + 1.1;
                        putFloat(b);
                    }"""
        expect = "1\n2.1"
        self.assertTrue(TestCodeGen.test(input, expect, 533))
    
    def test_expr_stmt_2(self):
        input = """ void main() {
                        int a;
                        float b;
                        string c;
                        boolean d;
                        a = 10;
                        b = a + 0.25;
                        c = "a string";
                        d = a > b;
                        putBoolLn(d);
                        putString(c);
                    }"""
        expect = "false\na string"
        self.assertTrue(TestCodeGen.test(input, expect, 534))
    

    ###############################
    #   TEST STATEMENTS           #
    ###############################

    def test_if_stmt_1(self):
        input = """ void main() {
                        if (true)
                            putString("In cai nay");
                        else
                            putString("Dung in cai nay nha");
                    }"""
        expect = "In cai nay"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_if_stmt_2(self):
        input = """ void main() {
                        if (false)
                            putString("Dung in cai nay nha");
                    }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_if_stmt_3(self):
        input = """ void main() {
                        if (10 > 2 && true != false)
                            putString("Print this");
                        putString("This one!");
                    }"""
        expect = "Print thisThis one!"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_if_stmt_4(self):
        input = """ void main() {
                        if (10 > 2 && true != false && true)
                            putString("Print this");
                        if (10 == 11) 
                            putString("Not this one");
                        else
                            putString("Last one");
                    }"""
        expect = "Print thisLast one"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_if_stmt_5(self):
        input = """ void main() {
                        if (true) 
                            putInt(100);
                        else if (true)
                            putInt(101);
                        else
                            putInt(102);
                    }"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 539))
    
    def test_for_stmt_1(self):
        input = """ void main() {
                        int i;
                        for (i=1; i<3; i = i+1)
                            putInt(i);
                    }"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_for_stmt_2(self):
        input = """ void main() {
                        int i;
                        for (i=1; i<0; i = i+1)
                            putInt(i);
                    }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 541))
    
    def test_for_stmt_3(self):
        input = """ void main() {
                        int i;
                        for (i=1; i<10; i = i+1){
                            if (i%2 == 0)
                                putInt(i); 
                        }
                    }"""
        expect = "2468"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_for_stmt_4(self):
        input = """ void main() {
                        int i, j;
                        for (i=1; i<3; i = i+1){
                            for (j=1; j<3; j=j+1){
                                putInt(i);
                                putIntLn(j);
                            }
                        }
                    }"""
        expect = "11\n12\n21\n22\n"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_for_stmt_5(self):
        input = """ void main() {
                        int i;
                        for (i=1; i!=4; i = i*2){
                            putInt(i);
                        }
                    }"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 544))
    
    def test_dowhile_stmt_1(self):
        input = """ void main() {
                        int a;
                        a = 1;
                        do{
                            putInt(1);
                            a = a+1;
                        } while a != 3;
                    }"""
        expect = "11"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_dowhile_stmt_2(self):
        input = """ void main() {
                        int a;
                        do{
                            putInt(1);
                        } while false;
                    }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_dowhile_stmt_3(self):
        input = """ void main() {
                        int a;
                        a = 10;
                        do{
                            putInt(a);
                            a = a-1;
                        } while a>0;
                    }"""
        expect = "10987654321"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_dowhile_stmt_4(self):
        input = """ void main() {
                        int a;
                        do{
                            putInt(1);
                        } while false;
                    }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 548))
    
    def test_func_void_1(self):
        input = """ void foo(){
                        putInt(1);
                    }
                    void main(){
                        foo();
                    }
                    """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_func_void_2(self):
        input = """ void foo(){
                        putString("haha");
                        return;
                    }
                    void main(){
                        foo();
                        foo();
                    }
                    """
        expect = "hahahaha"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_func_string_1(self):
        input = """ string foo(){
                        return "string";
                    }
                    void main(){
                        putString(foo());
                    }
                    """
        expect = "string"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_func_string_2(self):
        input = """ void foo(string a){
                        putString(a);
                    }
                    void main(){
                        foo("baa");
                    }
                    """
        expect = "baa"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_func_string_3(self):
        input = """ string foo(string a){
                        return a;
                    }
                    void main(){
                        putString(foo("baa"));
                    }
                    """
        expect = "baa"
        self.assertTrue(TestCodeGen.test(input, expect, 553))
    
    def test_func_int_1(self):
        input = """ int foo(){
                        return 5;
                    }
                    void main(){
                        putInt(foo());
                    }
                    """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_func_int_2(self):
        input = """ void foo(int a){
                        putInt(a);
                    }
                    void main(){
                        foo(1);
                    }
                    """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_func_float_1(self):
        input = """ float foo(){
                        return 1.0;
                    }
                    void main(){
                        if (foo() == 1)
                            putInt(1);
                    }
                    """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_func_float_2(self):
        input = """ void foo(float a){
                        putFloat(a);
                    }
                    void main(){
                        foo(1);
                    }
                    """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 557))
    
    def test_break_for_1(self):
        input = """ void main(){
                        int a;
                        for (a=1; a<10; a=a+1){
                            if (a%5 == 0)
                                break;
                            putInt(a);
                        }
                    }
                    """
        expect = "1234"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_break_for_2(self):
        input = """ void main(){
                        int a;
                        for (a=1; a<10; a=a+1){
                            break;
                        }
                    }
                    """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_break_dowhile_1(self):
        input = """ void main(){
                        int a;
                        do 
                            break;
                        while true;
                    }
                    """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_break_dowhile_2(self):
        input = """ void main(){
                        int a;
                        a = 10;
                        do 
                            if (a==1)
                                break;
                            putInt(a);
                            a = a-1;
                        while a>0;
                    }
                    """
        expect = "1098765432"
        self.assertTrue(TestCodeGen.test(input, expect, 561))
    
    def test_continue_for_1(self):
        input = """ void main(){
                        int a;
                        for (a=1; a<10; a=a+1){
                            if (a==4)
                                continue;
                            putInt(a);
                        }
                    }
                    """
        expect = "12356789"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_continue_for_2(self):
        input = """ void main(){
                        int a;
                        for (a=1; a<10; a=a+1){
                            if (a==4 || a==6)
                                continue;
                            putInt(a);
                        }
                    }
                    """
        expect = "1235789"
        self.assertTrue(TestCodeGen.test(input, expect, 563))    
    
    def test_continue_dowhile_1(self):
        input = """ void main(){
                        int a;
                        a = 1;
                        do 
                            a = a + 1;
                            if (a==5)
                                continue;
                            putInt(a);
                        while a<10;
                    }
                    """
        expect = "234678910"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_continue_dowhile_2(self):
        input = """ void main(){
                        int a;
                        a = 1;
                        do 
                            if (a==5)
                                continue;
                            putInt(a);
                            a = a + 1;
                        while a!=4;
                    }
                    """
        expect = "123"
        self.assertTrue(TestCodeGen.test(input, expect, 565))
    
    def test_global_1(self):
        input = """ float a, b;
                    void main(){
                        a = 1;
                        putFloat(a);
                        b = a + 1;
                        putFloat(b);
                    }
                    """
        expect = "1.02.0"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_global_2(self):
        input = """ float a, b;
                    boolean c;
                    void main(){
                        a = 1;
                        putFloat(a);
                        b = a + 1;
                        putFloat(b);
                        c = true;
                        putBool(c);
                    }
                    """
        expect = "1.02.0true"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_arr_global(self):
        input = """ int a[10];
                    void main(){
                        a[0] = a[1] = 1;
                        putInt(a[0] + a[1]);
                    }
                    """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_arr_local(self):
        input = """ 
                    void main(){
                        int a[10];
                        a[0] = a[1] = 1;
                        putInt(a[0] + a[1]);
                    }
                    """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_arr_cell(self):
        input = """ int foo(){return 1;}
                    void main(){
                        int a[10];
                        a[0] = a[1] = 1;
                        putInt(a[0] + a[1] + a[foo()]);
                    }
                    """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 570))
    
    def test_fibonacci(self):
        input = """ void main()    
                    {    
                        int n1,n2,n3,i,number;    
                        n1 = 0;
                        n2 = 1;
                        number = 10;   
                        putInt(n1);
                        putInt(n2);    
                        for(i=3;i<number;i = i+1)    
                        {    
                            n3=n1+n2;    
                            putIntLn(n3);    
                            n1=n2;    
                            n2=n3;    
                        }  
                    }
                    """
        expect = "011\n2\n3\n5\n8\n13\n21\n"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_prime_number(self):
        input = """ void main(){    
                        int n, i, m, flag; 
                        m = 0;   
                        flag = 0;
                        n = 44;   
                        m = n/2;    
                        for(i=2;i<=m;i=i+1)    
                        {    
                            if(n%i==0)    
                            {    
                                putString("44 is not prime");    
                                flag=1;    
                                break;    
                            }    
                        }    
                        if(flag==0)    
                        putString("Number is prime");     
                    }    
                    """
        expect = "44 is not prime"
        self.assertTrue(TestCodeGen.test(input, expect, 572))
    
    def test_prime_number(self):
        input = """ void main()    
                    {    
                        int n,r,sum,temp;    
                        sum = 0;
                        n = 12321;    
                        temp=n;    
                        do  
                        {    
                            r=n%10;    
                            sum=(sum*10)+r;    
                            n=n/10;    
                        } while n>0; 
                        if(temp==sum)    
                            putString("palindrome number");    
                        else    
                            putString("not palindrome");   
                    }   
                    """
        expect = "palindrome number"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_factorial(self):
        input = """ void main()    
                    {    
                        int i,fact,number;    
                        fact=1;
                        number = 5;   
                        for(i=1;i<=number;i=i+1){    
                            fact=fact*i;    
                        }    
                        putString("Factorial is: ");    
                        putInt(fact);
                    }   
                    """
        expect = "Factorial is: 120"
        self.assertTrue(TestCodeGen.test(input, expect, 574))
    
    def test_amstrong_number(self):
        input = """ void main()    
                    {    
                        int n,r,sum,temp;  
                        sum = 0;  
                        n = 153;  
                        temp=n;    
                        do
                        {    
                            r=n%10;    
                            sum=sum+(r*r*r);    
                            n=n/10;    
                        } while(n>0) ; 
                        if(temp==sum)    
                            putString("armstrong number");    
                        else    
                            putString("not armstrong number");    
                    }   
                    """
        expect = "armstrong number"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_sum_of_digits(self):
        input = """ void main()    
                    {    
                        int n,sum,m;
                        sum = 0;    
                        n = 654;    
                        do
                        {    
                            m=n%10;    
                            sum=sum+m;    
                            n=n/10;    
                        } while(n>0);   
                        putInt(sum);    
                    }    
                    """
        expect = "15"
        self.assertTrue(TestCodeGen.test(input, expect, 576))
    
    def test_reverse_number(self):
        input = """ void main()    
                    {    
                        int n, reverse, rem;    
                        reverse = 0;
                        n = 123;  
                        do
                        {    
                            rem=n%10;    
                            reverse=reverse*10+rem;    
                            n= n/10;    
                        } while(n!=0);
                        putInt(reverse);    
                    }       
                    """
        expect = "321"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_swap_no_temp(self):
        input = """ void main()    
                    {    
                        int a, b;  
                        a = 10;
                        b = 20;    
                        putIntLn(a);
                        putIntLn(b);   
                        a=a+b;  
                        b=a-b;    
                        a=a-b;   
                        putStringLn("After:"); 
                        putIntLn(a);
                        putIntLn(b); 
                    }   
                    """
        expect = "10\n20\nAfter:\n20\n10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 578))
    
    def test_check_odd_even(self):
        input = """ void main() {
                        int num;
                        num = 101;
                        if(num % 2 == 0)
                            putString("even");
                        else
                            putString("odd");
                    }
                    """
        expect = "odd"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_check_leap_year(self):
        input = """ void main() {
                        int year;
                        year = 2019;
                        if (year % 4 == 0) {
                            if (year % 100 == 0) {
                                // the year is a leap year if it is divisible by 400.
                                if (year % 400 == 0)
                                    putString("leap year");
                                else
                                    putString("not a leap year");
                            } else
                                putString("leap year");
                        } else
                            putString("not a leap year");
                    }
                    """
        expect = "not a leap year"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_mul_table(self):
        input = """ void main() {
                        int n, i;
                        n = 1;
                        for (i = 1; i <= 10; i = i+1) {
                            putInt(n);
                            putString(" * ");
                            putInt(i);
                            putString(" = ");
                            putIntLn(n*i);
                        }
                    }
                    """
        expect = "1 * 1 = 1\n1 * 2 = 2\n1 * 3 = 3\n1 * 4 = 4\n1 * 5 = 5\n1 * 6 = 6\n1 * 7 = 7\n1 * 8 = 8\n1 * 9 = 9\n1 * 10 = 10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_find_gcd(self):
        input = """ void main()
                    {
                        int n1, n2, i, gcd;
                        n1 = 81;
                        n2 = 153;
                        gcd = 1;
                        for(i=2; i <= n1 && i <= n2; i=i+1)
                        {
                            if(n1%i==0 && n2%i==0)
                                gcd = i;
                        }
                        putInt(gcd);
                    }
                    """
        expect = "9"
        self.assertTrue(TestCodeGen.test(input, expect, 582))
    
    def test_get_power(self):
        input = """ int pow(int base, int exp){
                        int result;
                        result = 1;
                        do {
                            result = result * base;
                            exp = exp - 1;
                        } while (exp != 0);
                        return result;
                    }
                    void main() {
                        putInt(pow(2,4));
                    }
                    """
        expect = "16"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_get_average(self):
        input = """ void main() {
                        int n, i;
                        int num[50], sum;
                        float avg;
                        sum = 0;
                        n = 50;
                        avg = 0.0;
                        for (i=0; i<n; i=i+1){
                            num[i] = i;
                        }
                        for (i = 0; i < n; i = i+1) {
                            sum = sum + num[i];
                        }
                        avg = sum / n;
                        putFloat(avg);
                    }
                    """
        expect = "24.0"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_get_quo_remain(self):
        input = """ void main() {
                        int dividend, divisor, quotient, remainder;
                        dividend = 25;
                        divisor = 4;
                        // Computes quotient
                        quotient = dividend / divisor;
                        // Computes remainder
                        remainder = dividend % divisor;
                        putIntLn(quotient);
                        putInt(remainder);
                    }
                    """
        expect = "6\n1"
        self.assertTrue(TestCodeGen.test(input, expect, 585))
    
    def test_get_biggest(self):
        input = """ void main() {
                        float n1, n2, n3;
                        n1 = 1.1;
                        n2 = 10.56;
                        n3 = 100.01;
                        if (n1 >= n2 && n1 >= n3)
                            putString("n1 is largest");
                        if (n2 >= n1 && n2 >= n3)
                            putString("n2 is largest");
                        if (n3 >= n1 && n3 >= n2)
                            putString("n3 is largest");
                    }
                    """
        expect = "n3 is largest"
        self.assertTrue(TestCodeGen.test(input, expect, 586))
    
    def test_get_sum(self):
        input = """ void main() {
                        int n, i, sum;
                        sum = 0;
                        n = 10;
                        for (i = 1; i <= n; i=i+1) {
                            sum = sum + i;
                        }
                        putInt(sum);
                    }
                    """
        expect = "55"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_get_LCD(self):
        input = """ void main() {
                        int n1, n2, min;
                        n1 = 72;
                        n2 = 120;
                        if (n1>n2)
                            min = n1;
                        else
                            min = n2;
                        do {
                            if (min % n1 == 0 && min % n2 == 0) {
                                putInt(min);
                                break;
                            }
                            min = min + 1;
                        } while true;
                    }

                    """
        expect = "360"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_get_prime_numbers(self):
        input = """ void main() {
                        int low, high, i, flag;
                        flag = 0;
                        low = 20;
                        high = 50;
                        do {
                            flag = 0;
                            for (i = 2; i <= low / 2; i = i+1) {
                                if (low % i == 0) {
                                    flag = 1;
                                    break;
                                }
                            }
                            if (flag == 0){
                                putInt(low);
                            }
                            low = low+1;
                        } while(low<high);
                    }
                    """
        expect = "23293137414347"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_get_prime_numbers_function(self):
        input = """ void main() {
                        int low, high, i, flag;
                        flag = 0;
                        low = 20;
                        high = 50;
                        do {
                            flag = 0;
                            for (i = 2; i <= low / 2; i = i+1) {
                                if (low % i == 0) {
                                    flag = 1;
                                    break;
                                }
                            }
                            if (flag == 0){
                                putInt(low);
                            }
                            low = low+1;
                        } while(low<high);
                    }
                    """
        expect = "23293137414347"
        self.assertTrue(TestCodeGen.test(input, expect, 589))
    
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
        self.assertTrue(TestCodeGen.test(input,expect,590))

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
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test_array_use_1(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,592))
    
    def test_array_use_2(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,593))

    def test_array_use_3(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,594))

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
        self.assertTrue(TestCodeGen.test(input,expect,594))

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
        self.assertTrue(TestCodeGen.test(input,expect,596))

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
        self.assertTrue(TestCodeGen.test(input,expect,597))
    
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
        self.assertTrue(TestCodeGen.test(input,expect,598))
        
    def test_check_neg_pos(self):
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
        self.assertTrue(TestCodeGen.test(input,expect,599))
    '''

    def test_dowhile_stmt_1(self):
        input = """ void main() {
                        int a;
                        a = 1;
                        do{
                          //  putInt(1);
                            a = a+1;
                            return;
                        } while a != 3;
                        putInt(a);
                    }"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 545))
