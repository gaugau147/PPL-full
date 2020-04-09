// Tran Thi Ngoc Diep - 1827005

grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// 1. Program
// 1.1. Program structure
program         : declare+ EOF;
declare         : var_declaration | function_declaration ;

// 1.2. variable declaration
var_declaration : primitive_type var_list SEMI ;
var_list        : variable COMMA var_list | variable ;
primitive_type  : INTEGER 
                | FLOAT 
                | STRING 
                | BOOLEAN ;  
void_type       : VOID ;
variable        : ID | ID LSB INTLIT RSB ;

// 1.3. function declaration
function_declaration: return_type function_name LP param_list? RP body ;
return_type     : primitive_type | void_type | array_pointer_type;
array_pointer_type: primitive_type LSB RSB;
function_name   : ID ;
param_list      : param_declaration COMMA param_list | param_declaration ;

param_declaration   : ( primitive_type ID ) 
                    | ( primitive_type ID LSB RSB ) 
                    ;
body            : block_statement ;

// 1.4. Statement and control flow
statement       : block_statement 
                | assign_statement
                | if_statement
                | do_while_statement
                | for_statement
                | break_statement
                | continue_statement
                | return_statement
                | expression_statement
                ;

// 1.4.1. Block statement
block_statement : LCB statement_list? RCB ;
statement_list  : stmt_decl+ ;
stmt_decl       : statement | var_declaration ;


// 1.4.2. Assign statement
assign_statement: assignment SEMI;
assignment      : assign_LHS ASSIGN assignment | exp ;
assign_LHS      : ID | index_expression ;

// Precedence and Associativity
exp_list        : exp COMMA exp_list | exp;
exp             : exp OR exp1 | exp1 ;
exp1            : exp1 AND exp2 | exp2 ; 
exp2            : exp3 ( EQ | NEQ ) exp3 | exp3 ;
exp3            : exp4 ( LT | LTE | GT | GTE ) exp4 | exp4 ;
exp4            : exp4 ( ADD | SUB ) exp5 | exp5 ;
exp5            : exp5 ( DIV | MUL | DIV_INT ) exp6 | exp6 ;
exp6            : ( SUB | NOT ) exp6 | exp7 ;
exp7            : operand ;

// Index Expression
index_expression: operand1 operand2 ;
operand         : literal | operand1 ;
literal         : INTLIT | FLOATLIT | BOOLLIT | STRINGLIT ;
operand1        : ID | func_call | LP assignment RP | operand1 operand2 ;

operand2        : LSB exp RSB ;
func_call       : ID LP exp_list? RP ;

assign_right    : assignment | exp ;

// 1.4.3. if statement
if_statement    : IF LP exp_bool RP statement (ELSE statement)? ;
exp_bool        : assignment ;

// 1.4.4. do while statement
do_while_statement  : DO statement+ WHILE exp_bool SEMI ; 

// 1.4.5. for statement
for_statement   : FOR LP exp_for SEMI exp_for SEMI exp_for RP statement ;
exp_for         : assignment ;

// 1.4.6. break statement
break_statement : BREAK SEMI ;

// 1.4.7. continue statement
continue_statement  : CONTINUE SEMI ;

// 1.4.8. return statement
return_statement: RETURN exp_re? SEMI ;
exp_re          : assignment ;

//1.4.9. expression statement
expression_statement: exp SEMI ;

// 2. Lexer Declaration
// 2.1. Fragments

fragment E: [eE];

// 2.2. Keywords

// Methods

// If else Statement
IF	: 'if' ;
ELSE	: 'else' ;

// Loop Statement
FOR	: 'for' ;
WHILE	: 'while' ; 
DO	: 'do' ;

// Stop Statement
RETURN	: 'return' ;
BREAK	: 'break' ;
CONTINUE: 'continue' ;

// Primitive Types
INTEGER : 'int' ;
STRING  : 'string' ;
FLOAT   : 'float' ;
BOOLEAN : 'boolean' ;
VOID	: 'void' ;

// 2.3. Operators
DIV_INT	: '%' ;
NOT	    : '!' ;
AND	    : '&&' ;
OR	    : '||' ;

ADD	    : '+' ;
SUB	    : '-' ;
MUL	    : '*' ;
DIV	    : '/' ;

ASSIGN	: '=' ;
LT	    : '<' ;
LTE	    : '<=' ;
GT	    : '>' ;
GTE	    : '>=' ;
NEQ	    : '!=';
EQ	    : '==';

// 2.4. Specific characters
LP	    : '(' ;
RP	    : ')' ;
LSB	    : '[' ;
RSB	    : ']' ;
LCB     : '{' ;
RCB     : '}' ;

SEMI 	: ';' ;
COMMA	: ',' ;
fragment DOT: '.' ;

// 2.5. Comment
BLOCK_COMMENT	: '/*' .*? '*/'	-> skip ;
LINE_COMMENT	: '//' ~[\r\n]*	-> skip ;


// 2.6. TYPES AND VALUES
// boolean literal
BOOLLIT		: 'true' | 'false' ;

// float literal
fragment EXPONENT   : E SUB? DIGIT+ ;
fragment DIGIT	    : [0-9] ;
fragment SIGN	    : [+-] ;

FLOATLIT    : DIGIT+ DOT DIGIT* EXPONENT?
            | DIGIT+ EXPONENT
            | DIGIT* DOT DIGIT+ EXPONENT?;

// int literal
INTLIT	    : DIGIT+ ;

// identifier
ID	        : [_a-zA-Z][_a-zA-Z0-9]* ;

// string literal, illegal escape, unclosed string and error character
STRINGLIT	: '"' CHAR* '"' 
            { 
		        input_string = str(self.text)
		        self.text = input_string[1:-1]
	        } //get the string, leave out double quote
	        ;

fragment CHAR	: ~[\b\f\r\n\t"\\]     
    			| ESC_SEQ
    			;

fragment ESC_SEQ: '\\' [bfrnt"\\] ;

fragment ESC_ILL: '\\' ~[bfrnt"\\] ;


UNCLOSE_STRING  : '"' CHAR* ( [\b\f\r\n\t"\\] | EOF ) 
                {
                    input_string = str(self.text)
                    escape = ['\b', '\n', '\r', '\f', '\t', '"', '\\']
                    if input_string[-1] in escape:
                        self.text = input_string[1:-1]
                    else:
                        self.text = input_string[1:]
                } //excluding the legal escape
                ;

ILLEGAL_ESCAPE  : '"' CHAR* ESC_ILL;

// White space
WS 	: [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// Error character
ERROR_CHAR: .;