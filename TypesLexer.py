# Generated from java-escape by ANTLR 4.5
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\16")
        buf.write("W\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\7\7(\n\7")
        buf.write("\f\7\16\7+\13\7\3\7\3\7\3\7\7\7\60\n\7\f\7\16\7\63\13")
        buf.write("\7\3\7\5\7\66\n\7\3\b\6\b9\n\b\r\b\16\b:\3\b\3\b\5\b?")
        buf.write("\n\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\6\rR\n\r\r\r\16\rS\3\r\3\r\4")
        buf.write(")\61\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\3\2\6\3\2\62;\5\2--//^^\5\2,,\61\61^^\5")
        buf.write("\2\13\f\17\17\"\"\\\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2\t!\3\2")
        buf.write("\2\2\13#\3\2\2\2\r\65\3\2\2\2\178\3\2\2\2\21@\3\2\2\2")
        buf.write("\23B\3\2\2\2\25D\3\2\2\2\27J\3\2\2\2\31Q\3\2\2\2\33\34")
        buf.write("\7*\2\2\34\4\3\2\2\2\35\36\7+\2\2\36\6\3\2\2\2\37 \7.")
        buf.write("\2\2 \b\3\2\2\2!\"\7]\2\2\"\n\3\2\2\2#$\7_\2\2$\f\3\2")
        buf.write("\2\2%)\7$\2\2&(\13\2\2\2\'&\3\2\2\2(+\3\2\2\2)*\3\2\2")
        buf.write("\2)\'\3\2\2\2*,\3\2\2\2+)\3\2\2\2,\66\7$\2\2-\61\7)\2")
        buf.write("\2.\60\13\2\2\2/.\3\2\2\2\60\63\3\2\2\2\61\62\3\2\2\2")
        buf.write("\61/\3\2\2\2\62\64\3\2\2\2\63\61\3\2\2\2\64\66\7)\2\2")
        buf.write("\65%\3\2\2\2\65-\3\2\2\2\66\16\3\2\2\2\679\t\2\2\28\67")
        buf.write("\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;>\3\2\2\2<=\7\60")
        buf.write("\2\2=?\t\2\2\2><\3\2\2\2>?\3\2\2\2?\20\3\2\2\2@A\t\3\2")
        buf.write("\2A\22\3\2\2\2BC\t\4\2\2C\24\3\2\2\2DE\7T\2\2EF\7C\2\2")
        buf.write("FG\7P\2\2GH\7I\2\2HI\7G\2\2I\26\3\2\2\2JK\7H\2\2KL\7N")
        buf.write("\2\2LM\7Q\2\2MN\7Q\2\2NO\7T\2\2O\30\3\2\2\2PR\t\5\2\2")
        buf.write("QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\b")
        buf.write("\r\2\2V\32\3\2\2\2\t\2)\61\65:>S\3\b\2\2")
        return buf.getvalue()


class TypesLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    STRING = 6
    NUM = 7
    ADD_OP = 8
    MUL_OP = 9
    RANGE = 10
    FLOOR = 11
    WS = 12

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            "'('", "')'", "','", "'['", "']'", "'RANGE'", "'FLOOR'" ]

    symbolicNames = [ u"<INVALID>",
            "STRING", "NUM", "ADD_OP", "MUL_OP", "RANGE", "FLOOR", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "STRING", "NUM", 
                  "ADD_OP", "MUL_OP", "RANGE", "FLOOR", "WS" ]

    grammarFileName = "Types.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


