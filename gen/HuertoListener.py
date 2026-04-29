# Generated from Huerto.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .HuertoParser import HuertoParser
else:
    from HuertoParser import HuertoParser

# This class defines a complete listener for a parse tree produced by HuertoParser.
class HuertoListener(ParseTreeListener):

    # Enter a parse tree produced by HuertoParser#program.
    def enterProgram(self, ctx:HuertoParser.ProgramContext):
        pass

    # Exit a parse tree produced by HuertoParser#program.
    def exitProgram(self, ctx:HuertoParser.ProgramContext):
        pass


    # Enter a parse tree produced by HuertoParser#declaration.
    def enterDeclaration(self, ctx:HuertoParser.DeclarationContext):
        pass

    # Exit a parse tree produced by HuertoParser#declaration.
    def exitDeclaration(self, ctx:HuertoParser.DeclarationContext):
        pass


    # Enter a parse tree produced by HuertoParser#routine.
    def enterRoutine(self, ctx:HuertoParser.RoutineContext):
        pass

    # Exit a parse tree produced by HuertoParser#routine.
    def exitRoutine(self, ctx:HuertoParser.RoutineContext):
        pass


    # Enter a parse tree produced by HuertoParser#statement.
    def enterStatement(self, ctx:HuertoParser.StatementContext):
        pass

    # Exit a parse tree produced by HuertoParser#statement.
    def exitStatement(self, ctx:HuertoParser.StatementContext):
        pass


    # Enter a parse tree produced by HuertoParser#ifControl.
    def enterIfControl(self, ctx:HuertoParser.IfControlContext):
        pass

    # Exit a parse tree produced by HuertoParser#ifControl.
    def exitIfControl(self, ctx:HuertoParser.IfControlContext):
        pass


    # Enter a parse tree produced by HuertoParser#cultivoAction.
    def enterCultivoAction(self, ctx:HuertoParser.CultivoActionContext):
        pass

    # Exit a parse tree produced by HuertoParser#cultivoAction.
    def exitCultivoAction(self, ctx:HuertoParser.CultivoActionContext):
        pass


    # Enter a parse tree produced by HuertoParser#esperarAction.
    def enterEsperarAction(self, ctx:HuertoParser.EsperarActionContext):
        pass

    # Exit a parse tree produced by HuertoParser#esperarAction.
    def exitEsperarAction(self, ctx:HuertoParser.EsperarActionContext):
        pass


    # Enter a parse tree produced by HuertoParser#call.
    def enterCall(self, ctx:HuertoParser.CallContext):
        pass

    # Exit a parse tree produced by HuertoParser#call.
    def exitCall(self, ctx:HuertoParser.CallContext):
        pass


    # Enter a parse tree produced by HuertoParser#condition.
    def enterCondition(self, ctx:HuertoParser.ConditionContext):
        pass

    # Exit a parse tree produced by HuertoParser#condition.
    def exitCondition(self, ctx:HuertoParser.ConditionContext):
        pass


    # Enter a parse tree produced by HuertoParser#comparator.
    def enterComparator(self, ctx:HuertoParser.ComparatorContext):
        pass

    # Exit a parse tree produced by HuertoParser#comparator.
    def exitComparator(self, ctx:HuertoParser.ComparatorContext):
        pass



del HuertoParser