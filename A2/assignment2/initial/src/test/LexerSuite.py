import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifiers1(self):
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_identifiers2(self):
        self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
    def test_identifiers3(self):
        self.assertTrue(TestLexer.checkLexeme("aA$sVN","aA,Error Token $",103))
    def test_identifiers4(self):
        self.assertTrue(TestLexer.checkLexeme("_ca123abc 123ab_ 005aa", "_ca123abc,123,ab_,005,aa,<EOF>", 104))
    def test_identifiers5(self):
        self.assertTrue(TestLexer.checkLexeme("r.23d r,ab", "r,.23,d,r,,,ab,<EOF>", 105))
    def test_identifiers6(self):
        self.assertTrue(TestLexer.checkLexeme("abcdefgh345iklm ab4 4ab 00cde00", "abcdefgh345iklm,ab4,4,ab,00,cde00,<EOF>",106))

    def test_keyword1(self):
        i = "bool boolean BOOL Bool break Break Continue continue Continue& "
        o = "bool,boolean,BOOL,Bool,break,Break,Continue,continue,Continue,Error Token &"
        self.assertTrue(TestLexer.checkLexeme(i, o, 107))
    def test_keyword2(self):
        i = "if If IF else Else ELSE for FOR For While while Do DO do"
        o = "if,If,IF,else,Else,ELSE,for,FOR,For,While,while,Do,DO,do,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 108))
    def test_keyword3(self):
        i = "int Int INT float Float FLOAT string str STRING True true False false"
        o = "int,Int,INT,float,Float,FLOAT,string,str,STRING,True,true,False,false,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o ,109))
    def test_keyword4(self):
        i = "intfloat 12int sTring int50 string 1.1float"
        o = "intfloat,12,int,sTring,int50,string,1.1,float,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 133))
    def test_keyword5(self):
        i = "boolbool int_ dowhile if0else"
        o = "boolbool,int_,dowhile,if0else,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 134))

    def test_operator1(self):
        self.assertTrue(TestLexer.checkLexeme("a/3+4=12*b-3%2", "a,/,3,+,4,=,12,*,b,-,3,%,2,<EOF>", 110))
    def test_operator2(self):
        i = "!true && false || a == a; a!=b;a<>b;a<=b;a>=b;a=4ed"
        o = "!,true,&&,false,||,a,==,a,;,a,!=,b,;,a,<,>,b,;,a,<=,b,;,a,>=,b,;,a,=,4,ed,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 111))

    def test_separator(self):
        self.assertTrue(TestLexer.checkLexeme("a+(15) a[4], { program; }", "a,+,(,15,),a,[,4,],,,{,program,;,},<EOF>",112))

    def test_integer1(self):
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",113))
    def test_integer2(self):
        self.assertTrue(TestLexer.checkLexeme("-123,12/-123", "-,123,,,12,/,-,123,<EOF>",114))

    def test_float1(self):
        self.assertTrue(TestLexer.checkLexeme("1.2 1. .1 1e2 1.2E-2 1.2e-2", "1.2,1.,.1,1e2,1.2E-2,1.2e-2,<EOF>", 115))
    def test_float2(self):
        self.assertTrue(TestLexer.checkLexeme(".1E2 9.0 12e8 0.33E-3 128e-42", ".1E2,9.0,12e8,0.33E-3,128e-42,<EOF>", 116))
    def test_float3(self):
        self.assertTrue(TestLexer.checkLexeme("e-12 143e", "e,-,12,143,e,<EOF>", 117))
    def test_float4(self):
        self.assertTrue(TestLexer.checkLexeme(".e1", "Error Token .",118))
    def test_float5(self):
        self.assertTrue(TestLexer.checkLexeme("1.-1", "1.,-,1,<EOF>", 119))
    def test_float6(self):
        self.assertTrue(TestLexer.checkLexeme("1.2.1", "1.2,.1,<EOF>", 120))
    def test_float7(self):
        self.assertTrue(TestLexer.checkLexeme("abc.abc", "abc,Error Token .", 121))
    def test_float8(self):
        self.assertTrue(TestLexer.checkLexeme("12.e0 -101 11.E 11.1e2", "12.e0,-,101,11.,E,11.1e2,<EOF>", 122))
    def test_float9(self):
        self.assertTrue(TestLexer.checkLexeme("e-12.1 11.e1 12..12 2..2 .1e-3", "e,-,12.1,11.e1,12.,.12,2.,.2,.1e-3,<EOF>", 123))
    def test_float10(self):
        self.assertTrue(TestLexer.checkLexeme("e--12 e12E-15 99e 1E-15", "e,-,-,12,e12E,-,15,99,e,1E-15,<EOF>", 124))

    def test_block_comment1(self):
        self.assertTrue(TestLexer.checkLexeme("abc/*This is a block comment*/", "abc,<EOF>", 125))
    def test_block_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("/*This is the 2nd block comment with // */", "<EOF>", 126))
    def test_block_comment3(self):
        self.assertTrue(TestLexer.checkLexeme("abc/*This is a block comment with several symbols \n \t break;*/", "abc,<EOF>", 127))
    def test_block_comment4(self):
        self.assertTrue(TestLexer.checkLexeme("abc/*This is a block comment**//", "abc,/,<EOF>",128))
    
    def test_line_comment1(self):
        self.assertTrue(TestLexer.checkLexeme("abc//This is a line comment", "abc,<EOF>",129))
    def test_line_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("//This is a line comment with /* */ ","<EOF>", 130))
    def test_line_comment3(self):
        self.assertTrue(TestLexer.checkLexeme("/ /not_comment", "/,/,not_comment,<EOF>", 131))
    def test_comment1(self):
        self.assertTrue(TestLexer.checkLexeme("_an_id and /*comment","_an_id,and,/,*,comment,<EOF>",132))

    def test_string1(self):
        i = """ "abcde" """
        o = "abcde,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 135))
    def test_string2(self):
        i = """ "abc \\b abc" """
        o = "abc \\b abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 136))
    def test_string3(self):
        i = """ "abc \\f abc" """
        o = "abc \\f abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 137))
    def test_string5(self):
        i = """ "abc \\r abc" """
        o = "abc \\r abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 138))
    def test_string6(self):
        i = """ "abc \\n abc" """
        o = "abc \\n abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 139))
    def test_string7(self):
        i = """ "abc \\t abc" """
        o = "abc \\t abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 140))
    def test_string8(self):
        i = "zbc \"acb\"deff"
        o = "zbc,acb,deff,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 141))
    def test_string9(self):
        i = '"abc \\\\ abc"'
        o = "abc \\\\ abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 142))
    def test_string10(self):
        i = """ "This is a string" an_id //and a comment" """
        o = "This is a string,an_id,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 143))
    
    def test_illegal_escape1(self):
        i = """ "This is a string with illegal escape \\k leave out this part" """
        o = "Illegal Escape In String: This is a string with illegal escape \\k"
        self.assertTrue(TestLexer.checkLexeme(i, o, 144))
    def test_illegal_escape2(self):
        i = """ "A string with \\ is not accepted" """
        o = "Illegal Escape In String: A string with \\ "
        self.assertTrue(TestLexer.checkLexeme(i, o, 145))
    def test_illegal_escape3(self):
        i = """ "There's 2 illegal escape \\. and \\j" """
        o = "Illegal Escape In String: There's 2 illegal escape \\."
        self.assertTrue(TestLexer.checkLexeme(i, o, 146))
    def test_illegal_escape4(self):
        i = """ An_id and "A string with \\m is wrong" """
        o = "An_id,and,Illegal Escape In String: A string with \\m"
        self.assertTrue(TestLexer.checkLexeme(i, o, 147))
    def test_illegal_escape5(self):
        i = """ "A string with \\o and" an_id and number 4000"""
        o = "Illegal Escape In String: A string with \\o"
        self.assertTrue(TestLexer.checkLexeme(i, o, 148))
    def test_illegal_escape6(self):
        i = "abc+na\"m12345678\\lb"
        o = "abc,+,na,Illegal Escape In String: m12345678\\l"
        self.assertTrue(TestLexer.checkLexeme(i, o, 149))

    def test_unclosed_string1(self):
        i = """ "A string without closing """
        o = "Unclosed String: A string without closing "
        self.assertTrue(TestLexer.checkLexeme(i, o, 150))
    def test_unclosed_string2(self):
        i = """ an_id 1000 +-==*/>= "A string"""
        o = "an_id,1000,+,-,==,*,/,>=,Unclosed String: A string"
        self.assertTrue(TestLexer.checkLexeme(i, o, 151))
    def test_unclosed_string3(self):
        i = """ something "string \n"""
        o = "something,Unclosed String: string "
        self.assertTrue(TestLexer.checkLexeme(i, o, 152))
    def test_unclosed_string4(self):
        i = """ "a string \\n"""
        o = "Unclosed String: a string \\n"
        self.assertTrue(TestLexer.checkLexeme(i, o, 153))
    def test_unclosed_string5(self):
        i = '"a string \\'
        o = 'Unclosed String: a string '
        self.assertTrue(TestLexer.checkLexeme(i, o, 154))
    def test_unclosed_string6(self):
        i = """ an_id /*a comment*/ "a string" "an unclosed string """
        o = "an_id,a string,Unclosed String: an unclosed string "
        self.assertTrue(TestLexer.checkLexeme(i, o, 155))
    
    def test_error_char1(self):
        i = "(*101*) 11.+12*#"
        o = "(,*,101,*,),11.,+,12,*,Error Token #"
        self.assertTrue(TestLexer.checkLexeme(i, o, 157))
    def test_error_char2(self):
        i = "Abcdef`abcd"
        o = "Abcdef,Error Token `"
        self.assertTrue(TestLexer.checkLexeme(i, o, 158))
    def test_error_char3(self):
        i = "abcnefgh?1.12.2"
        o = "abcnefgh,Error Token ?"
        self.assertTrue(TestLexer.checkLexeme(i, o, 159))
    def test_error_char4(self):
        i = "ab-cd!efgh"
        o = "ab,-,cd,!,efgh,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 160))
    def test_error_char5(self):
        i = "abc+def+a{'}-9[]"
        o = "abc,+,def,+,a,{,Error Token '"
        self.assertTrue(TestLexer.checkLexeme(i, o, 161))
    def test_error_char6(self):
        i = "aBC[anc{]@abc"
        o = "aBC,[,anc,{,],Error Token @"
        self.assertTrue(TestLexer.checkLexeme(i, o, 162))
    def test_error_char7(self):
        i = "abc*de[;abc]"
        o = "abc,*,de,[,;,abc,],<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 163))

    def test_all1(self):
        i = """ 123abcd int[] """
        o = "123,abcd,int,[,],<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 156))
    def test_all2(self):
        i = "\"hel\\\"l\\\"o\\\\k\""
        o = "hel\\\"l\\\"o\\\\k,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(i, o, 164))
    def test_all3(self):
        i = "n=foo(int k){a=b;}"
        o = "n,=,foo,(,int,k,),{,a,=,b,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 165))
    def test_all4(self):
        i = "def f(k){ if len(k)==1 return 1/n;}"
        o = "def,f,(,k,),{,if,len,(,k,),==,1,return,1,/,n,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 166))
    def test_all5(self):
        i = "a //comment\n and an_id"
        o = "a,and,an_id,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 167))
    def test_all6(self):
        i = "a /*comment which does not close"
        o = "a,/,*,comment,which,does,not,close,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 168))
    def test_all7(self):
        i = """ "abc###" //a comment\n float 1.1e"""
        o = "abc###,float,1.1,e,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 169))
    def test_all8(self):
        i = """ "random //comment ne\\n het_comment/*comment nua ne*/" """
        o = "random //comment ne\\n het_comment/*comment nua ne*/,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 170))
    def test_all9(self):
        i = """random //comment ne\n het_comment/*comment nua ne*/"""
        o = "random,het_comment,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 171))
    def test_all10(self):
        i = "[abcd] = [1234] a.method()"
        o = "[,abcd,],=,[,1234,],a,Error Token ."
        self.assertTrue(TestLexer.checkLexeme(i, o, 172))
    def test_all11(self):
        i = "1.2.3abc// a comment"
        o = "1.2,.3,abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 173))
    def test_all12(self):
        i = "1.2.3..4..4..5"
        o = "1.2,.3,Error Token ."
        self.assertTrue(TestLexer.checkLexeme(i, o, 174))
    def test_all13(self):
        i = """ "unclose string?  \n """
        o = "Unclosed String: unclose string?  "
        self.assertTrue(TestLexer.checkLexeme(i, o, 175))
    def test_all14(self):
        i = """1.1.1.2 "this string is unclosed \f other part"""
        o = "1.1,.1,.2,Unclosed String: this string is unclosed "
        self.assertTrue(TestLexer.checkLexeme(i, o, 176))
    def test_all15(self):
        i = """ "unclosed string without escape"""
        o = "Unclosed String: unclosed string without escape"
        self.assertTrue(TestLexer.checkLexeme(i, o, 177))
    def test_all16(self):
        i = """a+b = c+d; string s = "abc\\ndef" """
        o = "a,+,b,=,c,+,d,;,string,s,=,abc\\ndef,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 178))
    def test_all17(self):
        i = "9.0 11.1 .33.4 123/abc123abc 123abc"
        o = "9.0,11.1,.33,.4,123,/,abc123abc,123,abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 179))
    def test_all18(self):
        i = "12e2 11e e11 3e3 .3 e3.3 3e.30"
        o = "12e2,11,e,e11,3e3,.3,e3,.3,3,e,.30,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 180))
    def test_all19(self):
        i = "/*abc ----???*/"
        o = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 181))
    def test_all20(self):
        i = "//"
        o = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 182))
    def test_all21(self):
        i = """{abcde} /* // a comment"""
        o = "{,abcde,},/,*,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 183))
    def test_all22(self):
        i = "abc>>>======"
        o = "abc,>,>,>=,==,==,=,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 184))
    def test_all23(self):
        i = """ a+b=5 "!@#$$" """
        o = "a,+,b,=,5,!@#$$,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 185))
    def test_all24(self):
        i = "intx[a[b[c[d[e;f=g%h]]]]]"
        o = "intx,[,a,[,b,[,c,[,d,[,e,;,f,=,g,%,h,],],],],],<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 186))
    def test_all25(self):
        i = """ "a string" "another string" unopened string" """
        o = 'a string,another string,unopened,string,Unclosed String:  '
        self.assertTrue(TestLexer.checkLexeme(i, o, 187))
    def test_all26(self):
        i = """ an_id anum 123.456e10 "a string with //comment? and\\h" """
        o = """an_id,anum,123.456e10,Illegal Escape In String: a string with //comment? and\\h"""
        self.assertTrue(TestLexer.checkLexeme(i, o, 188))
    def test_all27(self):
        i = """ "another test for \\t string" """
        o = """another test for \\t string,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(i, o, 189))
    def test_all28(self):
        i = """ "3^4 \nabcfdefghiklmnopqrstv" """
        o = "Unclosed String: 3^4 "
        self.assertTrue(TestLexer.checkLexeme(i, o, 190))
    def test_all29(self):
        i = "00.00e2"
        o = "00.00e2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 191))
    def test_all30(self):
        i = """ "Cuc xi` lau` la` ong be lap' \\F" """
        o = "Illegal Escape In String: Cuc xi` lau` la` ong be lap' \\F"
        self.assertTrue(TestLexer.checkLexeme(i, o, 192))
    def test_all31(self):
        i = """ "abcde\\?" """
        o = "Illegal Escape In String: abcde\\?"
        self.assertTrue(TestLexer.checkLexeme(i, o, 193))
    def test_all32(self):
        i = "1234abc1234abc: 20"
        o = "1234,abc1234abc,Error Token :"
        self.assertTrue(TestLexer.checkLexeme(i, o, 194))
    def test_all33(self):
        i = "int main(){int a[10], if (a<10): a = 10;}"
        o = "int,main,(,),{,int,a,[,10,],,,if,(,a,<,10,),Error Token :"
        self.assertTrue(TestLexer.checkLexeme(i, o, 195))
    def test_all34(self):
        i = "//a comment\n /*another one*/ //and one more\n "
        o = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 196))
    def test_all35(self):
        i = ">==>==>==//**0"
        o = ">=,=,>=,=,>=,=,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 197))
    def test_all36(self):
        i = "int(){for(a=10;a<20;a++)}"
        o = "int,(,),{,for,(,a,=,10,;,a,<,20,;,a,+,+,),},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 198))
    def test_all37(self):
        i = "1.1.1.1.1.1.e.e.1"
        o = "1.1,.1,.1,.1,.1,Error Token ."
        self.assertTrue(TestLexer.checkLexeme(i, o, 199))
    def test_all38(self):
        i = "100010001 0x10001 0xAFCC"
        o = "100010001,0,x10001,0,xAFCC,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(i, o, 200))

