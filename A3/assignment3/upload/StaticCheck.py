# 1827005 - Tran Thi Ngoc Diep
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import *


class MType:
    # Type of function declaration
    # partype: parameter type
    # rettype: return type

    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MType( ' + str([str(x) for x in self.partype]) + "," + str(self.rettype) + ')'

class ExpUtils:
    @staticmethod
    def isNaNType(expType):
        return type(expType) not in [IntType, FloatType]

    @staticmethod
    def isOpForNumber(operator):
        return str(operator) in ['+', '-', '*', '/', '%', '>', '<', '>=', '<=']

    @staticmethod
    def mergeNumberType(lType, rType):
        return FloatType() if FloatType in [type(x) for x in [lType, rType]] else IntType()

class Symbol:
    '''
    name: string
    mtype: MType | ArrayType | ArrayPointerType | PrimitiveType
    value:
    kind: Function() | Parameter() | Variable()
    isGlobal: boolean
    '''
    # set the default declare type is FuncDecl
    def __init__(self, name, mtype, value=None, kind=Function(), isGlobal=False):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.isGlobal = isGlobal

    def __str__(self):
        return 'Symbol( ' + str(self.name) + "," + str(self.mtype) + "," + str(self.value) + ')'

    def getKind(self):
        return self.kind if type(self.mtype) is MType else Identifier()

    # turn a Symbol to tuple
    def toTuple(self):
        return (str(self.name), type(self.getKind()))

    # turn a Symbol to tuple of string
    def toTupleString(self):
        return (str(self.name), str(self.mtype))

    # change the kind of Symbol to parameter
    def toParam(self):
        self.kind = Parameter()
        return self

    # change the kind of Symbol to Variable
    def toVar(self):
        self.kind = Variable()
        return self

    # change the status of Symbol to Global???
    def toGlobal(self):
        self.isGlobal = True
        return self

    # change the name to string for comparing
    @staticmethod
    def cmp(symbol):
        return str(symbol.name)

    # set the declaration to VarDecl
    @staticmethod
    def fromVarDecl(decl):
        return Symbol(decl.variable, decl.varType, kind=Variable())

    # set the declaration to FuncDecl
    @staticmethod
    def fromFuncDecl(decl):
        paramType = [x.varType for x in decl.param]
        return Symbol(decl.name.name, MType(paramType, decl.returnType), kind=Function())

    @staticmethod
    def fromDecl(decl):
        return Symbol.fromVarDecl(decl) if type(decl) is VarDecl else Symbol.fromFuncDecl(decl)


class Scope:
    # 
    @staticmethod
    def isExisten(listSymbols, symbol):
        return len([x for x in listSymbols if str(x.name) == str(symbol.name)]) > 0

    @staticmethod
    def merge(currentScope, comingScope):
        # merge the local scope into the global scope
        # check if a symbol is in global scope yet
        return reduce(lambda lst, sym: lst if Scope.isExisten(lst, sym) else lst+[sym], currentScope, comingScope)


class Checker:
    '''
    class Utils:
        def lookup(self,name,lst,func):
            for x in lst:
                if name == func(x):
                    return x
            return None
    '''

    utils = Utils()

    @staticmethod
    def checkRedeclared(currentScope, listNewSymbols):
        # make a copy of current scope
        newScope = currentScope.copy()
        #traverse through the list of new declarations
        for x in listNewSymbols:
            # check if the name is already in current scope or not
            f = Checker.utils.lookup(Symbol.cmp(x), newScope, Symbol.cmp)
            if f is not None:
                raise Redeclared(x.kind, x.name)
            newScope.append(x)
        return newScope

    @staticmethod
    def checkUndeclared(visibleScope, name, kind, notGlobal=False):
        # Return Symbol declared in scope
        scope = visibleScope if not notGlobal else [
            x for x in visibleScope if not x.isGlobal]
        res = Checker.utils.lookup(
            (str(name), type(kind)), scope, lambda x: x.toTuple())
        if res is None:
            raise Undeclared(kind, name)
        return res


    @staticmethod
    def matchType(patternType, paramType):
        # Handle Array Type & Array Pointer Type
        if type(patternType) == ArrayPointerType and type(paramType) in [ArrayType, ArrayPointerType]:
            return type(patternType.eleType) == type(paramType.eleType)

        # Handle Primitive Types
        if type(patternType) == type(paramType): 
            return True
        if type(patternType) is FloatType and type(paramType) is IntType:
            return True
        return False

    @staticmethod
    def checkParamType(pattern, params):
        if len(pattern) != len(params): 
            return False
        # for i in pattern:
        #     if pattern[i]
        return all([Checker.matchType(a, b) for a, b in zip(pattern, params)])

    @staticmethod
    def handleReturnStmts(stmts):
        # stmts: [(stmt, type)]
        # traverse through list of n-1 stmts
        for i in range(0, len(stmts)-1):
            # check if there is return or continue stmt
            if Checker.isStopTypeStatment(stmts[i][1]):
                # raise unreachable stmt for the stmt after return/continue
                raise UnreachableStatement(stmts[i+1][0])
        return None if stmts == [] else stmts[-1][1]

    @staticmethod
    def isReturnTypeFunction(retType):
        # check return type
        return type(retType) in [IntType, FloatType, BoolType, StringType, ArrayPointerType, ArrayType]

    @staticmethod
    def isReturnType(retType):
        return Checker.isReturnTypeFunction(retType) 

    @staticmethod
    def isStopTypeStatment(retType):
        # check if stmt is return or continue stmt
        return Checker.isReturnType(retType) or type(retType) in [Break, Continue]

# Graph for Call Statements and Call Expression between Functions 
class Graph:
    # an object Graph has 3 dictionary attibutes
    link = {} # { 'n1': ['n2', 'n3'], 'n2': [], 'n3': ['n1', 'n2'] }
    visited = {} # { 'n1': True, 'n2': False, 'n3': False }
    invoked = {} # { 'n1': True, 'n2': False, 'n3': False }

    @staticmethod
    def initialize():
        Graph.link.clear()
        Graph.visited.clear()
        Graph.invoked.clear()

    @staticmethod
    def add(u, v=None):
        # u is a new key
        u = str(u)
        # if u not in Graph yet, add it to the graph and set to not visited
        if type(Graph.link.get(u)) != list:
            Graph.link[u] = []
            Graph.visited[u] = False
            Graph.invoked[u] = False
        # 
        if v is None: 
            return
        v = str(v)
        if v != u and v not in Graph.link[u]: 
            Graph.link[u].append(v)
            Graph.invoked[v] = True # v is invoked by u

    @staticmethod
    def dfs(u):
        # set u is visited
        u = str(u)
        Graph.visited[u] = True
        # set v is visited
        [Graph.dfs(v) for v in Graph.link[u] if not Graph.visited[v]]

    @staticmethod
    def getUnreachableNode():
        # traverse through the keys of link
        for u in Graph.link:
            # if a key is not visited and invoked
            if not Graph.visited[u] and not Graph.invoked[u]: 
                return u
        # traverse through the keys of link again
        for u in Graph.link:
            # if a key is not visited
            if not Graph.visited[u]: 
                return u
        return None

    @staticmethod
    def setDefaultVisitedNodes(listNodes):
        for u in listNodes: 
            Graph.visited[str(u)] = True

class StaticChecker(BaseVisitor, Utils):
    # Include all global declarations
    global_envi = [ Symbol("getInt",MType([],IntType())),
                    Symbol("putIntLn",MType([IntType()],VoidType())),
                    Symbol("putInt", MType([IntType()], VoidType())),
                    Symbol("getFloat", MType([], FloatType())),
                    Symbol("putFloat", MType([FloatType()], VoidType())),
                    Symbol("putFloatLn", MType([FloatType()], VoidType())),
                    Symbol("putBool", MType([BoolType()], VoidType())),
                    Symbol("putBoolLn", MType([BoolType()], VoidType())),
                    Symbol("putString", MType([StringType()], VoidType())),
                    Symbol("putStringLn", MType([StringType()], VoidType())),
                    Symbol("putLn", MType([], VoidType()))]
            
    
    def __init__(self,ast):
        self.ast = ast
    
    def check(self):
        Graph.initialize()
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast: Program, globalEnv): 
        # list all global declaration in the program and set it to global
        symbols = [Symbol.fromDecl(x).toGlobal() for x in ast.decl]
        # check if there is any redeclared in global environment
        scope = Checker.checkRedeclared(globalEnv, symbols)
        # check for no entry point error
        entryPoint = Symbol("main", MType([], VoidType()))
        # search in list of symbols and find main function
        res = self.lookup(entryPoint.toTupleString(), symbols, lambda x: x.toTupleString())
        if res is None:
            raise NoEntryPoint()
        # list of FuncDecl is global env + main func + other func declare in program
        listFuncDecl = globalEnv + [entryPoint] + [Symbol.fromDecl(x) for x in ast.decl if type(x) is FuncDecl]
        # traverse through the funcdecl and create a graph
        for x in listFuncDecl:
            Graph.add(x.name)
        # set all built in functions as visited
        Graph.setDefaultVisitedNodes([u.name for u in globalEnv])
        # visit declarations
        [self.visit(x, scope) for x in ast.decl]
        # set the main function as visited 
        Graph.dfs("main")
        # look for unreachable function
        u = Graph.getUnreachableNode()
        if u is not None: 
            symbol = self.lookup(u, listFuncDecl, Symbol.cmp)
            raise UnreachableFunction(symbol.name)
        return None
        
    def visitFuncDecl(self, ast: FuncDecl, scope): 
        # get list of parameters
        list_params = [self.visit(x,scope).toParam() for x in ast.param]
        # get list of var declarations
        list_vars = [self.visit(x, scope).toVar() for x in ast.body.member if type(x) is VarDecl]
        # list of new symbol in local scope
        list_new_symbols = list_params + list_vars
        # check for redeclaration in local scope
        localScope = Checker.checkRedeclared([], list_new_symbols)
        # if no error, merge it to the current scope
        newScope = Scope.merge(scope, localScope)
        # get the statements list inside the function
        stmts = [self.visit(x, (newScope, ast.returnType, False, ast.name.name)) for x in ast.body.member if not(type(x) is VarDecl)]
        # get return type 
        retType = Checker.handleReturnStmts(stmts)
        # check if return type is the same as function's
        if Checker.isReturnTypeFunction(ast.returnType) and not Checker.isReturnTypeFunction(retType):
            raise FunctionNotReturn(ast.name.name)
        
    def visitVarDecl(self, ast, scope):
        return Symbol.fromVarDecl(ast)
    
    # visit a block
    def visitBlock(self, ast: Block, params):
        scope, retType, inLoop, funcName = params
        # get list of variable declaration
        list_vars = [self.visit(x, scope).toVar() for x in ast.member if type(x) is VarDecl]
        # check for redeclaration in local scope
        localScope = Checker.checkRedeclared([], list_vars)
        # if no error, merge it to the current scope
        newScope = Scope.merge(scope, localScope)
        # get the statements list inside the function
        stmts = [self.visit(x, (newScope, retType, inLoop, funcName)) for x in ast.member if not(type(x) is VarDecl)]
        # get return type 
        ret = Checker.handleReturnStmts(stmts)
        return (ast, None)

    # Visit statements
    # params: (scope, retType, inLoop, funcName)
    # return a tupe (Statement, Return type)
    
    # visit If stmt
    def visitIf(self, ast: If, params):
        # scope: current environment
        # retType: function return type
        # inLoop: is this stmt in a loop or not (for break / continue)
        # funcName: function name
        scope, retType, inLoop, funcName = params
        # get expression type
        condType = self.visit(ast.expr, (scope, funcName))
        # raise error if expression is not Boolean type
        if type(condType) is not BoolType:
            raise TypeMismatchInStatement(ast)
        # get then stmt and else stmt
        stmt1 = [self.visit(ast.thenStmt, params)]
        stmt2 = None
        ret2 = None
        if not(ast.elseStmt is None):
            stmt2 = [self.visit(ast.elseStmt, params)]
            ret2 = Checker.handleReturnStmts(stmt2)

        # check if there is break or continue in these stmts
        ret1 = Checker.handleReturnStmts(stmt1)
        # ret2 = Checker.handleReturnStmts(stmt2)

        if ret1 is None or ret2 is None: 
            return (ast, None)
        if all([x not in [type(ret1), type(ret2)] for x in [Break, Continue]]): 
            return (ast, retType)
        return (ast, Break())

    # visit For stmt
    def visitFor(self, ast: For, params):
        scope, retType, inLoop, funcName = params
        # get expressions type
        exp1Type = self.visit(ast.expr1, (scope, funcName))
        exp2Type = self.visit(ast.expr2, (scope, funcName))
        exp3Type = self.visit(ast.expr3, (scope, funcName))
        # check expression type
        if (False in [type(x) is IntType for x in [exp1Type, exp3Type]]) or (type(exp2Type) is not BoolType):
            raise TypeMismatchInStatement(ast)
        # get stmt list
        stmt = [self.visit(ast.loop, (scope, retType, True, funcName))]
        # check for unreachable / get return stmt (if any)
        retType = Checker.handleReturnStmts(stmt)
        return (ast, None)

    # visit Do While stmt
    def visitDowhile(self, ast: Dowhile, params):
        scope, retType, inLoop, funcName = params
        # get condition expression 
        condType = self.visit(ast.exp, (scope, funcName))
        # check condition expression type
        if type(condType) is not BoolType:
            raise TypeMismatchInStatement(ast)
        # visit statement list
        stmt = [self.visit(x, (scope, retType, True, funcName)) for x in ast.sl]
        # check for unreachable / get return stmt
        retType = Checker.handleReturnStmts(stmt)
        return (ast, None)

    # visit Continue stmt
    def visitContinue(self, ast, params):
        scope, retType, inLoop, funcName = params
        if not inLoop: 
            raise ContinueNotInLoop()
        return (ast, Continue())

    # visit Break stmt
    def visitBreak(self, ast, params):
        scope, retType, inLoop, funcName = params
        if not inLoop:
            raise BreakNotInLoop()
        return (ast, Break())

    # visit Return stmt
    def visitReturn(self, ast: Return, params):
        scope, retType, inLoop, funcName = params
        if type(retType) is VoidType and ast.expr:
            raise TypeMismatchInStatement(ast)
        ret = self.visit(ast.expr, (scope, funcName)) if ast.expr else VoidType()
        if not Checker.matchType(retType, ret):
            raise TypeMismatchInStatement(ast)
        return (ast, ret)

    # visit func call
    def visitCallExpr(self, ast: CallExpr, params): 
        '''scope, retType, inLoop, funcName = params
        self.handleCall(ast, scope, funcName, Function())
        return (ast, None)'''
        # handle statement
        if len(params) == 4:
            scope, retType, inLoop, funcName = params
            self.handleCall(ast, scope, funcName, Function())
            return (ast, None)
        # handle expression
        else: 
            scope, funcName = params
            symbol = self.handleCall(ast, scope, funcName, Function())
            return symbol.mtype.rettype

    def visitBinaryOp(self, ast: BinaryOp, params):
        # handle expression
        # return result type of the binary op
        if len(params) == 2:
            scope, funcName = params
            op = str(ast.op)
            lType = self.visit(ast.left, (scope, funcName))
            rType = self.visit(ast.right, (scope, funcName))
            # ['+', '-', '*', '/', '%', '>', '<', '>=', '<=']
            if ExpUtils.isOpForNumber(op):
                if ExpUtils.isNaNType(lType) or ExpUtils.isNaNType(rType):
                    raise TypeMismatchInExpression(ast)
                elif op in ['+', '-', '*', '/']:
                    if type(lType) == IntType and type(rType) == IntType:
                        return IntType()
                    else:
                        return ExpUtils.mergeNumberType(lType, rType)
                elif op == '%':
                    if FloatType in [type(lType), type(rType)]:
                        raise TypeMismatchInExpression(ast)
                    else:
                        return IntType()
                else:
                    return BoolType()
            # ['&&', '||']
            elif op in ['&&', '||']:
                if not(type(lType) == BoolType and type(rType) == BoolType):
                    return TypeMismatchInExpression(ast)
                else:
                    return BoolType()
            # ['==', '!=']
            elif op in ['==', '!=']:
                if (type(lType) == type(rType)) and (type(lType) not in [ArrayType, ArrayPointerType, VoidType]):
                    return BoolType()
                else:
                    raise TypeMismatchInExpression(ast)
            # ['=']
            elif op == '=':
                ### handle not left value
                
                ###
                if type(lType) == IntType and type(rType) == IntType:
                    return IntType()
                elif type(lType) == IntType and type(rType) == FloatType:
                    raise TypeMismatchInExpression(ast)
                elif type(lType) == FloatType and type(rType) in [IntType, FloatType]:
                    return FloatType()
                elif type(lType) == BoolType and type(rType) == BoolType:
                    return BoolType()
                else:
                    raise TypeMismatchInExpression(ast)
        else:
            scope, retType, inLoop, funcName = params
            op = str(ast.op)
            lType = self.visit(ast.left, (scope, funcName))
            rType = self.visit(ast.right, (scope, funcName))
            # ['+', '-', '*', '/', '%', '>', '<', '>=', '<=']
            if ExpUtils.isOpForNumber(op):
                if ExpUtils.isNaNType(lType) or ExpUtils.isNaNType(rType):
                    raise TypeMismatchInExpression(ast)
                elif op in ['+', '-', '*', '/']:
                    if type(lType) == IntType and type(rType) == IntType:
                        return (ast, None)
                    else:
                        return ExpUtils.mergeNumberType(lType, rType)
                elif op == '%':
                    if FloatType in [type(lType), type(rType)]:
                        raise TypeMismatchInExpression(ast)
                    else:
                        return (ast, None)
                else:
                    return (ast, None)
            # ['&&', '||']
            elif op in ['&&', '||']:
                if not(type(lType) == BoolType and type(rType) == BoolType):
                    return TypeMismatchInExpression(ast)
                else:
                    return (ast, None)
            # ['==', '!=']
            elif op in ['==', '!=']:
                if (type(lType) == type(rType)) and (type(lType) not in [ArrayType, ArrayPointerType, VoidType]):
                    return (ast, None)
                else:
                    raise TypeMismatchInExpression(ast)
            # ['=']
            elif op == '=':
                ### handle not left value

                ###
                if type(lType) == IntType and type(rType) == IntType:
                    return (ast, None)
                elif type(lType) == IntType and type(rType) == FloatType:
                    raise TypeMismatchInExpression(ast)
                elif type(lType) == FloatType and type(rType) in [IntType, FloatType]:
                    return (ast, None)
                elif type(lType) == BoolType and type(rType) == BoolType:
                    return (ast, None)
                else:
                    raise TypeMismatchInExpression(ast)


    # visit unary op
    def visitUnaryOp(self, ast: UnaryOp, params):
        # handle expression
        if len(params) == 2:
            scope, funcName = params
            op = str(ast.op)
            expType = self.visit(ast.body, (scope, funcName))
            if (op == '-' and ExpUtils.isNaNType(expType)) or (op == '!' and type(expType) is not BoolType):
                raise TypeMismatchInExpression(ast)
            return expType
        # handle expression statement
        else:
            scope, retType, inLoop, funcName = params
            op = str(ast.op)
            expType = self.visit(ast.body, (scope, funcName))
            if (op == '-' and ExpUtils.isNaNType(expType)) or (op == '!' and type(expType) is not BoolType):
                raise TypeMismatchInExpression(ast)
            return (ast, None)


    # visit Id
    def visitId(self, ast: Id, params):
        scope, funcName = params
        symbol = Checker.checkUndeclared(scope, ast.name, Identifier())
        return symbol.mtype

    # visit ArrayCell 
    def visitArrayCell(self, ast: ArrayCell, params):
        scope, funcName = params
        arrType = self.visit(ast.arr, params)
        idxType = self.visit(ast.idx, params)
        if type(idxType) is not IntType or type(arrType) not in [ArrayType, ArrayPointerType]:
            raise TypeMismatchInExpression(ast)
        return arrType.eleType

    # handle a function call
    def handleCall(self, ast, scope, funcName, kind):
        symbol = Checker.checkUndeclared(scope, ast.method.name, Function())
        paramType = [self.visit(x, (scope, funcName)) for x in ast.param]
        if not Checker.checkParamType(symbol.mtype.partype, paramType):
            raise TypeMismatchInExpression(ast)
        Graph.add(funcName, ast.method.name)
        return symbol

    def visitIntLiteral(self, ast, params): 
        return IntType()

    def visitFloatLiteral(self, ast, params):
        return FloatType()

    def visitBooleanLiteral(self, ast, params):
        return BoolType()

    def visitStringLiteral(self, ast, params):
        return StringType()
    

