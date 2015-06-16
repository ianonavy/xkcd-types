# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .TypesListener import TypesListener
    from .TypesVisitor import TypesVisitor
else:
    from TypesListener import TypesListener
    from TypesVisitor import TypesVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\16")
        buf.write("o\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\3\2\5\2!\n\2\3\3\3\3\5\3%\n\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\5\5.\n\5\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\7\t?\n\t\f\t\16")
        buf.write("\tB\13\t\5\tD\n\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\7\13Q\n\13\f\13\16\13T\13\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\7\f\\\n\f\f\f\16\f_\13\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\5\ri\n\r\3\16\3\16\3\17\3\17\3\17\2\4")
        buf.write("\24\26\20\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\2k\2 ")
        buf.write("\3\2\2\2\4$\3\2\2\2\6&\3\2\2\2\b-\3\2\2\2\n/\3\2\2\2\f")
        buf.write("\61\3\2\2\2\16\65\3\2\2\2\20:\3\2\2\2\22G\3\2\2\2\24J")
        buf.write("\3\2\2\2\26U\3\2\2\2\30h\3\2\2\2\32j\3\2\2\2\34l\3\2\2")
        buf.write("\2\36!\5\22\n\2\37!\5\24\13\2 \36\3\2\2\2 \37\3\2\2\2")
        buf.write("!\3\3\2\2\2\"%\5\6\4\2#%\5\16\b\2$\"\3\2\2\2$#\3\2\2\2")
        buf.write("%\5\3\2\2\2&\'\7\f\2\2\'(\7\3\2\2()\5\b\5\2)*\7\4\2\2")
        buf.write("*\7\3\2\2\2+.\5\n\6\2,.\5\f\7\2-+\3\2\2\2-,\3\2\2\2.\t")
        buf.write("\3\2\2\2/\60\7\b\2\2\60\13\3\2\2\2\61\62\7\t\2\2\62\63")
        buf.write("\7\5\2\2\63\64\7\t\2\2\64\r\3\2\2\2\65\66\7\r\2\2\66\67")
        buf.write("\7\3\2\2\678\7\t\2\289\7\4\2\29\17\3\2\2\2:C\7\6\2\2;")
        buf.write("@\5\2\2\2<=\7\5\2\2=?\5\2\2\2><\3\2\2\2?B\3\2\2\2@>\3")
        buf.write("\2\2\2@A\3\2\2\2AD\3\2\2\2B@\3\2\2\2C;\3\2\2\2CD\3\2\2")
        buf.write("\2DE\3\2\2\2EF\7\7\2\2F\21\3\2\2\2GH\7\n\2\2HI\7\t\2\2")
        buf.write("I\23\3\2\2\2JK\b\13\1\2KL\5\26\f\2LR\3\2\2\2MN\f\3\2\2")
        buf.write("NO\7\n\2\2OQ\5\26\f\2PM\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS")
        buf.write("\3\2\2\2S\25\3\2\2\2TR\3\2\2\2UV\b\f\1\2VW\5\30\r\2W]")
        buf.write("\3\2\2\2XY\f\3\2\2YZ\7\13\2\2Z\\\5\30\r\2[X\3\2\2\2\\")
        buf.write("_\3\2\2\2][\3\2\2\2]^\3\2\2\2^\27\3\2\2\2_]\3\2\2\2`i")
        buf.write("\5\32\16\2ai\5\34\17\2bi\5\4\3\2ci\5\20\t\2de\7\3\2\2")
        buf.write("ef\5\2\2\2fg\7\4\2\2gi\3\2\2\2h`\3\2\2\2ha\3\2\2\2hb\3")
        buf.write("\2\2\2hc\3\2\2\2hd\3\2\2\2i\31\3\2\2\2jk\7\t\2\2k\33\3")
        buf.write("\2\2\2lm\7\b\2\2m\35\3\2\2\2\n $-@CR]h")
        return buf.getvalue()


class TypesParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"','", u"'['", u"']'", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'RANGE'", u"'FLOOR'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"STRING", u"NUM", u"ADD_OP", 
                      u"MUL_OP", u"RANGE", u"FLOOR", u"WS" ]

    RULE_expr = 0
    RULE_funcCall = 1
    RULE_rangeCall = 2
    RULE_rangeArgs = 3
    RULE_rangeString = 4
    RULE_rangeNums = 5
    RULE_floorCall = 6
    RULE_array = 7
    RULE_unaryExpr = 8
    RULE_addExpr = 9
    RULE_mulExpr = 10
    RULE_term = 11
    RULE_num = 12
    RULE_string = 13

    ruleNames =  [ "expr", "funcCall", "rangeCall", "rangeArgs", "rangeString", 
                   "rangeNums", "floorCall", "array", "unaryExpr", "addExpr", 
                   "mulExpr", "term", "num", "string" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    STRING=6
    NUM=7
    ADD_OP=8
    MUL_OP=9
    RANGE=10
    FLOOR=11
    WS=12

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(TypesParser.UnaryExprContext,0)


        def addExpr(self):
            return self.getTypedRuleContext(TypesParser.AddExprContext,0)


        def getRuleIndex(self):
            return TypesParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, TypesVisitor ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = TypesParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 30
            token = self._input.LA(1)
            if token in [TypesParser.ADD_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.unaryExpr()

            elif token in [TypesParser.T__0, TypesParser.T__3, TypesParser.STRING, TypesParser.NUM, TypesParser.RANGE, TypesParser.FLOOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.addExpr(0)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rangeCall(self):
            return self.getTypedRuleContext(TypesParser.RangeCallContext,0)


        def floorCall(self):
            return self.getTypedRuleContext(TypesParser.FloorCallContext,0)


        def getRuleIndex(self):
            return TypesParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.exitFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, TypesVisitor ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = TypesParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcCall)
        try:
            self.state = 34
            token = self._input.LA(1)
            if token in [TypesParser.RANGE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.rangeCall()

            elif token in [TypesParser.FLOOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.floorCall()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RangeCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANGE(self):
            return self.getToken(TypesParser.RANGE, 0)

        def rangeArgs(self):
            return self.getTypedRuleContext(TypesParser.RangeArgsContext,0)


        def getRuleIndex(self):
            return TypesParser.RULE_rangeCall

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.enterRangeCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.exitRangeCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, TypesVisitor ):
                return visitor.visitRangeCall(self)
            else:
                return visitor.visitChildren(self)




    def rangeCall(self):

        localctx = TypesParser.RangeCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_rangeCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(TypesParser.RANGE)
            self.state = 37
            self.match(TypesParser.T__0)
            self.state = 38
            self.rangeArgs()
            self.state = 39
            self.match(TypesParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RangeArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rangeString(self):
            return self.getTypedRuleContext(TypesParser.RangeStringContext,0)


        def rangeNums(self):
            return self.getTypedRuleContext(TypesParser.RangeNumsContext,0)


        def getRuleIndex(self):
            return TypesParser.RULE_rangeArgs

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.enterRangeArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.exitRangeArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, TypesVisitor ):
                return visitor.visitRangeArgs(self)
            else:
                return visitor.visitChildren(self)




    def rangeArgs(self):

        localctx = TypesParser.RangeArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rangeArgs)
        try:
            self.state = 43
            token = self._input.LA(1)
            if token in [TypesParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.rangeString()

            elif token in [TypesParser.NUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.rangeNums()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RangeStringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TypesParser.STRING, 0)

        def getRuleIndex(self):
            return TypesParser.RULE_rangeString

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.enterRangeString(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.exitRangeString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, TypesVisitor ):
                return visitor.visitRangeString(self)
            else:
                return visitor.visitChildren(self)




    def rangeString(self):

        localctx = TypesParser.RangeStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_rangeString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(TypesParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RangeNumsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(TypesParser.NUM)
            else:
                return self.getToken(TypesParser.NUM, i)

        def getRuleIndex(self):
            return TypesParser.RULE_rangeNums

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.enterRangeNums(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.exitRangeNums(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, TypesVisitor ):
                return visitor.visitRangeNums(self)
            else:
                return visitor.visitChildren(self)




    def rangeNums(self):

        localctx = TypesParser.RangeNumsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rangeNums)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(TypesParser.NUM)
            self.state = 48
            self.match(TypesParser.T__2)
            self.state = 49
            self.match(TypesParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FloorCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOOR(self):
            return self.getToken(TypesParser.FLOOR, 0)

        def NUM(self):
            return self.getToken(TypesParser.NUM, 0)

        def getRuleIndex(self):
            return TypesParser.RULE_floorCall

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.enterFloorCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.exitFloorCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, TypesVisitor ):
                return visitor.visitFloorCall(self)
            else:
                return visitor.visitChildren(self)




    def floorCall(self):

        localctx = TypesParser.FloorCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_floorCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(TypesParser.FLOOR)
            self.state = 52
            self.match(TypesParser.T__0)
            self.state = 53
            self.match(TypesParser.NUM)
            self.state = 54
            self.match(TypesParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypesParser.ExprContext)
            else:
                return self.getTypedRuleContext(TypesParser.ExprContext,i)


        def getRuleIndex(self):
            return TypesParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, TypesVisitor ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = TypesParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(TypesParser.T__3)
            self.state = 65
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TypesParser.T__0) | (1 << TypesParser.T__3) | (1 << TypesParser.STRING) | (1 << TypesParser.NUM) | (1 << TypesParser.ADD_OP) | (1 << TypesParser.RANGE) | (1 << TypesParser.FLOOR))) != 0):
                self.state = 57
                self.expr()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TypesParser.T__2:
                    self.state = 58
                    self.match(TypesParser.T__2)
                    self.state = 59
                    self.expr()
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 67
            self.match(TypesParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnaryExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD_OP(self):
            return self.getToken(TypesParser.ADD_OP, 0)

        def NUM(self):
            return self.getToken(TypesParser.NUM, 0)

        def getRuleIndex(self):
            return TypesParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, TypesVisitor ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = TypesParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_unaryExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(TypesParser.ADD_OP)
            self.state = 70
            self.match(TypesParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AddExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mulExpr(self):
            return self.getTypedRuleContext(TypesParser.MulExprContext,0)


        def addExpr(self):
            return self.getTypedRuleContext(TypesParser.AddExprContext,0)


        def ADD_OP(self):
            return self.getToken(TypesParser.ADD_OP, 0)

        def getRuleIndex(self):
            return TypesParser.RULE_addExpr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, TypesVisitor ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)



    def addExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TypesParser.AddExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_addExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.mulExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TypesParser.AddExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                    self.state = 75
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 76
                    self.match(TypesParser.ADD_OP)
                    self.state = 77
                    self.mulExpr(0) 
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MulExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(TypesParser.TermContext,0)


        def mulExpr(self):
            return self.getTypedRuleContext(TypesParser.MulExprContext,0)


        def MUL_OP(self):
            return self.getToken(TypesParser.MUL_OP, 0)

        def getRuleIndex(self):
            return TypesParser.RULE_mulExpr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.exitMulExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, TypesVisitor ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)



    def mulExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TypesParser.MulExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_mulExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TypesParser.MulExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                    self.state = 86
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 87
                    self.match(TypesParser.MUL_OP)
                    self.state = 88
                    self.term() 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(TypesParser.NumContext,0)


        def string(self):
            return self.getTypedRuleContext(TypesParser.StringContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(TypesParser.FuncCallContext,0)


        def array(self):
            return self.getTypedRuleContext(TypesParser.ArrayContext,0)


        def expr(self):
            return self.getTypedRuleContext(TypesParser.ExprContext,0)


        def getRuleIndex(self):
            return TypesParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, TypesVisitor ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = TypesParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_term)
        try:
            self.state = 102
            token = self._input.LA(1)
            if token in [TypesParser.NUM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.num()

            elif token in [TypesParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.string()

            elif token in [TypesParser.RANGE, TypesParser.FLOOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.funcCall()

            elif token in [TypesParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.array()

            elif token in [TypesParser.T__0]:
                self.enterOuterAlt(localctx, 5)
                self.state = 98
                self.match(TypesParser.T__0)
                self.state = 99
                self.expr()
                self.state = 100
                self.match(TypesParser.T__1)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(TypesParser.NUM, 0)

        def getRuleIndex(self):
            return TypesParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, TypesVisitor ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)




    def num(self):

        localctx = TypesParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(TypesParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TypesParser.STRING, 0)

        def getRuleIndex(self):
            return TypesParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TypesListener ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, TypesVisitor ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = TypesParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(TypesParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.addExpr_sempred
        self._predicates[10] = self.mulExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def addExpr_sempred(self, localctx:AddExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def mulExpr_sempred(self, localctx:MulExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         



