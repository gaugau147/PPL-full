# Student ID: 1820047
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import *


class MType:
    def __init__(self, partype, rettype):
        # Parameter type: list(Type)
        self.partype = partype

        # Return type
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
    def mergeNumberType(leftType, rightType):
        return (FloatType(), False) if FloatType in [type(x) for x in [leftType, rightType]] else (IntType(), False)


class Symbol:
    def __init__(self, name, mtype, value=None, kind=Function(), globalScope=False):
        # Name of symbol: string
        self.name = name

        # Type of symbol: MType | ArrayType | PrimitiveType
        self.mtype = mtype

        # Value of symbol
        self.value = value

        # Kind of symbol: Function() | Parameter() | Variable()
        self.kind = kind

        # Scope of symbol: True | False
        self.globalScope = globalScope

    def __str__(self):
        return 'Symbol( ' + str(self.name) + "," + str(self.mtype) + "," + str(self.value) + ')'

    def getKind(self):
        return self.kind if type(self.mtype) is MType else Identifier()

    def nameKind(self):
        return (str(self.name), type(self.getKind()))

    def nameType(self):
        return (str(self.name), str(self.mtype))

    def kindToParam(self):
        self.kind = Parameter()
        return self

    def kindToVar(self):
        self.kind = Variable()
        return self

    def scopeToGlobal(self):
        self.globalScope = True
        return self

    @staticmethod
    def nameToString(symbol):
        return str(symbol.name)

    @staticmethod
    def isSymbolVarDecl(decl):
        return Symbol(decl.variable, decl.varType, kind=Variable())

    @staticmethod
    def isSymbolFuncDecl(decl):
        paramType = [x.varType for x in decl.param]
        return Symbol(decl.name.name, MType(paramType, decl.returnType), kind=Function())

    @staticmethod
    def symbolDecl(decl):
        return Symbol.isSymbolVarDecl(decl) if type(decl) is VarDecl else Symbol.isSymbolFuncDecl(decl)

    @staticmethod
    def symbolVarDecl(decl):
        if type(decl) is VarDecl:
            return Symbol.isSymbolVarDecl(decl)
        else:
            return None

    @staticmethod
    def symbolFuncDecl(decl):
        if type(decl) is FuncDecl:
            return Symbol.isSymbolFuncDecl(decl)
        else:
            return None


###################### Scope ###############################
class Scope:
    @staticmethod
    def isExistent(lstSyms, sym):
        return len([x for x in lstSyms if str(x.name) == str(sym.name)]) > 0

    @staticmethod
    def merge(currentScope, comingScope):
        # merge the local scope into the global scope
        # check if a symbol is in global scope yet
        return reduce(lambda lst, sym: lst if Scope.isExistent(lst, sym) else lst+[sym], currentScope, comingScope)


############################## Checker ################################
class Checker(Utils):

    '''
    class Utils:
        def lookup(self,name,lst,func):
            for x in lst:
                if name == func(x):
                    return x
            return None
    '''

    utilsModule = Utils()

    @staticmethod
    def checkRedecl(currentScope, newLstSym):
        scope = currentScope.copy()
        for x in newLstSym:
            f = Checker.utilsModule.lookup(
                Symbol.nameToString(x), scope, Symbol.nameToString)
            if f is not None:
                raise Redeclared(x.kind, x.name)
            scope.append(x)
        return scope

    @staticmethod
    def checkUndecl(visibleScope, name, kind, notGlobalScope=False):
        if visibleScope is not notGlobalScope:
            scope = visibleScope
        else:
            scope = [x for x in visibleScope if not x.globalScope]
        res = Checker.utilsModule.lookup((str(name), type(kind)),
                                         scope, lambda x: x.nameKind())
        if res is None:
            raise Undeclared(kind, name)
        return res

    ####### Edit Here ###########
    @staticmethod
    def matchArrayType(a, b):
        return type(a.eleType) == type(b.eleType)

    ####### Edit Here ###########
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


################################# Graph Structure ############################


class Graph:
    # an object Graph has 3 dictionary attibutes
    link = {}  # { 'n1': ['n2', 'n3'], 'n2': [], 'n3': ['n1', 'n2'] }
    visited = {}  # { 'n1': True, 'n2': False, 'n3': False }
    invoked = {}  # { 'n1': True, 'n2': False, 'n3': False }

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
            Graph.invoked[v] = True  # v is invoked by u

    @staticmethod
    def deptFirstSearch(u):
        # set u is visited
        u = str(u)
        Graph.visited[u] = True
        # set v is visited
        [Graph.deptFirstSearch(v)
         for v in Graph.link[u] if not Graph.visited[v]]

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

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType())),
        Symbol("putInt", MType([IntType()], VoidType())),
        Symbol("getFloat", MType([], FloatType())),
        Symbol("putFloat", MType([FloatType()], VoidType())),
        Symbol("putFloatLn", MType([FloatType()], VoidType())),
        Symbol("putBool", MType([BoolType()], VoidType())),
        Symbol("putBoolLn", MType([BoolType()], VoidType())),
        Symbol("putString", MType([StringType()], VoidType())),
        Symbol("putStringLn", MType([StringType()], VoidType())),
        Symbol("putLn", MType([], VoidType()))
    ]

    def __init__(self, ast):
        # print(ast)
        # print(ast)
        # print()
        self.ast = ast

    def check(self):
        Graph.initialize()
        return self.visit(self.ast, StaticChecker.global_envi)

    # def visitProgram(self, ast, c):
        # return [self.visit(x, c) for x in ast.decl]

    def visitProgram(self, ast, c):
        ast: Program

        # List of declarations including varDecl and FuncDecl
        lstSyms = [Symbol.symbolDecl(x).scopeToGlobal() for x in ast.decl]

        # List of function declarations
        lstFuncSyms = [Symbol.symbolFuncDecl(x) for x in ast.decl]

        scope = Checker.checkRedecl(c, lstSyms)

        # An example of entry point
        entry = Symbol("main", MType([], VoidType()), Function())

        # res = self.lookup(entry.nameType(), lstSyms, lambda x: x.nameType())
        # if res is None:
        #     raise NoEntryPoint()

        # Check if there is an entry point
        res = self.lookup(str(entry.name), lstSyms,
                          lambda x: x.nameToString(x))
        if res is None:
            raise NoEntryPoint()

        lstFuncDecl = c + [entry] + [Symbol.symbolDecl(x)
                                     for x in ast.decl if type(x) is FuncDecl]

        for x in lstFuncDecl:
            Graph.add(x.name)

        Graph.setDefaultVisitedNodes([u.name for u in c])

        for x in ast.decl:
            self.visit(x, scope)

        Graph.deptFirstSearch("main")
        unreachableNode = Graph.getUnreachableNode()
        if unreachableNode is not None:
            sym = self.lookup(unreachableNode, lstFuncDecl,
                              Symbol.nameToString)
            raise UnreachableFunction(symbol.name)
        return None

    # def visitFuncDecl(self, ast, c):
    #     return list(map(lambda x: self.visit(x, (c, True)), ast.body.member))

    def visitFuncDecl(self, ast, c):
        ast: FuncDecl

        lstParams = [self.visit(x, c).kindToParam() for x in ast.param]

        lstVars = [self.visit(x, c).kindToVar()
                   for x in ast.body.member if type(x) is VarDecl]

        lstCombineSyms = lstParams + lstVars

        localScope = Checker.checkRedecl([], lstCombineSyms)

        scope = Scope.merge(c, localScope)

        lstStmts = [self.visit(x, (scope, ast.returnType, False, ast.name.name))
                    for x in ast.body.member if not(type(x) is VarDecl)]

        retType = Checker.handleReturnStmts(lstStmts)

        if Checker.isReturnTypeFunction(ast.returnType) and not Checker.isReturnTypeFunction(retType):
            raise FunctionNotReturn(ast.name.name)

    def visitVarDecl(self, ast, c):
        return Symbol.isSymbolVarDecl(ast)

    def visitBlock(self, ast, c):
        ast: Block

        _scope, retType, isInLoop, funcName = c

        lstVars = [self.visit(x, _scope).kindToVar()
                   for x in ast.member if type(x) is VarDecl]

        localScope = Checker.checkRedecl([], lstVars)

        scope = Scope.merge(_scope, localScope)

        lstStmts = [self.visit(x, (scope, retType, isInLoop, funcName))
                    for x in ast.member if not(type(x) is VarDecl)]

        Checker.handleReturnStmts(lstStmts)

        return (ast, None)

    def visitIf(self, ast, c):
        ast: If

        _scope, retType, isInLoop, funcName = c

        condiType = self.visit(ast.expr, (_scope, funcName))[0]

        if type(condiType) is not BoolType:
            raise TypeMismatchInStatement(ast)

        lstThenStmts = [self.visit(ast.thenStmt, c)]
        lstElseStmts = None
        elseRet = None

        if not(ast.elseStmt is None):
            lstElseStmts = [self.visit(ast.elseStmt, c)]
            elseRet = Checker.handleReturnStmts(lstElseStmts)

        thenRet = Checker.handleReturnStmts(lstThenStmts)

        if thenRet is None or elseRet is None:
            return (ast, None)

        if all([x not in [type(elseRet), type(thenRet)] for x in [Break, Continue]]):
            return (ast, retType)

        return (ast, Break())

    def visitFor(self, ast, c):
        ast: For

        _scope, retType, isInLoop, funcName = c

        symbol = Checker.checkUndecl(
            _scope, ast.id.name, Identifier(), notGlobalScope=True)
        exprTypeOne = self.visit(ast.expr1, (scope, funcName))[0]
        exprTypeTwo = self.visit(ast.expr2, (scope, funcName))[0]
        exprTypeThree = self.visit(ast.expr3, (scope, funcName))[0]

        if False in [type(x) is IntType for x in [exprTypeOne, exprTypeThree]] or (type(exprTypeTwo) is not BoolType):
            raise TypeMismatchInStatement(ast)

        lstStmts = [self.visit(ast.loop, (_scope, retType, True, funcName))]

        Checker.handleReturnStmts(lstStmts)

        return (ast, None)

    # visit Do While stmt
    def visitDowhile(self, ast: Dowhile, c):
        _scope, retType, inLoop, funcName = c
        condiType = self.visit(ast.exp, (_scope, funcName))[0]
        if type(condiType) is not BoolType:
            raise TypeMismatchInStatement(ast)
        lstStmts = [self.visit(x, (_scope, retType, True, funcName))
                    for x in ast.sl]
        retType = Checker.handleReturnStmts(lstStmts)
        return (ast, None)

    def visitContinue(self, ast, c):
        ast: Continue

        _scope, retType, isInLoop, funcName = c
        if not isInLoop:
            raise ContinueInLoop()
        return (ast, Continue())

    def visitBreak(self, ast, c):
        ast: Break

        _scope, retType, isInLoop, funcName = c
        if not isInLoop:
            raise BreakNotInLoop()
        return (ast, Break())

    def visitReturn(self, ast, c):
        ast: Return

        _scope, retType, isInLoop, funcName = c
        if type(retType) is VoidType and ast.expr:
            raise TypeMismatchInStatement(ast)
        ret = self.visit(ast.expr, (_scope, funcName)
                         )[0] if ast.expr else VoidType()
        if not Checker.matchType(retType, ret):
            raise TypeMismatchInStatement(ast)
        return (ast, ret)

    def visitCallExpr(self, ast, c):
        ast: CallExpr

        if len(c) == 4:
            _scope, retType, isInLoop, funcName = c
            self.handleCall(ast, _scope, funcName, Function())
            return (ast, none)
        else:
            _scope, funcName = c
            symbol = self.handleCall(ast, _scope, funcName, Function())
            return (symbol.mtype.rettype, False)

    def visitBinaryOp(self, ast: BinaryOp, c):
        # handle expression
        # return result type of the binary op
        if len(c) == 2:
            _scope, funcName = c
            operator = str(ast.op)
            leftType = self.visit(ast.left, (_scope, funcName))[0]
            rightType = self.visit(ast.right, (_scope, funcName))[0]
            # ['+', '-', '*', '/', '%', '>', '<', '>=', '<=']
            if ExpCheck.isOpForNumber(operator):
                if ExpCheck.isNaNType(leftType) or ExpCheck.isNaNType(rightType):
                    raise TypeMismatchInExpression(ast)
                elif operator in ['+', '-', '*', '/']:
                    if type(leftType) == IntType and type(rightType) == IntType:
                        return (IntType(), False)
                    else:
                        return ExpCheck.mergeNumberType(leftType, rightType)
                elif operator == '%':
                    if FloatType in [type(leftType), type(rightType)]:
                        raise TypeMismatchInExpression(ast)
                    else:
                        return (IntType(), False)
                else:
                    return (BoolType(), False)
            # ['&&', '||']
            elif operator in ['&&', '||']:
                if not(type(leftType) == BoolType and type(rightType) == BoolType):
                    return TypeMismatchInExpression(ast)
                else:
                    return (BoolType(), False)
            # ['==', '!=']
            elif operator in ['==', '!=']:
                if (type(leftType) == type(rightType)) and (type(leftType) not in [ArrayType, ArrayPointerType, VoidType]):
                    return (BoolType(), False)
                else:
                    raise TypeMismatchInExpression(ast)
            # ['=']
            elif operator == '=':
                # handle not left value
                isLeft = self.visit(ast.left, (_scope, funcName))[1]
                if isLeft == False:
                    raise NotLeftValue(ast.left)
                ###
                if type(leftType) == IntType and type(rightType) == IntType:
                    return (IntType(), False)
                elif type(leftType) == IntType and type(rightType) == FloatType:
                    raise TypeMismatchInExpression(ast)
                elif type(leftType) == FloatType and type(rightType) in [IntType, FloatType]:
                    return (FloatType(), False)
                elif type(leftType) == BoolType and type(rightType) == BoolType:
                    return (BoolType(), False)
                elif type(lType) == StringType and type(rType) == StringType:
                    return (StringType(), False)
                else:
                    raise TypeMismatchInExpression(ast)
        # handle stmt
        else:
            scope, retType, inLoop, funcName = c
            operator = str(ast.op)
            leftType = self.visit(ast.left, (_scope, funcName))[0]
            rightType = self.visit(ast.right, (_scope, funcName))[0]
            # ['+', '-', '*', '/', '%', '>', '<', '>=', '<=']
            if ExpCheck.isOpForNumber(operator):
                if ExpCheck.isNaNType(leftType) or ExpCheck.isNaNType(rightType):
                    raise TypeMismatchInExpression(ast)
                elif operator in ['+', '-', '*', '/']:
                    if type(leftType) == IntType and type(rightType) == IntType:
                        return (ast, None)
                    else:
                        return ExpCheck.mergeNumberType(leftType, rightType)
                elif operator == '%':
                    if FloatType in [type(leftType), type(rightType)]:
                        raise TypeMismatchInExpression(ast)
                    else:
                        return (ast, None)
                else:
                    return (ast, None)
            # ['&&', '||']
            elif operator in ['&&', '||']:
                if not(type(leftType) == BoolType and type(rightType) == BoolType):
                    return TypeMismatchInExpression(ast)
                else:
                    return (ast, None)
            # ['==', '!=']
            elif operator in ['==', '!=']:
                if (type(leftType) == type(rightType)) and (type(leftType) not in [ArrayType, ArrayPointerType, VoidType]):
                    return (ast, None)
                else:
                    raise TypeMismatchInExpression(ast)
            # ['=']
            elif operator == '=':
                # handle not left value
                isLeft = self.visit(ast.left, (_scope, funcName))[1]
                if isLeft == False:
                    raise NotLeftValue(ast.left)
                ###
                if type(leftType) == IntType and type(rightType) == IntType:
                    return (ast, None)
                elif type(leftType) == IntType and type(rightType) == FloatType:
                    raise TypeMismatchInExpression(ast)
                elif type(leftType) == FloatType and type(rightType) in [IntType, FloatType]:
                    return (ast, None)
                elif type(leftType) == BoolType and type(rightType) == BoolType:
                    return (ast, None)
                else:
                    raise TypeMismatchInExpression(ast)

    # visit unary op

    def visitUnaryOp(self, ast, c):
        ast: UnaryOp

        if len(c == 2):
            _scope, funcName = c
            operator = str(ast.op)
            expType = self.visit(ast.body, (_scope, funcName))[0]
            if (operator == '-' and ExpUtils.isNaNType(expType)) or (operator == '!' and type(expType) is not BoolType):
                raise TypeMismatchInExpression(ast)
            return (expType, True)
        else:
            _scope, retType, isInLoop, funcName = c
            operator = str(ast.op)
            expType = self.visit(ast.body, (_scope, funcName))[0]
            if (operator == '-' and ExpUtils.isNaNType(expType)) or (operator == '!' and type(expType) is not BoolType):
                raise TypeMismatchInExpression(ast)
            return (ast, None)

    # visit Id
    def visitId(self, ast, c):
        ast: Id

        _scope, funcName = c
        symbol = Checker.checkUndeclared(_scope, ast.name, Identifier())
        return (symbol.mtype, True)

    # visit ArrayCell
    def visitArrayCell(self, ast: ArrayCell, c):
        ast: ArrayCell

        _scope, funcName = c
        arrType = self.visit(ast.arr, (_scope, c))
        idxType = self.visit(ast.idx, (_scope, c))
        if type(idxType) is not IntType or type(arrType) is not ArrayType or type(arrType) is not ArrayPointerType:
            raise TypeMismatchInExpression(ast)
        return (arrType.eleType, True)

    # handle a function call
    def handleCall(self, ast, scope, funcName, kind):
        symbol = Checker.checkUndecl(scope, ast.method.name, Function())
        paramType = [self.visit(x, (scope, funcName))[0] for x in ast.param]
        if not Checker.checkParamType(symbol.mtype.partype, paramType):
            raise TypeMismatchInExpression(ast)
        Graph.add(funcName, ast.method.name)
        return symbol

    def visitIntLiteral(self, ast, c):
        return (IntType(), False)

    def visitFloatLiteral(self, ast, c):
        return (FloatType(), False)

    def visitBooleanLiteral(self, ast, c):
        return (BoolType(), False)

    def visitStringLiteral(self, ast, c):
        return (StringType(), False)

    # def visitCallExpr(self, ast, c):
    #     at = [self.visit(x, (c[0], False)) for x in ast.param]

    #     res = self.lookup(ast.method.name, c[0], lambda x: x.name)
    #     if res is None or not type(res.mtype) is MType:
    #         raise Undeclared(Function(), ast.method.name)
    #     elif len(res.mtype.partype) != len(at):
    #         if c[1]:
    #             raise TypeMismatchInStatement(ast)
    #         else:
    #             raise TypeMismatchInExpression(ast)
    #     else:
    #         return res.mtype.rettype

    # def visitIntLiteral(self, ast, c):
    #     return IntType()
