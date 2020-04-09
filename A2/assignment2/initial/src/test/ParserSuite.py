import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_simple_program(self):
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        i = """int main( {}"""
        e = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(i, e, 203))
    
    def test_variable_declaration1(self):
        i = """ int main() {
            int i, j, k;
            string s;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 204))
    
    def test_variable_declaration2(self):
        i = """ boolean flag;
                int main(){}
            """
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 205))
    
    def test_variable_declaration3(self):
        i = """ float y;
                int main(){}
                void func(){}
                string z[2];
            """
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 206))
    
    def test_variable_declaration4(self):
        i = """ string s;
                int main(){
                    int x, a[1];
                }
            """
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 207))
    
    def test_variable_declaration5(self):
        i = """ int foo(){}
                int main(){
                    string x = y;
                }
            """
        e = "Error on line 3 col 29: ="
        self.assertTrue(TestParser.checkParser(i, e, 208))
    
    def test_function_declaration1(self):
        i = """ int foo(int a, int b, string c){}"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 209))

    def test_function_declaration2(self):
        i = """ int foo(string a, int b[]){
                    string str;
                }
            """
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 210))

    def test_function_declaration3(self):
        i = """int foo (boolean b, 30){}"""
        e = "Error on line 1 col 20: 30"
        self.assertTrue(TestParser.checkParser(i, e, 211))
    
    def test_function_declaration4(self):
        i = """int foo(int x, y){}"""
        e = "Error on line 1 col 15: y"
        self.assertTrue(TestParser.checkParser(i, e, 212))

    def test_function_declaration5(self):
        i = """string foo(int a[10]){}"""
        e = "Error on line 1 col 17: 10"
        self.assertTrue(TestParser.checkParser(i, e, 213))
    
    def test_function_declaration6(self):
        i = """boolean foo()"""
        e = "Error on line 1 col 13: <EOF>"
        self.assertTrue(TestParser.checkParser(i, e, 214))

    def test_assign_statement1(self):
        i = """ int main(){
                    int y;
                    y = 100;
                }
            """
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 215))
    
    def test_assign_statement2(self):
        i = """int main(){
                    s = "this is a string";
                    f = 1.2;
                    a = b = d[10] = 100;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 216))
    
    def test_assign_statement3(self):
        i = """int foo(int a[], int b){
                    s[10] = 1.e-10 = b;
            }"""
        e = "Error on line 2 col 35: ="
        self.assertTrue(TestParser.checkParser(i, e, 217))

    def test_assign_statement4(self):
        i = """int main(){
                    a = func(b,c);
                    b = func(a)[100];
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 218))
    
    def test_assign_statement5(self):
        i = """int main(){
                    a = func(func(b)[100]);
                    a[10] = b[10] = 1.1e10;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 219))

    def test_assign_statement6(self):
        i = """int main(){
                    a = b = func(10);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 220))

    def test_if_statement1(self):
        i = """int main(){
                    if (true)
                    {a = 10;}
                    else
                    a = a + 1;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 221))

    def test_if_statement2(self):
        i = """int main(){
                    if (a=10) a = 10;
                    else {a = 0; b = 10;}
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 222))

    def test_if_statement3(self):
        i = """int main(){
                    if (a>=b)
                        a = 100;
                    b = a;
                }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 223))

    def test_if_statement4(self):
        i = """int main(){
                    if (a>=b)
                        a = 100;
                        b = a;
                    else
                        a = 10;
                }"""
        e = "Error on line 5 col 20: else"
        self.assertTrue(TestParser.checkParser(i, e, 224))
    
    def test_if_statement5(self):
        i = """int main(){
                    if (a != true)
                        a = false;
                    else {
                        a = 10;
                        b = 100;
                    }
                }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 225))

    def test_if_statement6(self):
        i = """int main(){
                    if (a == 10)
                        a = false;
                    else if (a == 11)
                        a = 10;
                    else
                        b = 100;
                }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 226))

    def test_if_statement7(self):
        i = """int main(){
                    if (a<10)
                        print("This is a test case");
                    // this is a comment
                }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 227))

    def test_function_declaration7(self):
        i = """ int foo(int a, int c[]){
                    int foo2(int b){}
                }"""
        e = "Error on line 2 col 28: ("
        self.assertTrue(TestParser.checkParser(i, e, 228))
    
    def test_function_declaration8(self):
        i = """ int foo(int a, int c[]){
                    void a;
                    int b;
                }"""
        e = "Error on line 2 col 20: void"
        self.assertTrue(TestParser.checkParser(i, e, 229))
    
    def test_if_statement8(self):
        i = """int main() {
                    if (a+b>c+d-e*3){
                        a = 10;
                    }
                    else
                        a = 100;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 230))
    
    def test_if_statement9(self):
        i = """int main(){
                    if (foo(3) == foo (4) && foo(5) != foo(6)){
                        print("it's true");
                    }
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 231))

    def test_if_statement10(self):
        i = """int main(){
                    if(foo()) {
                        a = 10;
                    }
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 232))

    def test_if_statement11(self):
        i = """int main(){
                    a = true;
                    if (a){
                        a == false;
                    }
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 233))

    def test_assign_statement7(self):
        i = """int main(){
                    x = ((x + 2) / 3) * (1 + 4/x[2+3] - 1 + 2);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 234))

    def test_do_while_statement1(self):
        i = """int main(){
                    do 
                        y = 10;
                    while (true);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 235))
    
    def test_do_while_statement2(self):
        i = """int main(){
                    do {}
                    while (true);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 236))

    def test_do_while_statement3(self):
        i = """int main(){
                    do {}{}
                    while true ;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 237))

    def test_do_while_statement4(self):
        i = """int main() {
                    do {y = 10;}{}{string x;}
                    while(true);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 238))

    def test_do_while_statement5(self):
        i = """int main(){
                    do
                    while(true);
            }"""
        e = "Error on line 3 col 20: while"
        self.assertTrue(TestParser.checkParser(i, e, 239))
    
    def test_do_while_statement6(self):
        i = """int main(){
                    do y = 10;
                    while(a > 0);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 240))

    def test_do_while_statement7(self):
        i = """int main(){
                    do y = 10;
                    while (a=10);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 241))

    def test_do_while_statement8(self):
        i = """int main(){
                    do y = true;
                    while (a*2 == 3 && c == d || g != h);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 242))

    def test_for_statement1(self):
        i = """int main(){
                for(a; a<10; a=a+1){
                    print("testing");
                }
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 243))

    def test_for_statement2(self):
        i = """int main(){
                    for (a=10; a<100; a=a+1){
                        print("testing");
                    }
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 244))

    def test_for_statement3(self):
        i = """int main(){
                    for(a; a!=100; a = a*a){
                        print("testing");
                    }
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 245))

    def test_for_statement4(self):
        i = """int main(){
                    for(a;a==100;){
                        a = a+1;
                    }
            }"""
        e = "Error on line 2 col 33: )"
        self.assertTrue(TestParser.checkParser(i, e, 246))

    def test_for_statement5(self):
        i = """int main(){
                    for(a; a==100; a=a+1){}
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 247))

    def test_for_statement6(self):
        i = """int main(){
                for(a; a==100; a=a+1)
            }"""
        e = "Error on line 3 col 12: }"
        self.assertTrue(TestParser.checkParser(i, e, 248))
    def test_break_statement(self):
        i = """int main(){
                    do break;
                    while true;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 249))
    def test_continue_statement(self):
        i = """int main(){
                    do continue;
                    while true;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 250))

    def test_return_statement(self):
        i = """int main(){
                    return;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 251))

    def test_block_statement(self):
        i = """int main(){ """
        e = "Error on line 1 col 12: <EOF>"
        self.assertTrue(TestParser.checkParser(i, e, 252))

    def test_func_call1(self):
        i = """int main(){
                    foo(a+1>b+c*3/2/3/d[c+d]);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 253))

    def test_func_call2(self):
        i = """int main(){
                    if(foo(3)>foo(2)+10){}
                    else {foo(3)[a+b[foo(c)]];}
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 254))
    
    def test_func_call3(self):
        i = """int main(){
                    foo(3,a+b,c+d,4);
                    foo();
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 255))
    
    def test_func_call4(self):
        i = """int main(){
                    foo(3, foo(4, foo(5, foo(6, foo1(7)))));
                    return 3;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 256))

    def test_func_call5(self):
        i = """int main(){
                    return foo(a,b,c,4,5,6);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 257))

    def test_func_call6(self):
        i = """int main(){
                    print("a string");
                    foo(str);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 258))
    
    def test_func_call7(self):
        i = """int main(){
                    a[foo()]==10;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 259))

    def test_bulk1(self):
        i = """ int a, b, c[10];
                int foo(float a, float b){
                    return a+b;
                }
                int main(){
                    foo(3,5);
                }
            """
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 260))

    def test_bulk2(self):
        i = """ void foo1(){
                    if (a==b)
                        b = c;
                    if (e!=f)
                        foo(a,b);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 261))

    def test_bulk3(self):
        i = """ void foo1(){
                    if (a==b)
                        b = c;
                    else 
                        foo(a,b);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 262))

    def test_bulk4(self):
        i = """ int main(){
                    if (a==b) {
                        if (c==d){
                            do {} while true ;
                        }
                    }
                    else c=1;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 263))

    def test_bulk5(self):
        i = """ int a;
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
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 264))

    def test_bulk6(self):
        i = """ string hello(int a, int b){
                    c = a+b;
                    putString("Hello World");
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 265))

    def test_bulk7(self):
        i = """ int a, b;
                int sum(int a, int b) {return a+b;}
                int main(){
                    putString("Enter a num: ");
                    getInt(a);
                    putString("Enter a num: ");
                    getInt(b);
                    putString("The sum of them is: ");
                    putInt(sum(a, b));
                }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 266))

    def test_bulk8(self):
        i = """ string first, last;
                int main(){
                    first = "Edison";
                    last = "Thomas";
                    putString("Full name is: ");
                    putString(first);
                    putString(last);
                }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 267))

    def test_bulk9(self):
        i = """ int main(){
                    a = a + b + c + 10 - 12 / 13 / 14.1 / 15.2 * 3 / 2 + foo()[foo()];
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 268))

    def test_bulk10(self):
        i = """ int main(){
                    a[b[19]] = 19;
                    a = foo(3);
                    b = a;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 269))
    
    def test_bulk11(self):
        i = """ int main(){
                    if (a==b)
                        if (c==d)
                            e = f;
                        else i = 1;
                    else x = 2;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 270))
    
    def test_bulk12(self):
        i = """ int main(){
                    int a[m];
        }"""
        e = "Error on line 2 col 26: m"
        self.assertTrue(TestParser.checkParser(i, e, 271))
        
    def test_bulk13(self):
        i = """ int main(){
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
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 272))

    def test_bulk14(self):
        i = """ int sum(int a[], int m){
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
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 273))
    
    def test_bulk15(self):
        i = """ int main(){
                    int a[10], sum, i;
                    sum = 0;
                    for (i=0; i<10; i=i+1)
                        sum = sum + a[i];
                    return sum;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 274))

    def test_bulk16(self):
        i = """ int foo(int a[], int n){
                    int sum, i;
                    s = 0;
                    for (i = 0; i<5; i=i+1){
                        if (a[i] % 2 == 0)
                            sum = sum + a[i];
                    }
                    return sum;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 275))

    def test_bulk17(self):
        i = """ int foo(int n){
                    int i;
                    for(i=2; i<n-1; i=i+1){
                        if (n % i == 0)
                            return 0;
                        else
                            return 1;
                    }
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 276))

    def test_bulk18(self):
        i = """ boolean foo(int a[], int n, int k){
                    boolean flag;
                    int i;
                    for (i=1; i<n; i=i+1){
                        if (a[i] != a[i-1]+k){
                            flag = false;
                            return flag;
                            // stop checking
                        }
                    }
                    return flag;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 277))

    def test_bulk19(self):
        i = """int foo(int x) {
                    int f1, f2;
                    if (x<=2)
                        return 1;
                    else
                        return foo(x-2) + foo(x-1);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 278))

    def test_bulk20(self):
        i = """boolean foo(int i){
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
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 279))

    def test_bulk21(self):
        i = """float foo(float a, float b, float c){
                    if ((a+b)>c && (b+c)>a && (a+c)>b){
                        p = (a+b+c)/2;
                        s = sqrt(p*(p-a)*(p-b)*(p-c));
                        /*
                        abc la 3 canh cua tam giac
                        */
                        return p;
                    } 
                    else return 0; //abc thang hang
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 280))

    def test_bulk22(self):
        i = """ int i;
                ()"""
        e = "Error on line 2 col 16: ("
        self.assertTrue(TestParser.checkParser(i, e, 281))

    def test_bulk23(self):
        i = """string foo(){
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
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 282))

    def test_bulk24(self):
        i = """int main(){
                    do{}
                    while a==4 && b==6-8-9-5;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 283))

    def test_bulk25(self):
        i = """int main(){
                    a[1] = 1;
                    a[2] = 2+a[1][1]+c+a;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 284))

    def test_array_pointer1(self):
        i = """ int[] foo(int a[], int b){
                    int c[3];
                    return c;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 285))

    def test_bulk26(self):
        i = """void main( ){ 
                    if (a) 
                        if (b) 
                            if (c) a; 
                            else a; 
                        else }"""
        e = "Error on line 6 col 29: }"
        self.assertTrue(TestParser.checkParser(i, e, 286))

    def test_array_pointer2(self):
        i = """string[] foo(){
                    int c[3];
                    return c;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 287))

    def test_array_pointer3(self):
        i = """string[]foo(){return c[10];}"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 288))

    def test_array_pointer4(self):
        i = """float[10]foo(){return c;}"""
        e = "Error on line 1 col 6: 10"
        self.assertTrue(TestParser.checkParser(i, e, 289))

    def test_bulk27(self):
        i = """void foo (int i) {
                    int child_of_foo ( f loat f ) { . . . } //ERROR
            }"""
        e = "Error on line 2 col 37: ("
        self.assertTrue(TestParser.checkParser(i, e, 290))

    def test_bulk28(self):
        i = """int[] foo(int a, float b[]) {
                    int c[3]; 
                    if (a>0) 
                        foo(2)[3+x] = a[b[2]] + 3;
                    return c; 
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 291))
    
    def test_bulk29(self):
        i = """int i ;
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
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 292))

    def test_bulk30(self):
        i = """ int foo(float a){
                    if (a==1)
                        if (b>3) c=5;
                        else d=1;
                    if (e<4) good();
                    else
                        if (h>5) notgood();
                        else good();
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 293))
    
    def test_bulk31(self):
        i = """ int foo(){
                    float a;
                    a = (((5 != 6) < (6 == 5)) >= (4 + 5 > 1)) <= 1;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 294))

    def test_bulk32(self):
        i = """ void main(){
                    a = -a * b / 5 + (x && y && z + a || q * -p) && 6 * 5 / -(5 % t);
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 295))

    def test_bulk33(self):
        i = """ void main() {
                    float a;
                    a = b/2*n/4/5%2 && 2*9/4%2;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 296))

    def test_bulk34(self):
        i = """ int main(){
                    foo(2)[3+x] = a[b[f+y[2]-h[t[5+j]] * 4]] + 3;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 297))
    
    def test_bulk35(self):
        i = """ int main(){
                    b[1] = 1;
                    foo(a+1)[2] = 1+a[1]+c+("abc"<0);
                    foo(1)[m+1] = 3;
                    foo(1+a[1]+(1<0))[10] = 4;
            }"""
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 298))

    def test_bulk36(self):
        i = """ float foo(){
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
        e = "successful"
        self.assertTrue(TestParser.checkParser(i, e, 299))

    def test_bulk37(self):
        i = """ int [ ] foo ( int b [ ] ) {
                    a+b=c+d;
            }"""
        e = "Error on line 2 col 23: ="
        self.assertTrue(TestParser.checkParser(i, e, 300))
        