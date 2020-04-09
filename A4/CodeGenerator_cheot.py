'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
import sys
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from Visitor import BaseVisitor
from AST import *

sys.path.append('../utils')
sys.path.append('../checker')


class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("getInt", MType([], IntType()), CName(self.libName)),
            Symbol("putIntLn", MType([IntType()],VoidType()), CName(self.libName)),
            Symbol("putInt", MType([IntType()],VoidType()), CName(self.libName)),
            Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
            Symbol("putFloat", MType([FloatType()],VoidType()), CName(self.libName)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
            Symbol("putBool", MType([BoolType()],VoidType()), CName(self.libName)),
            Symbol("putBoolLn", MType([BoolType()],VoidType()), CName(self.libName)),
            Symbol("putString", MType([StringType()],VoidType()), CName(self.libName)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
            Symbol("putLn", MType([], VoidType()), CName(self.libName))
        ]

    def gen(self, ast, dir_):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


class ClassType(Type):
    def __init__(self, cname):
        # cname: String
        self.cname = cname

    def __str__(self):
        return "ClassType"

    def accept(self, v, param):
        return v.visitClassType(self, param)


class SubBody():
    def __init__(self, frame, sym, isGlobal = False, isExpr = False):
        # frame: Frame
        # sym: List[Symbol]

        self.frame = frame
        self.sym = sym
        self.isGlobal = isGlobal
        self.isExpr = isExpr


class Access():
    def __init__(self, frame, sym, isLeft, isFirst, checkArrayType = False, getLeft = False):
        # frame: Frame
        # sym: List[Symbol]
        # isLeft: Boolean
        # isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
        self.checkArrayType = checkArrayType
        self.getLeft = getLeft


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        # value: Int

        self.value = value


class CName(Val):
    def __init__(self, value):
        # value: String

        self.value = value

class StupidUtils:
    @staticmethod
    def isOpForNumberToNumber(operator):
        return str(operator) in ['+', '-', '*', '/', '%']

    @staticmethod
    def isOpForNumberToBoolean(operator):
        return str(operator) in ['!=', '==', '>', '<', '>=', '<=']

    @staticmethod
    def isOpForNumber(operator):
        return StupidUtils.isOpForNumberToNumber(operator) or StupidUtils.isOpForNumberToBoolean(operator)

    @staticmethod
    def mergeNumberType(lType, rType):
        return FloatType() if FloatType in [type(x) for x in [lType, rType]] else IntType()

    @staticmethod
    def retrieveType(originType):
        if type(originType) is ArrayType: return ArrayPointerType(originType.eleType)
        return originType


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        # astTree: AST
        # env: List[Symbol]
        # dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
            # not in original version
        self.listGlobalArray = [] # list(VarDecl: array declare global)


    def visitProgram(self, ast, c):
        # ast: Program
        # c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        ###################################################################################
        staticDecl = self.env
        for x in ast.decl:
            if type(x) is FuncDecl:
                partype = [i.varType for i in x.param]
                staticDecl = [Symbol(x.name.name.lower(), MType(
                    partype, x.returnType), CName(self.className))] + staticDecl
            else:
                newSym = self.visit(x, SubBody(None, None, isGlobal=True))
                staticDecl = [newSym] + staticDecl

        e = SubBody(None, staticDecl)

        # visit ast tree
        for x in ast.decl:
            if type(x) is FuncDecl:
                e = self.visit(x, e)

        ###################################################################################

        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), [], None, Block([])), c, Frame("<init>", VoidType))
        self.genMETHOD(FuncDecl(Id("<clinit>"), [], None, Block([])), c, Frame("<clinit>", VoidType))
        self.emit.emitEPILOG()
        return c

    def visitVarDecl(self, ast: VarDecl, o: SubBody):
        subctxt = o
        frame = o.frame
        isGlobal = o.isGlobal
        varName = ast.variable
        varType = ast.varType
        if isGlobal:
            self.emit.printout(self.emit.emitATTRIBUTE(varName, StupidUtils.retrieveType(varType), False, ""))
            if type(ast.varType) is ArrayType: 
                self.listGlobalArray.append(ast)
            return Symbol(varName, varType)
        # params
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, varName, StupidUtils.retrieveType(varType), frame.getStartLabel(), frame.getEndLabel(), frame))
        return SubBody(frame, [Symbol(varName, varType, Index(idx))] + subctxt.sym)

    def genMETHOD(self, consdecl: FuncDecl, o, frame: Frame):
        # o: Any

        glenv = o

        methodName = consdecl.name.name

        isInit = consdecl.returnType is None and methodName == "<init>"
        isClassInit = consdecl.returnType is None and methodName == "<clinit>"
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit or isClassInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else [StupidUtils.retrieveType(x.varType) for x in consdecl.param]
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        # glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(
                StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        # listParamArray = [] # list(Symbol(name, mtype, value: Index(idx)))
        # listLocalArray = [] # list(Symbol(name, mtype, value: Index(idx)))
        paramList = SubBody(frame, glenv)

        for x in consdecl.param:
            paramList = self.visit(x, paramList)
            if type(x.varType) is ArrayType:
                listParamArray.append(paramList.sym[0])

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        # # Init global array declare
        # if isClassInit:
        #     for x in self.listGlobalArray:
        #         size = x.varType.upper - x.varType.lower + 1
        #         self.emit.printout(self.emit.emitInitNewStaticArray(self.className + "/" + x.variable.name, size, x.varType.eleType, frame))

        # # Init local array declare
        # for sym in listLocalArray:
        #     index = sym.value.value
        #     varType = sym.mtype
        #     size = varType.upper - varType.lower + 1
        #     self.emit.printout(self.emit.emitInitNewLocalArray(index, size, varType.eleType, frame))

        # # Clone params array
        # for sym in listParamArray:
        #     index = sym.value.value
        #     eleType = sym.mtype.eleType
        #     self.emit.printout(self.emit.emitCloneArray(index, eleType, frame))

        # for x in o:
        #     print(x)

        # visit block member
        # list(map(lambda x: self.visit(x, SubBody(frame, paramList.sym)), consdecl.body.member))
        self.visit(consdecl.body, SubBody(frame, paramList.sym))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitBlock(self, ast: Block, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym

        listLocalArray = [] # list(Symbol(name, mtype, value: Index(idx)))

        hasReturnStmt = False
        for x in ast.member:
            if type(x) is VarDecl:
                # var decl
                ctxt = self.visit(x, ctxt)
                symbols = ctxt.sym
                # handle array variable
                if type(x.varType) is ArrayType:
                    index = ctxt.sym[0].value.value
                    varType = ctxt.sym[0].mtype
                    size = varType.dimen
                    self.emit.printout(self.emit.emitInitNewLocalArray(index, size, varType.eleType, frame))
            else:
                # statement
                e = SubBody(frame, symbols)
                if self.visit(x, e) == True:
                    hasReturnStmt = True
        return hasReturnStmt

    def visitCallExpr(self, ast: CallExpr, o):
        # call statement
        if type(o) is SubBody:
            ctxt = o
            frame = ctxt.frame
            nenv = ctxt.sym
            sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
            cname = sym.value.value

            ctype = sym.mtype
            paramType = ctype.partype

            paramsCode = ""
            idx = 0
            for x in ast.param:
                pCode, pType = self.visit(x, Access(frame, nenv, False, True))
                if type(paramType[idx]) is FloatType and type(pType) is IntType:
                    pCode = pCode + self.emit.emitI2F(frame)
                if type(paramType[idx]) is ArrayType:
                    pass
                paramsCode = paramsCode + pCode
                idx = idx + 1
        
            code = paramsCode + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame) 
            self.emit.printout(code)

            # idx = 0
            # in_ = ("", [])
            # for x in ast.param:
            #     pCode, pType = self.visit(x, Access(frame, nenv, False, True))
            #     if type(paramType[idx]) is FloatType and type(pType) is IntType:
            #         pCode = pCode + self.emit.emitI2F(frame)
            #     in_ = (in_[0] + pCode, in_[1].append(pType))
            #     idx = idx + 1

            # code = in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame)
            # self.emit.printout(code)
        else:
            # call expression
            ctxt = o
            frame = ctxt.frame
            nenv = ctxt.sym
            sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
            cname = sym.value.value

            ctype = sym.mtype
            paramType = ctype.partype


            paramsCode = ""
            idx = 0
            for x in ast.param:
                pCode, pType = self.visit(x, Access(frame, nenv, False, True))
                if type(paramType[idx]) is FloatType and type(pType) is IntType:
                    pCode = pCode + self.emit.emitI2F(frame)
                if type(paramType[idx]) is ArrayType:
                    pass
                paramsCode = paramsCode + pCode
                idx = idx + 1
        
            code = paramsCode + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame) 
            return code, ctype.rettype

            # idx = 0
            # in_ = ("", [])
            # for x in ast.param:
            #     print(len(ast.param))
            #     pCode, pType = self.visit(x, Access(frame, nenv, False, True))
            #     if type(paramType[idx]) is FloatType and type(pType) is IntType:
            #         pCode = pCode + self.emit.emitI2F(frame)
            #     in_ = (in_[0] + pCode, in_[1].append(pType))
            #     idx = idx + 1

            # code = in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame)
            # return code, ctype.rettype

    def visitIf(self, ast: If, o: SubBody):
        # ctxt = o
        # frame = ctxt.frame
        # nenv = ctxt.sym
        # # [print(x) for x in nenv]
        # expCode, expType = self.visit(ast.expr, Access(frame, nenv, False, True))
        # self.emit.printout(expCode)

        # labelT = frame.getNewLabel() # eval is true
        # labelE = frame.getNewLabel() # label end

        # self.emit.printout(self.emit.emitIFTRUE(labelT, frame)) # false
        # # False
        # self.visit(ast.elseStmt, ctxt)
        # self.emit.printout(self.emit.emitGOTO(labelE, frame)) # go to end
        # # True
        # self.emit.printout(self.emit.emitLABEL(labelT, frame))
        # self.visit(ast.thenStmt, ctxt)
        # # End
        # self.emit.printout(self.emit.emitLABEL(labelE, frame))
        # return False

        ######################################################################
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        expCode, expType = self.visit(ast.expr, Access(frame, nenv, False, True))
        self.emit.printout(expCode)
        if ast.elseStmt:
            labelT = frame.getNewLabel() # eval is true
            labelE = frame.getNewLabel() # label end

            self.emit.printout(self.emit.emitIFTRUE(labelT, frame)) # false
            # False
            hasReturnStmt = True in [self.visit(ast.elseStmt, ctxt)]
            if not hasReturnStmt:
                    self.emit.printout(self.emit.emitGOTO(labelE, frame)) # go to end
            # True
            self.emit.printout(self.emit.emitLABEL(labelT, frame))
            hasReturnStmt = True in [self.visit(ast.thenStmt, ctxt)] and hasReturnStmt
            # End
            self.emit.printout(self.emit.emitLABEL(labelE, frame))
            return hasReturnStmt
        else:
            labelT = frame.getNewLabel() # eval is true
            labelE = frame.getNewLabel() # label end

            self.emit.printout(self.emit.emitIFTRUE(labelT, frame)) # false
            self.emit.printout(self.emit.emitGOTO(labelE, frame)) # go to end
            # True
            self.emit.printout(self.emit.emitLABEL(labelT, frame))
            hasReturnStmt = True in [self.visit(ast.thenStmt, ctxt)] and hasReturnStmt
            # End
            self.emit.printout(self.emit.emitLABEL(labelE, frame))
            return hasReturnStmt

    def visitDowhile(self, ast: Dowhile, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        expCode, expType = self.visit(ast.exp, Access(frame, nenv, False, True))
        
        # do statement once before go in loop
        frame.enterLoop()
        [self.visit(x, o) for x in ast.sl]
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

        labelS = frame.getNewLabel() # label start
        labelE = frame.getNewLabel() # label end
        # enter loop
        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelS, frame))
        self.emit.printout(expCode)
        self.emit.printout(self.emit.emitIFFALSE(labelE, frame))
        hasReturnStmt = True in [self.visit(x, o) for x in ast.sl]
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelS, frame)) # loop
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

        # def visitBreak(self, ast: Break, o: SubBody):
        # ctxt = o
        # frame = ctxt.frame
        # return self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))


    def visitFor(self, ast: For, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        exp2Code, _ = self.visit(ast.expr2, Access(frame, nenv, False, True))
        
        labelS = frame.getNewLabel() # label start
        labelE = frame.getNewLabel() # label end

        # Init value
        self.visit(ast.expr1, SubBody(frame, nenv))
        frame.enterLoop()
        # Loop
        self.emit.printout(self.emit.emitLABEL(labelS, frame))
        # 1. Condition
        self.emit.printout(exp2Code)
        self.emit.printout(self.emit.emitIFFALSE(labelE, frame))
        # 2. Statements
        hasReturnStmt = True in [self.visit(ast.loop, ctxt)]
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        # 3. Update index
        self.visit(ast.expr3, SubBody(frame, nenv))

        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelS, frame)) # loop
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitReturn(self, ast: Return, o: SubBody):

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        retType = frame.returnType

        if not type(retType) is VoidType:
            expCode, expType = self.visit(ast.expr, Access(frame, nenv, False, True))
            if type(retType) is FloatType and type(expType) is IntType:
                expCode = expCode + self.emit.emitI2F(frame)
            self.emit.printout(expCode)
        self.emit.printout(self.emit.emitRETURN(retType, frame))
        return True

    def visitBreak(self, ast: Break, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        return self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinue(self, ast: Continue, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        return self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

    #################### Expression ######################
    def visitId(self, ast: Id, o: Access):
        # Return (name, type, index)
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym
        isLeft = ctxt.isLeft
        isFirst = ctxt.isFirst


        if isLeft and ctxt.checkArrayType:
            return False, None

        sym = self.lookup(ast.name, symbols, lambda x: x.name)

        # recover status of stack in frame
        if not isFirst and isLeft: 
            frame.push()
        elif not isFirst and not isLeft: 
            frame.pop()

        isArrayType = type(sym.mtype) is ArrayType
        emitType = StupidUtils.retrieveType(sym.mtype)
        if sym.value is None: # not index -> global var - static field
            if isLeft and not isArrayType:
                retCode = self.emit.emitPUTSTATIC(self.className + "/" + sym.name, emitType, frame)
            else:
                retCode = self.emit.emitGETSTATIC(self.className + "/" + sym.name, emitType, frame)
        else:
            if isLeft and not isArrayType:
                retCode = self.emit.emitWRITEVAR(sym.name, emitType, sym.value.value, frame)
            else:
                retCode = self.emit.emitREADVAR(sym.name, emitType, sym.value.value, frame)

        return retCode, sym.mtype

    
    def visitArrayCell(self, ast: ArrayCell, o: Access):
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym
        isLeft = ctxt.isLeft
        isFirst = ctxt.isFirst

        if isLeft and ctxt.checkArrayType: return True, None

        arrCode, arrType = self.visit(ast.arr, Access(frame, symbols, True, True))
        idxCode, idxType = self.visit(ast.idx, Access(frame, symbols, False, True))
        # update index jvm, i.e [3..5] -> [0..2], access [4] -> [1]
        # idxCode = idxCode + self.emit.emitPUSHICONST(arrType.lower, frame) + self.emit.emitADDOP('-', IntType(), frame)
        # Steps: aload(address index) -> iconst(access index) -> iaload
        if isLeft:
            return [arrCode + idxCode, self.emit.emitASTORE(arrType.eleType, frame)], arrType.eleType
        return arrCode + idxCode + self.emit.emitALOAD(arrType.eleType, frame), arrType.eleType
        

    def visitBinaryOp(self, ast: BinaryOp, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        op = str(ast.op)
            
        if StupidUtils.isOpForNumber(op): # for number type
            lCode, lType = self.visit(ast.left, ctxt)
            rCode, rType = self.visit(ast.right, ctxt)
            mType = StupidUtils.mergeNumberType(lType, rType)
            # if op == '/': 
            #     mType = FloatType() # mergeType >= lType, rType
            if type(lType) is IntType and type(mType) != type(lType):
                lCode = lCode + self.emit.emitI2F(frame)
            if type(rType) is IntType and type(mType) != type(rType):
                rCode = rCode + self.emit.emitI2F(frame)
            if StupidUtils.isOpForNumberToNumber(op):
                if op in ['+', '-']:
                    return lCode + rCode + self.emit.emitADDOP(op, mType, frame), mType
                if op in ['*', '/']:
                    return lCode + rCode + self.emit.emitMULOP(op, mType, frame), mType
                if op == '%':
                    return lCode + rCode + self.emit.emitMOD(frame), mType
            else: # op to boolean: > <= == !=, ...
                return lCode + rCode + self.emit.emitREOP(op, mType, frame), BoolType()
        elif op == '=':
            if type(o) is Access:
                # print("access")
                isArray, _ = self.visit(ast.left, Access(frame, nenv, True, True, True))

                if not isArray:
                    expCode, expType = self.visit(ast.right, Access(frame, nenv, False, True))
                    lhsCode, lhsType = self.visit(ast.left, Access(frame, nenv, True, True))

                    if type(lhsType) is FloatType and type(expType) is IntType:
                        expCode = expCode + self.emit.emitI2F(frame)
                    self.emit.printout(expCode + self.emit.emitDUP(frame) + lhsCode)
                    return "",expType
                else:
                    for i in range(0, 2): frame.push()

                    # handle array
                    if o.getLeft == False:
                        # print("right")
                        expCode, expType = self.visit(ast.right, Access(frame, nenv, False, True, False, False))
                        lhsCode, lhsType = self.visit(ast.left, Access(frame, nenv, True, True))

                        if type(lhsType) is FloatType and type(expType) is IntType:
                            expCode = expCode + self.emit.emitI2F(frame)
                        self.emit.printout(lhsCode[0])
                        for i in range(0, 2): frame.push()
                        return expCode, expType
                    elif o.getLeft == True:
                        # print("left")
                        expCode, expType = self.visit(ast.right, Access(frame, nenv, False, True, False, True))
                        lhsCode, lhsType = self.visit(ast.left, Access(frame, nenv, True, True))

                        if type(lhsType) is FloatType and type(expType) is IntType:
                            expCode = expCode + self.emit.emitI2F(frame)
                        self.emit.printout(self.emit.emitDUPX2(frame) + lhsCode[1])
                        for i in range(0, 2): frame.push()
                        return None, None
            else:
                # print("subbody")
                isArray, _ = self.visit(ast.left, Access(frame, nenv, True, True, True))

                if isArray:
                    # handle array
                    for i in range(0, 2): frame.push()

                    lhsCode, lhsType = self.visit(ast.left, Access(frame, nenv, True, True))
                    expCode, expType = self.visit(ast.right, Access(frame, nenv, False, True))
                    self.emit.printout(lhsCode[0] + expCode)
                    _, _ = self.visit(ast.right, Access(frame, nenv, False, True, False, True))
                    self.emit.printout(lhsCode[1])
                    
                    for i in range(0, 2): frame.pop()
                else:
                    # push 1 slot for duplicate value
                    frame.push()
                    expCode, expType = self.visit(ast.right, Access(frame, nenv, False, True))
                    lhsCode, lhsType = self.visit(ast.left, Access(frame, nenv, True, True))

                    if type(lhsType) is FloatType and type(expType) is IntType:
                        expCode = expCode + self.emit.emitI2F(frame)

                    self.emit.printout(expCode + lhsCode)
                    # recover status of stack
                    frame.pop()

                ###################################################
                # frame.push()
                # expCode, expType = self.visit(ast.right, Access(frame, nenv, False, True))
                # lhsCode, lhsType = self.visit(ast.left, Access(frame, nenv, True, True))

                # if type(lhsType) is FloatType and type(expType) is IntType:
                #     expCode = expCode + self.emit.emitI2F(frame)
                # if not isArray:
                #     self.emit.printout(expCode + lhsCode)
                #     frame.pop()
                # else:
                #     self.emit.printout(lhsCode[0] + expCode + lhsCode[1])
                #     [frame.pop() for i in range(0,2)]
            ############################################################################
            # isArray, _ = self.visit(ast.left, Access(frame, nenv, True, True, True))

            # if isArray:
            #     for i in range(0, 2):
            #         frame.push()

            # expCode, expType = self.visit(ast.right, Access(frame, nenv, False, True))
            # lhsCode, lhsType = self.visit(ast.left, Access(frame, nenv, True, True))

            # if type(lhsType) is FloatType and type(expType) is IntType:
            #     expCode = expCode + self.emit.emitI2F(frame)
            # if not isArray:
            #     self.emit.printout(expCode + lhsCode)
            # else:
            #     self.emit.printout(lhsCode[0] + expCode + lhsCode[1])
            #     # recover stack status
            #     [frame.pop() for i in range(0,2)]
            # return expCode + lhsCode, None

        else: # for boolean type
            lCode, lType = self.visit(ast.left, ctxt)
            rCode, rType = self.visit(ast.right, ctxt)
            mType = BoolType()
            if op == '||': return lCode + rCode + self.emit.emitOROP(frame), mType
            if op == '&&': return lCode + rCode + self.emit.emitANDOP(frame), mType


    def visitUnaryOp(self, ast: UnaryOp, o: Access):
        ctxt = o
        frame = ctxt.frame
        op = ast.op
        bodyCode, bodyType = self.visit(ast.body, ctxt)
        if op == '-':
            return bodyCode + self.emit.emitNEGOP(bodyType, frame), bodyType
        if op == '!':
            return bodyCode + self.emit.emitNOT(bodyType, frame), bodyType

    ###################### Literal ##########################
    def visitIntLiteral(self, ast: IntLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()

    def visitStringLiteral(self, ast: StringLiteral, o: Access):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()
