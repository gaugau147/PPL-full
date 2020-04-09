# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declare.
    def visitDeclare(self, ctx:MCParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_declaration.
    def visitVar_declaration(self, ctx:MCParser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_list.
    def visitVar_list(self, ctx:MCParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitive_type.
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#void_type.
    def visitVoid_type(self, ctx:MCParser.Void_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variable.
    def visitVariable(self, ctx:MCParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#function_declaration.
    def visitFunction_declaration(self, ctx:MCParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_type.
    def visitReturn_type(self, ctx:MCParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_pointer_type.
    def visitArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#function_name.
    def visitFunction_name(self, ctx:MCParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#param_list.
    def visitParam_list(self, ctx:MCParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#param_declaration.
    def visitParam_declaration(self, ctx:MCParser.Param_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#body.
    def visitBody(self, ctx:MCParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_statement.
    def visitBlock_statement(self, ctx:MCParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement_list.
    def visitStatement_list(self, ctx:MCParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt_decl.
    def visitStmt_decl(self, ctx:MCParser.Stmt_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#assign_statement.
    def visitAssign_statement(self, ctx:MCParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#assignment.
    def visitAssignment(self, ctx:MCParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#assign_LHS.
    def visitAssign_LHS(self, ctx:MCParser.Assign_LHSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_list.
    def visitExp_list(self, ctx:MCParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp1.
    def visitExp1(self, ctx:MCParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp2.
    def visitExp2(self, ctx:MCParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp3.
    def visitExp3(self, ctx:MCParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp4.
    def visitExp4(self, ctx:MCParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp5.
    def visitExp5(self, ctx:MCParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp6.
    def visitExp6(self, ctx:MCParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp7.
    def visitExp7(self, ctx:MCParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#index_expression.
    def visitIndex_expression(self, ctx:MCParser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#literal.
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operand1.
    def visitOperand1(self, ctx:MCParser.Operand1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operand2.
    def visitOperand2(self, ctx:MCParser.Operand2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_call.
    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#assign_right.
    def visitAssign_right(self, ctx:MCParser.Assign_rightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_statement.
    def visitIf_statement(self, ctx:MCParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_bool.
    def visitExp_bool(self, ctx:MCParser.Exp_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#do_while_statement.
    def visitDo_while_statement(self, ctx:MCParser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_statement.
    def visitFor_statement(self, ctx:MCParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_for.
    def visitExp_for(self, ctx:MCParser.Exp_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_statement.
    def visitBreak_statement(self, ctx:MCParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_statement.
    def visitContinue_statement(self, ctx:MCParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_statement.
    def visitReturn_statement(self, ctx:MCParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_re.
    def visitExp_re(self, ctx:MCParser.Exp_reContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_statement.
    def visitExpression_statement(self, ctx:MCParser.Expression_statementContext):
        return self.visitChildren(ctx)



del MCParser