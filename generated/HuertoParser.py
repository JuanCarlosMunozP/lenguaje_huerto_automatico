# Generated from Huerto.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,77,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,4,0,21,8,0,11,0,12,0,22,1,0,1,0,1,1,1,
        1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,4,2,37,8,2,11,2,12,2,38,1,2,1,
        2,1,3,1,3,1,3,3,3,46,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,55,8,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,64,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,2,1,0,11,13,
        1,0,16,18,74,0,20,1,0,0,0,2,26,1,0,0,0,4,30,1,0,0,0,6,45,1,0,0,0,
        8,47,1,0,0,0,10,63,1,0,0,0,12,65,1,0,0,0,14,70,1,0,0,0,16,74,1,0,
        0,0,18,21,3,2,1,0,19,21,3,4,2,0,20,18,1,0,0,0,20,19,1,0,0,0,21,22,
        1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,24,1,0,0,0,24,25,5,0,0,1,
        25,1,1,0,0,0,26,27,5,1,0,0,27,28,5,19,0,0,28,29,5,2,0,0,29,3,1,0,
        0,0,30,31,5,3,0,0,31,32,5,19,0,0,32,33,5,4,0,0,33,34,5,5,0,0,34,
        36,5,6,0,0,35,37,3,6,3,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,
        0,38,39,1,0,0,0,39,40,1,0,0,0,40,41,5,7,0,0,41,5,1,0,0,0,42,46,3,
        8,4,0,43,46,3,10,5,0,44,46,3,12,6,0,45,42,1,0,0,0,45,43,1,0,0,0,
        45,44,1,0,0,0,46,7,1,0,0,0,47,48,5,8,0,0,48,49,3,14,7,0,49,50,5,
        9,0,0,50,54,3,6,3,0,51,52,5,10,0,0,52,53,5,9,0,0,53,55,3,6,3,0,54,
        51,1,0,0,0,54,55,1,0,0,0,55,9,1,0,0,0,56,57,7,0,0,0,57,58,5,19,0,
        0,58,64,5,2,0,0,59,60,5,14,0,0,60,61,5,20,0,0,61,62,5,15,0,0,62,
        64,5,2,0,0,63,56,1,0,0,0,63,59,1,0,0,0,64,11,1,0,0,0,65,66,5,19,
        0,0,66,67,5,4,0,0,67,68,5,5,0,0,68,69,5,2,0,0,69,13,1,0,0,0,70,71,
        5,19,0,0,71,72,3,16,8,0,72,73,5,20,0,0,73,15,1,0,0,0,74,75,7,1,0,
        0,75,17,1,0,0,0,6,20,22,38,45,54,63
    ]

class HuertoParser ( Parser ):

    grammarFileName = "Huerto.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'cultivo'", "';'", "'tarea'", "'('", 
                     "')'", "'{'", "'}'", "'si'", "':'", "'sino'", "'regar'", 
                     "'abonar'", "'podar'", "'esperar'", "'dias'", "'<'", 
                     "'>'", "'=='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUMBER", 
                      "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_routine = 2
    RULE_statement = 3
    RULE_control = 4
    RULE_action = 5
    RULE_call = 6
    RULE_condition = 7
    RULE_comparator = 8

    ruleNames =  [ "program", "declaration", "routine", "statement", "control", 
                   "action", "call", "condition", "comparator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    ID=19
    NUMBER=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(HuertoParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HuertoParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(HuertoParser.DeclarationContext,i)


        def routine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HuertoParser.RoutineContext)
            else:
                return self.getTypedRuleContext(HuertoParser.RoutineContext,i)


        def getRuleIndex(self):
            return HuertoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = HuertoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 18
                    self.declaration()
                    pass
                elif token in [3]:
                    self.state = 19
                    self.routine()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==3):
                    break

            self.state = 24
            self.match(HuertoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HuertoParser.ID, 0)

        def getRuleIndex(self):
            return HuertoParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = HuertoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(HuertoParser.T__0)
            self.state = 27
            self.match(HuertoParser.ID)
            self.state = 28
            self.match(HuertoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoutineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HuertoParser.ID, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HuertoParser.StatementContext)
            else:
                return self.getTypedRuleContext(HuertoParser.StatementContext,i)


        def getRuleIndex(self):
            return HuertoParser.RULE_routine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoutine" ):
                listener.enterRoutine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoutine" ):
                listener.exitRoutine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoutine" ):
                return visitor.visitRoutine(self)
            else:
                return visitor.visitChildren(self)




    def routine(self):

        localctx = HuertoParser.RoutineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_routine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(HuertoParser.T__2)
            self.state = 31
            self.match(HuertoParser.ID)
            self.state = 32
            self.match(HuertoParser.T__3)
            self.state = 33
            self.match(HuertoParser.T__4)
            self.state = 34
            self.match(HuertoParser.T__5)
            self.state = 36 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 35
                self.statement()
                self.state = 38 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 555264) != 0)):
                    break

            self.state = 40
            self.match(HuertoParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def control(self):
            return self.getTypedRuleContext(HuertoParser.ControlContext,0)


        def action(self):
            return self.getTypedRuleContext(HuertoParser.ActionContext,0)


        def call(self):
            return self.getTypedRuleContext(HuertoParser.CallContext,0)


        def getRuleIndex(self):
            return HuertoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = HuertoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.control()
                pass
            elif token in [11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.action()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.call()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ControlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HuertoParser.RULE_control

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfControlContext(ControlContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HuertoParser.ControlContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition(self):
            return self.getTypedRuleContext(HuertoParser.ConditionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HuertoParser.StatementContext)
            else:
                return self.getTypedRuleContext(HuertoParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfControl" ):
                listener.enterIfControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfControl" ):
                listener.exitIfControl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfControl" ):
                return visitor.visitIfControl(self)
            else:
                return visitor.visitChildren(self)



    def control(self):

        localctx = HuertoParser.ControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_control)
        try:
            localctx = HuertoParser.IfControlContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(HuertoParser.T__7)
            self.state = 48
            self.condition()
            self.state = 49
            self.match(HuertoParser.T__8)
            self.state = 50
            self.statement()
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 51
                self.match(HuertoParser.T__9)
                self.state = 52
                self.match(HuertoParser.T__8)
                self.state = 53
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HuertoParser.RULE_action

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EsperarActionContext(ActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HuertoParser.ActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(HuertoParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEsperarAction" ):
                listener.enterEsperarAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEsperarAction" ):
                listener.exitEsperarAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEsperarAction" ):
                return visitor.visitEsperarAction(self)
            else:
                return visitor.visitChildren(self)


    class CultivoActionContext(ActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HuertoParser.ActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(HuertoParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCultivoAction" ):
                listener.enterCultivoAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCultivoAction" ):
                listener.exitCultivoAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCultivoAction" ):
                return visitor.visitCultivoAction(self)
            else:
                return visitor.visitChildren(self)



    def action(self):

        localctx = HuertoParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13]:
                localctx = HuertoParser.CultivoActionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 57
                self.match(HuertoParser.ID)
                self.state = 58
                self.match(HuertoParser.T__1)
                pass
            elif token in [14]:
                localctx = HuertoParser.EsperarActionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(HuertoParser.T__13)
                self.state = 60
                self.match(HuertoParser.NUMBER)
                self.state = 61
                self.match(HuertoParser.T__14)
                self.state = 62
                self.match(HuertoParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HuertoParser.ID, 0)

        def getRuleIndex(self):
            return HuertoParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = HuertoParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(HuertoParser.ID)
            self.state = 66
            self.match(HuertoParser.T__3)
            self.state = 67
            self.match(HuertoParser.T__4)
            self.state = 68
            self.match(HuertoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HuertoParser.ID, 0)

        def comparator(self):
            return self.getTypedRuleContext(HuertoParser.ComparatorContext,0)


        def NUMBER(self):
            return self.getToken(HuertoParser.NUMBER, 0)

        def getRuleIndex(self):
            return HuertoParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = HuertoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(HuertoParser.ID)
            self.state = 71
            self.comparator()
            self.state = 72
            self.match(HuertoParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HuertoParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = HuertoParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





