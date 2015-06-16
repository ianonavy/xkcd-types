# Generated from java-escape by ANTLR 4.5
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\16")
        buf.write("[\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\7\7(\n\7")
        buf.write("\f\7\16\7+\13\7\3\7\3\7\3\7\7\7\60\n\7\f\7\16\7\63\13")
        buf.write("\7\3\7\5\7\66\n\7\3\b\6\b9\n\b\r\b\16\b:\3\b\3\b\6\b?")
        buf.write("\n\b\r\b\16\b@\5\bC\n\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\6\rV\n\r\r")
        buf.write("\r\16\rW\3\r\3\r\4)\61\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\3\2\6\3\2\62;\5\2--//^^")
        buf.write("\5\2,,\61\61^^\5\2\13\f\17\17\"\"a\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7\37")
        buf.write("\3\2\2\2\t!\3\2\2\2\13#\3\2\2\2\r\65\3\2\2\2\178\3\2\2")
        buf.write("\2\21D\3\2\2\2\23F\3\2\2\2\25H\3\2\2\2\27N\3\2\2\2\31")
        buf.write("U\3\2\2\2\33\34\7*\2\2\34\4\3\2\2\2\35\36\7+\2\2\36\6")
        buf.write("\3\2\2\2\37 \7.\2\2 \b\3\2\2\2!\"\7]\2\2\"\n\3\2\2\2#")
        buf.write("$\7_\2\2$\f\3\2\2\2%)\7$\2\2&(\13\2\2\2\'&\3\2\2\2(+\3")
        buf.write("\2\2\2)*\3\2\2\2)\'\3\2\2\2*,\3\2\2\2+)\3\2\2\2,\66\7")
        buf.write("$\2\2-\61\7)\2\2.\60\13\2\2\2/.\3\2\2\2\60\63\3\2\2\2")
        buf.write("\61\62\3\2\2\2\61/\3\2\2\2\62\64\3\2\2\2\63\61\3\2\2\2")
        buf.write("\64\66\7)\2\2\65%\3\2\2\2\65-\3\2\2\2\66\16\3\2\2\2\67")
        buf.write("9\t\2\2\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;B")
        buf.write("\3\2\2\2<>\7\60\2\2=?\t\2\2\2>=\3\2\2\2?@\3\2\2\2@>\3")
        buf.write("\2\2\2@A\3\2\2\2AC\3\2\2\2B<\3\2\2\2BC\3\2\2\2C\20\3\2")
        buf.write("\2\2DE\t\3\2\2E\22\3\2\2\2FG\t\4\2\2G\24\3\2\2\2HI\7T")
        buf.write("\2\2IJ\7C\2\2JK\7P\2\2KL\7I\2\2LM\7G\2\2M\26\3\2\2\2N")
        buf.write("O\7H\2\2OP\7N\2\2PQ\7Q\2\2QR\7Q\2\2RS\7T\2\2S\30\3\2\2")
        buf.write("\2TV\t\5\2\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2X")
        buf.write("Y\3\2\2\2YZ\b\r\2\2Z\32\3\2\2\2\n\2)\61\65:@BW\3\b\2\2")
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


