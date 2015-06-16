# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by TypesParser.

class TypesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TypesParser#expr.
    def visitExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypesParser#funcCall.
    def visitFuncCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypesParser#rangeCall.
    def visitRangeCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypesParser#rangeArgs.
    def visitRangeArgs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypesParser#rangeString.
    def visitRangeString(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypesParser#rangeNums.
    def visitRangeNums(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypesParser#floorCall.
    def visitFloorCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypesParser#array.
    def visitArray(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypesParser#unaryExpr.
    def visitUnaryExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypesParser#addExpr.
    def visitAddExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypesParser#mulExpr.
    def visitMulExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypesParser#term.
    def visitTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypesParser#num.
    def visitNum(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypesParser#string.
    def visitString(self, ctx):
        return self.visitChildren(ctx)


