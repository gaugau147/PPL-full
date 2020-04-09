
#Tran Thi Ngoc Diep - 1827005

from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import *


class ASTGeneration(MCVisitor):

    def visitProgram(self, ctx:MCParser.ProgramContext):
        '''program: declare+ EOF;'''
        return Program(list(reduce(lambda x,y: x+y,[self.visit(t) for t in ctx.declare()],[])))

    
    def visitDeclare(self, ctx:MCParser.DeclareContext):
        '''declare: var_declaration | function_declaration;'''
        return self.visit(ctx.getChild(0))


    def visitVar_declaration(self, ctx:MCParser.Var_declarationContext):
        '''var_declaration: primitive_type var_list SEMI;
        '''
        var_typ = self.visit(ctx.primitive_type())
        var_lst = self.visit(ctx.var_list())
        return [VarDecl(x[0],ArrayType(x[1],var_typ) if x[1]>0 else var_typ) for x in var_lst]


    def visitVar_list(self, ctx:MCParser.Var_listContext):
        '''var_list: variable COMMA var_list | variable ;'''
        return [self.visit(ctx.variable())] + self.visit(ctx.var_list()) if ctx.var_list() else [self.visit(ctx.variable())]

    
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        if ctx.INTEGER(): return IntType()
        if ctx.FLOAT(): return FloatType()
        if ctx.BOOLEAN(): return BoolType()
        if ctx.STRING(): return StringType()


    def visitVoid_type(self, ctx:MCParser.Void_typeContext):
        return VoidType()


    def visitVariable(self, ctx:MCParser.VariableContext):
        '''variable: ID | ID LSB INTLIT RSB ;'''
        if ctx.getChildCount()==1:
            return (ctx.ID().getText(),-1)
        else:
            return (ctx.ID().getText(),int(ctx.INTLIT().getText()))


    def visitFunction_declaration(self, ctx:MCParser.Function_declarationContext):
        '''function_declaration: return_type function_name LP param_list? RP body ;'''
        func_name = Id(self.visit(ctx.function_name()))
        param = self.visit(ctx.param_list()) if ctx.param_list() else []
        return_typ = self.visit(ctx.return_type())
        func_body = self.visit(ctx.body())
        return [FuncDecl(func_name, param, return_typ, func_body)]
    
    def visitFunction_name(self, ctx:MCParser.Function_nameContext):
        '''function_name: ID ;'''
        return ctx.ID().getText()

    def visitParam_list(self, ctx:MCParser.Param_listContext):
        '''param_list: param_declaration COMMA param_list | param_declaration ;'''
        return [self.visit(ctx.param_declaration())] + self.visit(ctx.param_list()) if ctx.param_list() else [self.visit(ctx.param_declaration())]

    def visitParam_declaration(self, ctx:MCParser.Param_declarationContext):
        '''param_declaration: ( primitive_type ID ) | ( primitive_type ID LSB RSB );'''
        return VarDecl(ctx.ID().getText(), self.visit(ctx.primitive_type())) if (ctx.getChildCount() == 2) else VarDecl(ctx.ID().getText(), ArrayPointerType(self.visit(ctx.primitive_type())))

    def visitReturn_typeContext(self, ctx:MCParser.Return_typeContext):
        '''return_type: primitive_type | void_type | array_pointer_type;'''
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        elif ctx.void_type:
            return self.visit(ctx.void_type())
        else:
            return self.visit(ctx.array_pointer_type())

    def visitArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        '''array_pointer_type: primitive_type LSB RSB;'''
        return ArrayPointerType(self.visit(ctx.primitive_type()))

    def visitBody(self, ctx:MCParser.BodyContext):
        '''body: block_statement ;'''
        return self.visit(ctx.block_statement())

    def visitBlock_statement(self, ctx:MCParser.Block_statementContext):
        '''block_statement: LCB statement_list? RCB ;'''
        return Block(self.visit(ctx.statement_list())) if ctx.statement_list() else Block([])

    def visitStatement_list(self, ctx:MCParser.Statement_listContext):
        '''statement_list: stmt_decl+ ;'''
        declList = []
        for x in ctx.stmt_decl():
            decl = self.visit(x)
            if isinstance(decl, list):
                declList.extend(decl if decl else [])
            else:
                declList.append(decl)
        return declList

    def visitStmt_decl(self, ctx:MCParser.Stmt_declContext):
        '''stmt_decl: statement | var_declaration ;'''
        return self.visit(ctx.statement()) if ctx.statement() else self.visit(ctx.var_declaration())

    def visitStatement(self, ctx:MCParser.StatementContext):
        '''statement: block_statement 
                | assign_statement
                | if_statement
                | do_while_statement
                | for_statement
                | break_statement
                | continue_statement
                | return_statement
                | expression_statement
                ;'''
        if ctx.block_statement(): return self.visit(ctx.block_statement())
        elif ctx.assign_statement(): return self.visit(ctx.assign_statement())
        elif ctx.if_statement(): return self.visit(ctx.if_statement())
        elif ctx.do_while_statement(): return self.visit(ctx.do_while_statement())
        elif ctx.for_statement(): return self.visit(ctx.for_statement())
        elif ctx.break_statement(): return self.visit(ctx.break_statement())
        elif ctx.continue_statement(): return self.visit(ctx.continue_statement())
        elif ctx.return_statement(): return self.visit(ctx.return_statement())
        else: return self.visit(ctx.expression_statement())

    def visitAssign_statement(self, ctx:MCParser.Assign_statementContext):
        '''assign_statement: assignment SEMI;'''
        return self.visit(ctx.assignment())

    def visitAssignment(self, ctx:MCParser.AssignmentContext):
        '''assignment: assign_LHS ASSIGN assignment | exp ;'''
        if ctx.ASSIGN():
            left = self.visit(ctx.assign_LHS())
            right = self.visit(ctx.assignment())
            return BinaryOp(ctx.ASSIGN().getText(), left, right)
        else:
            return self.visit(ctx.exp())
    
    def visitAssign_LHS(self, ctx:MCParser.Assign_LHSContext):
        '''assign_LHS: ID | index_expression ;'''
        return Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.index_expression())

    def visitExp(self, ctx:MCParser.ExpContext):
        '''exp: exp OR exp1 | exp1 ;'''
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1())
        else:
            left = self.visit(ctx.exp())
            right = self.visit(ctx.exp1())
            return BinaryOp(ctx.OR().getText(), left, right)
    
    def visitExp1(self, ctx:MCParser.Exp1Context):
        '''exp1: exp1 AND exp2 | exp2 ; '''
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2())
        else:
            left = self.visit(ctx.exp1())
            right = self.visit(ctx.exp2())
            return BinaryOp(ctx.AND().getText(), left, right)
    
    def visitExp2(self, ctx:MCParser.Exp2Context):
        '''exp2: exp3 ( EQ | NEQ ) exp3 | exp3 ;'''
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3(0))
        else:
            left = self.visit(ctx.exp3(0))
            right = self.visit(ctx.exp3(1))
            op = ctx.EQ().getText() if ctx.EQ() else ctx.NEQ().getText()
            return BinaryOp(op, left, right)
    
    def visitExp3(self, ctx:MCParser.Exp3Context):
        '''exp3: exp4 ( LT | LTE | GT | GTE ) exp4 | exp4 ;'''
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4(0))
        else:
            left = self.visit(ctx.exp4(0))
            right = self.visit(ctx.exp4(1))
            if ctx.LT(): op = ctx.LT().getText()
            elif ctx.LTE(): op = ctx.LTE().getText()
            elif ctx.GT(): op = ctx.GT().getText()
            else: op = ctx.GTE().getText()
            return BinaryOp(op, left, right)

    def visitExp4(self, ctx:MCParser.Exp4Context):
        '''exp4: exp4 ( ADD | SUB ) exp5 | exp5 ;'''
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        else:
            left = self.visit(ctx.exp4())
            right = self.visit(ctx.exp5())
            op = ctx.ADD().getText() if ctx.ADD() else ctx.SUB().getText()
            return BinaryOp(op, left, right)
    
    def visitExp5(self, ctx:MCParser.Exp5Context):
        '''exp5: exp5 ( DIV | MUL | DIV_INT ) exp6 | exp6 ;'''
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        else:
            left = self.visit(ctx.exp5())
            right = self.visit(ctx.exp6())
            if ctx.DIV(): op = ctx.DIV().getText()
            elif ctx.MUL(): op = ctx.MUL().getText()
            else: op = ctx.DIV_INT().getText()
            return BinaryOp(op, left, right)

    def visitExp6(self, ctx:MCParser.Exp6Context):
        '''exp6: ( SUB | NOT ) exp6 | exp7 ;'''
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        else:
            right = self.visit(ctx.exp6())
            op = ctx.SUB().getText() if ctx.SUB() else ctx.NOT().getText()
            return UnaryOp(op, right)

    def visitExp7(self, ctx:MCParser.Exp7Context):
        '''exp7: operand ;'''
        return self.visit(ctx.operand())

    def visitExp_bool(self, ctx:MCParser.Exp_boolContext):
        '''exp_bool: assignment ;'''
        return self.visit(ctx.assignment())

    def visitExp_for(self, ctx:MCParser.Exp_forContext):
        '''exp_for: assignment ;'''
        return self.visit(ctx.assignment())

    def visitExp_re(self, ctx:MCParser.Exp_reContext):
        '''exp_re: assignment ;'''
        return self.visit(ctx.assignment())

    def visitOperand(self, ctx:MCParser.OperandContext):
        '''operand: literal | operand1 ;'''
        return self.visit(ctx.literal()) if ctx.literal() else self.visit(ctx.operand1())
    
    def toBool(self, x):
        return x == "true"

    def visitLiteral(self, ctx:MCParser.LiteralContext):
        ''' literal: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT;'''
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(self.toBool(ctx.BOOLLIT().getText()))
        else:
            return StringLiteral(ctx.STRINGLIT().getText())
    
    def visitOperand1(self, ctx:MCParser.Operand1Context):
        '''operand1: ID | func_call | LP assignment RP | operand1 operand2 ;'''
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        elif ctx.assignment():
            return self.visit(ctx.assignment())
        else:
            op1 = self.visit(ctx.operand1())
            op2 = self.visit(ctx.operand2())
            return ArrayCell(op1, op2)

    def visitOperand2(self, ctx:MCParser.Operand2Context):
        '''operand2: LSB exp RSB ;'''
        return self.visit(ctx.exp())

    def visitIndex_expression(self, ctx:MCParser.Index_expressionContext):
        '''index_expression: operand1 operand2 ;'''
        op1 = self.visit(ctx.operand1())
        op2 = self.visit(ctx.operand2())
        return ArrayCell(op1, op2)

    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        '''func_call: ID LP exp_list? RP ;'''
        exp_lst = self.visit(ctx.exp_list()) if ctx.exp_list() else []
        return CallExpr(Id(ctx.ID().getText()), exp_lst)

    def visitExp_list(self, ctx:MCParser.Exp_listContext):
        '''exp_list: exp COMMA exp_list | exp;'''
        return [self.visit(ctx.exp( ))] + self.visit(ctx.exp_list()) if ctx.exp_list() else [self.visit(ctx.exp())]

    def visitAssign_right(self, ctx:MCParser.Assign_rightContext):
        '''assign_right: assignment | exp ;'''
        return self.visit(ctx.assignment()) if ctx.assignment() else self.visit(ctx.exp())

    def visitIf_statement(self, ctx:MCParser.If_statementContext):
        '''if_statement: IF LP exp_bool RP statement (ELSE statement)? ;'''
        return If(self.visit(ctx.exp_bool()),self.visit(ctx.statement(0)),self.visit(ctx.statement(1))) if ctx.ELSE() else If(self.visit(ctx.exp_bool()),self.visit(ctx.statement(0)))

    def visitDo_while_statement(self, ctx:MCParser.Do_while_statementContext):
        '''do_while_statement: DO statement+ WHILE exp_bool SEMI ; '''
        stmt_lst = [self.visit(x) for x in ctx.statement()]
        exp_bool = self.visit(ctx.exp_bool())
        return Dowhile(stmt_lst, exp_bool)

    def visitFor_statement(self, ctx:MCParser.For_statementContext):
        '''for_statement: FOR LP exp_for SEMI exp_for SEMI exp_for RP statement ;'''
        exp0 = self.visit(ctx.exp_for(0))
        exp1 = self.visit(ctx.exp_for(1))
        exp2 = self.visit(ctx.exp_for(2))
        stmt = self.visit(ctx.statement())
        return For(exp0, exp1, exp2, stmt)

    def visitBreak_statement(self, ctx:MCParser.Break_statementContext):
        '''break_statement: BREAK SEMI ;'''
        return Break()

    def visitContinue_statement(self, ctx:MCParser.Continue_statementContext):
        '''continue_statement: CONTINUE SEMI ;'''
        return Continue()

    def visitReturn_statement(self, ctx:MCParser.Return_statementContext):
        '''return_statement: RETURN exp_re? SEMI ;'''
        return Return(self.visit(ctx.exp_re())) if ctx.exp_re() else Return()

    def visitExpression_statement(self, ctx:MCParser.Expression_statementContext):
        '''expression_statement: exp SEMI ;'''
        return self.visit(ctx.exp())

