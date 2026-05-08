# Generated from Huerto.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .HuertoParser import HuertoParser
else:
    from HuertoParser import HuertoParser

# This class defines a complete generic visitor for a parse tree produced by HuertoParser.

class HuertoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HuertoParser#program.
    def visitProgram(self, ctx:HuertoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HuertoParser#declaration.
    def visitDeclaration(self, ctx:HuertoParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HuertoParser#routine.
    def visitRoutine(self, ctx:HuertoParser.RoutineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HuertoParser#statement.
    def visitStatement(self, ctx:HuertoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HuertoParser#ifControl.
    def visitIfControl(self, ctx:HuertoParser.IfControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HuertoParser#cultivoAction.
    def visitCultivoAction(self, ctx:HuertoParser.CultivoActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HuertoParser#esperarAction.
    def visitEsperarAction(self, ctx:HuertoParser.EsperarActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HuertoParser#call.
    def visitCall(self, ctx:HuertoParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HuertoParser#condition.
    def visitCondition(self, ctx:HuertoParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HuertoParser#comparator.
    def visitComparator(self, ctx:HuertoParser.ComparatorContext):
        return self.visitChildren(ctx)



del HuertoParser