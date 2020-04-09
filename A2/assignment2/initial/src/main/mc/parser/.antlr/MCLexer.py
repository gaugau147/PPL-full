# Generated from e:\Studies\Bach khoa\TAI LIEU\HK191\NGUYEN LY NGON NGU LAP TRINH\Thay Rang\A2\assignment2\initial\src\main\mc\parser\MC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u0188\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3(\3(\7(\u00f7\n(\f(\16(\u00fa\13(\3(\3(\3")
        buf.write("(\3(\3(\3)\3)\3)\3)\7)\u0105\n)\f)\16)\u0108\13)\3)\3")
        buf.write(")\3*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u0115\n*\3+\3+\5+\u0119")
        buf.write("\n+\3+\6+\u011c\n+\r+\16+\u011d\3,\3,\3-\3-\3.\6.\u0125")
        buf.write("\n.\r.\16.\u0126\3.\3.\7.\u012b\n.\f.\16.\u012e\13.\3")
        buf.write(".\5.\u0131\n.\3.\6.\u0134\n.\r.\16.\u0135\3.\3.\3.\7.")
        buf.write("\u013b\n.\f.\16.\u013e\13.\3.\3.\6.\u0142\n.\r.\16.\u0143")
        buf.write("\3.\5.\u0147\n.\5.\u0149\n.\3/\6/\u014c\n/\r/\16/\u014d")
        buf.write("\3\60\3\60\7\60\u0152\n\60\f\60\16\60\u0155\13\60\3\61")
        buf.write("\3\61\7\61\u0159\n\61\f\61\16\61\u015c\13\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\5\62\u0163\n\62\3\63\3\63\3\63\3\64\3")
        buf.write("\64\3\64\3\65\3\65\7\65\u016d\n\65\f\65\16\65\u0170\13")
        buf.write("\65\3\65\5\65\u0173\n\65\3\65\3\65\3\66\3\66\7\66\u0179")
        buf.write("\n\66\f\66\16\66\u017c\13\66\3\66\3\66\3\67\6\67\u0181")
        buf.write("\n\67\r\67\16\67\u0182\3\67\3\67\38\38\3\u00f8\29\3\2")
        buf.write("\5\3\7\4\t\5\13\6\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33")
        buf.write("\16\35\17\37\20!\21#\22%\23\'\24)\25+\26-\27/\30\61\31")
        buf.write("\63\32\65\33\67\349\35;\36=\37? A!C\"E#G$I%K&M\2O\'Q(")
        buf.write("S)U\2W\2Y\2[*]+_,a-c\2e\2g\2i.k/m\60o\61\3\2\f\4\2GGg")
        buf.write("g\4\2\f\f\17\17\3\2\62;\4\2--//\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\6\3\n\f\16\17")
        buf.write("$$^^\5\2\13\f\17\17\"\"\2\u0194\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2")
        buf.write("S\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2")
        buf.write("\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\3q\3\2\2")
        buf.write("\2\5s\3\2\2\2\7v\3\2\2\2\t{\3\2\2\2\13\177\3\2\2\2\r\u0085")
        buf.write("\3\2\2\2\17\u0088\3\2\2\2\21\u008f\3\2\2\2\23\u0095\3")
        buf.write("\2\2\2\25\u009e\3\2\2\2\27\u00a2\3\2\2\2\31\u00a9\3\2")
        buf.write("\2\2\33\u00af\3\2\2\2\35\u00b7\3\2\2\2\37\u00bc\3\2\2")
        buf.write("\2!\u00be\3\2\2\2#\u00c0\3\2\2\2%\u00c3\3\2\2\2\'\u00c6")
        buf.write("\3\2\2\2)\u00c8\3\2\2\2+\u00ca\3\2\2\2-\u00cc\3\2\2\2")
        buf.write("/\u00ce\3\2\2\2\61\u00d0\3\2\2\2\63\u00d2\3\2\2\2\65\u00d5")
        buf.write("\3\2\2\2\67\u00d7\3\2\2\29\u00da\3\2\2\2;\u00dd\3\2\2")
        buf.write("\2=\u00e0\3\2\2\2?\u00e2\3\2\2\2A\u00e4\3\2\2\2C\u00e6")
        buf.write("\3\2\2\2E\u00e8\3\2\2\2G\u00ea\3\2\2\2I\u00ec\3\2\2\2")
        buf.write("K\u00ee\3\2\2\2M\u00f0\3\2\2\2O\u00f2\3\2\2\2Q\u0100\3")
        buf.write("\2\2\2S\u0114\3\2\2\2U\u0116\3\2\2\2W\u011f\3\2\2\2Y\u0121")
        buf.write("\3\2\2\2[\u0148\3\2\2\2]\u014b\3\2\2\2_\u014f\3\2\2\2")
        buf.write("a\u0156\3\2\2\2c\u0162\3\2\2\2e\u0164\3\2\2\2g\u0167\3")
        buf.write("\2\2\2i\u016a\3\2\2\2k\u0176\3\2\2\2m\u0180\3\2\2\2o\u0186")
        buf.write("\3\2\2\2qr\t\2\2\2r\4\3\2\2\2st\7k\2\2tu\7h\2\2u\6\3\2")
        buf.write("\2\2vw\7g\2\2wx\7n\2\2xy\7u\2\2yz\7g\2\2z\b\3\2\2\2{|")
        buf.write("\7h\2\2|}\7q\2\2}~\7t\2\2~\n\3\2\2\2\177\u0080\7y\2\2")
        buf.write("\u0080\u0081\7j\2\2\u0081\u0082\7k\2\2\u0082\u0083\7n")
        buf.write("\2\2\u0083\u0084\7g\2\2\u0084\f\3\2\2\2\u0085\u0086\7")
        buf.write("f\2\2\u0086\u0087\7q\2\2\u0087\16\3\2\2\2\u0088\u0089")
        buf.write("\7t\2\2\u0089\u008a\7g\2\2\u008a\u008b\7v\2\2\u008b\u008c")
        buf.write("\7w\2\2\u008c\u008d\7t\2\2\u008d\u008e\7p\2\2\u008e\20")
        buf.write("\3\2\2\2\u008f\u0090\7d\2\2\u0090\u0091\7t\2\2\u0091\u0092")
        buf.write("\7g\2\2\u0092\u0093\7c\2\2\u0093\u0094\7m\2\2\u0094\22")
        buf.write("\3\2\2\2\u0095\u0096\7e\2\2\u0096\u0097\7q\2\2\u0097\u0098")
        buf.write("\7p\2\2\u0098\u0099\7v\2\2\u0099\u009a\7k\2\2\u009a\u009b")
        buf.write("\7p\2\2\u009b\u009c\7w\2\2\u009c\u009d\7g\2\2\u009d\24")
        buf.write("\3\2\2\2\u009e\u009f\7k\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1")
        buf.write("\7v\2\2\u00a1\26\3\2\2\2\u00a2\u00a3\7u\2\2\u00a3\u00a4")
        buf.write("\7v\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\u00a8\7i\2\2\u00a8\30\3\2\2\2\u00a9\u00aa")
        buf.write("\7h\2\2\u00aa\u00ab\7n\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad")
        buf.write("\7c\2\2\u00ad\u00ae\7v\2\2\u00ae\32\3\2\2\2\u00af\u00b0")
        buf.write("\7d\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3")
        buf.write("\7n\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6")
        buf.write("\7p\2\2\u00b6\34\3\2\2\2\u00b7\u00b8\7x\2\2\u00b8\u00b9")
        buf.write("\7q\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7f\2\2\u00bb\36")
        buf.write("\3\2\2\2\u00bc\u00bd\7\'\2\2\u00bd \3\2\2\2\u00be\u00bf")
        buf.write("\7#\2\2\u00bf\"\3\2\2\2\u00c0\u00c1\7(\2\2\u00c1\u00c2")
        buf.write("\7(\2\2\u00c2$\3\2\2\2\u00c3\u00c4\7~\2\2\u00c4\u00c5")
        buf.write("\7~\2\2\u00c5&\3\2\2\2\u00c6\u00c7\7-\2\2\u00c7(\3\2\2")
        buf.write("\2\u00c8\u00c9\7/\2\2\u00c9*\3\2\2\2\u00ca\u00cb\7,\2")
        buf.write("\2\u00cb,\3\2\2\2\u00cc\u00cd\7\61\2\2\u00cd.\3\2\2\2")
        buf.write("\u00ce\u00cf\7?\2\2\u00cf\60\3\2\2\2\u00d0\u00d1\7>\2")
        buf.write("\2\u00d1\62\3\2\2\2\u00d2\u00d3\7>\2\2\u00d3\u00d4\7?")
        buf.write("\2\2\u00d4\64\3\2\2\2\u00d5\u00d6\7@\2\2\u00d6\66\3\2")
        buf.write("\2\2\u00d7\u00d8\7@\2\2\u00d8\u00d9\7?\2\2\u00d98\3\2")
        buf.write("\2\2\u00da\u00db\7#\2\2\u00db\u00dc\7?\2\2\u00dc:\3\2")
        buf.write("\2\2\u00dd\u00de\7?\2\2\u00de\u00df\7?\2\2\u00df<\3\2")
        buf.write("\2\2\u00e0\u00e1\7*\2\2\u00e1>\3\2\2\2\u00e2\u00e3\7+")
        buf.write("\2\2\u00e3@\3\2\2\2\u00e4\u00e5\7]\2\2\u00e5B\3\2\2\2")
        buf.write("\u00e6\u00e7\7_\2\2\u00e7D\3\2\2\2\u00e8\u00e9\7}\2\2")
        buf.write("\u00e9F\3\2\2\2\u00ea\u00eb\7\177\2\2\u00ebH\3\2\2\2\u00ec")
        buf.write("\u00ed\7=\2\2\u00edJ\3\2\2\2\u00ee\u00ef\7.\2\2\u00ef")
        buf.write("L\3\2\2\2\u00f0\u00f1\7\60\2\2\u00f1N\3\2\2\2\u00f2\u00f3")
        buf.write("\7\61\2\2\u00f3\u00f4\7,\2\2\u00f4\u00f8\3\2\2\2\u00f5")
        buf.write("\u00f7\13\2\2\2\u00f6\u00f5\3\2\2\2\u00f7\u00fa\3\2\2")
        buf.write("\2\u00f8\u00f9\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fb")
        buf.write("\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00fc\7,\2\2\u00fc")
        buf.write("\u00fd\7\61\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\b(\2\2")
        buf.write("\u00ffP\3\2\2\2\u0100\u0101\7\61\2\2\u0101\u0102\7\61")
        buf.write("\2\2\u0102\u0106\3\2\2\2\u0103\u0105\n\3\2\2\u0104\u0103")
        buf.write("\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u0106\3\2\2\2")
        buf.write("\u0109\u010a\b)\2\2\u010aR\3\2\2\2\u010b\u010c\7v\2\2")
        buf.write("\u010c\u010d\7t\2\2\u010d\u010e\7w\2\2\u010e\u0115\7g")
        buf.write("\2\2\u010f\u0110\7h\2\2\u0110\u0111\7c\2\2\u0111\u0112")
        buf.write("\7n\2\2\u0112\u0113\7u\2\2\u0113\u0115\7g\2\2\u0114\u010b")
        buf.write("\3\2\2\2\u0114\u010f\3\2\2\2\u0115T\3\2\2\2\u0116\u0118")
        buf.write("\5\3\2\2\u0117\u0119\5)\25\2\u0118\u0117\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119\u011b\3\2\2\2\u011a\u011c\5W,\2\u011b")
        buf.write("\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011b\3\2\2\2")
        buf.write("\u011d\u011e\3\2\2\2\u011eV\3\2\2\2\u011f\u0120\t\4\2")
        buf.write("\2\u0120X\3\2\2\2\u0121\u0122\t\5\2\2\u0122Z\3\2\2\2\u0123")
        buf.write("\u0125\5W,\2\u0124\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0128\3\2\2\2")
        buf.write("\u0128\u012c\5M\'\2\u0129\u012b\5W,\2\u012a\u0129\3\2")
        buf.write("\2\2\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012f")
        buf.write("\u0131\5U+\2\u0130\u012f\3\2\2\2\u0130\u0131\3\2\2\2\u0131")
        buf.write("\u0149\3\2\2\2\u0132\u0134\5W,\2\u0133\u0132\3\2\2\2\u0134")
        buf.write("\u0135\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2")
        buf.write("\u0136\u0137\3\2\2\2\u0137\u0138\5U+\2\u0138\u0149\3\2")
        buf.write("\2\2\u0139\u013b\5W,\2\u013a\u0139\3\2\2\2\u013b\u013e")
        buf.write("\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d")
        buf.write("\u013f\3\2\2\2\u013e\u013c\3\2\2\2\u013f\u0141\5M\'\2")
        buf.write("\u0140\u0142\5W,\2\u0141\u0140\3\2\2\2\u0142\u0143\3\2")
        buf.write("\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0146")
        buf.write("\3\2\2\2\u0145\u0147\5U+\2\u0146\u0145\3\2\2\2\u0146\u0147")
        buf.write("\3\2\2\2\u0147\u0149\3\2\2\2\u0148\u0124\3\2\2\2\u0148")
        buf.write("\u0133\3\2\2\2\u0148\u013c\3\2\2\2\u0149\\\3\2\2\2\u014a")
        buf.write("\u014c\5W,\2\u014b\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d")
        buf.write("\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e^\3\2\2\2\u014f")
        buf.write("\u0153\t\6\2\2\u0150\u0152\t\7\2\2\u0151\u0150\3\2\2\2")
        buf.write("\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0154\3")
        buf.write("\2\2\2\u0154`\3\2\2\2\u0155\u0153\3\2\2\2\u0156\u015a")
        buf.write("\7$\2\2\u0157\u0159\5c\62\2\u0158\u0157\3\2\2\2\u0159")
        buf.write("\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2")
        buf.write("\u015b\u015d\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e\7")
        buf.write("$\2\2\u015e\u015f\b\61\3\2\u015fb\3\2\2\2\u0160\u0163")
        buf.write("\n\b\2\2\u0161\u0163\5e\63\2\u0162\u0160\3\2\2\2\u0162")
        buf.write("\u0161\3\2\2\2\u0163d\3\2\2\2\u0164\u0165\7^\2\2\u0165")
        buf.write("\u0166\t\t\2\2\u0166f\3\2\2\2\u0167\u0168\7^\2\2\u0168")
        buf.write("\u0169\n\t\2\2\u0169h\3\2\2\2\u016a\u016e\7$\2\2\u016b")
        buf.write("\u016d\5c\62\2\u016c\u016b\3\2\2\2\u016d\u0170\3\2\2\2")
        buf.write("\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0172\3")
        buf.write("\2\2\2\u0170\u016e\3\2\2\2\u0171\u0173\t\n\2\2\u0172\u0171")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\b\65\4\2\u0175")
        buf.write("j\3\2\2\2\u0176\u017a\7$\2\2\u0177\u0179\5c\62\2\u0178")
        buf.write("\u0177\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017b\u017d\3\2\2\2\u017c\u017a\3")
        buf.write("\2\2\2\u017d\u017e\5g\64\2\u017el\3\2\2\2\u017f\u0181")
        buf.write("\t\13\2\2\u0180\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\u0185\b\67\2\2\u0185n\3\2\2\2\u0186\u0187\13\2")
        buf.write("\2\2\u0187p\3\2\2\2\30\2\u00f8\u0106\u0114\u0118\u011d")
        buf.write("\u0126\u012c\u0130\u0135\u013c\u0143\u0146\u0148\u014d")
        buf.write("\u0153\u015a\u0162\u016e\u0172\u017a\u0182\5\b\2\2\3\61")
        buf.write("\2\3\65\3")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    WHILE = 4
    DO = 5
    RETURN = 6
    BREAK = 7
    CONTINUE = 8
    INTEGER = 9
    STRING = 10
    FLOAT = 11
    BOOLEAN = 12
    VOID = 13
    DIV_INT = 14
    NOT = 15
    AND = 16
    OR = 17
    ADD = 18
    SUB = 19
    MUL = 20
    DIV = 21
    ASSIGN = 22
    LT = 23
    LTE = 24
    GT = 25
    GTE = 26
    NEQ = 27
    EQ = 28
    LP = 29
    RP = 30
    LSB = 31
    RSB = 32
    LCB = 33
    RCB = 34
    SEMI = 35
    COMMA = 36
    BLOCK_COMMENT = 37
    LINE_COMMENT = 38
    BOOLLIT = 39
    FLOATLIT = 40
    INTLIT = 41
    ID = 42
    STRINGLIT = 43
    UNCLOSE_STRING = 44
    ILLEGAL_ESCAPE = 45
    WS = 46
    ERROR_CHAR = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'while'", "'do'", "'return'", "'break'", 
            "'continue'", "'int'", "'string'", "'float'", "'boolean'", "'void'", 
            "'%'", "'!'", "'&&'", "'||'", "'+'", "'-'", "'*'", "'/'", "'='", 
            "'<'", "'<='", "'>'", "'>='", "'!='", "'=='", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "WHILE", "DO", "RETURN", "BREAK", "CONTINUE", 
            "INTEGER", "STRING", "FLOAT", "BOOLEAN", "VOID", "DIV_INT", 
            "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", "ASSIGN", "LT", 
            "LTE", "GT", "GTE", "NEQ", "EQ", "LP", "RP", "LSB", "RSB", "LCB", 
            "RCB", "SEMI", "COMMA", "BLOCK_COMMENT", "LINE_COMMENT", "BOOLLIT", 
            "FLOATLIT", "INTLIT", "ID", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "E", "IF", "ELSE", "FOR", "WHILE", "DO", "RETURN", "BREAK", 
                  "CONTINUE", "INTEGER", "STRING", "FLOAT", "BOOLEAN", "VOID", 
                  "DIV_INT", "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", 
                  "ASSIGN", "LT", "LTE", "GT", "GTE", "NEQ", "EQ", "LP", 
                  "RP", "LSB", "RSB", "LCB", "RCB", "SEMI", "COMMA", "DOT", 
                  "BLOCK_COMMENT", "LINE_COMMENT", "BOOLLIT", "EXPONENT", 
                  "DIGIT", "SIGN", "FLOATLIT", "INTLIT", "ID", "STRINGLIT", 
                  "CHAR", "ESC_SEQ", "ESC_ILL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "WS", "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text[1:]);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[47] = self.STRINGLIT_action 
            actions[51] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             
            		        input_string = str(self.text)
            		        self.text = input_string[1:-1]
            	        
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                                input_string = str(self.text)
                                escape = ['\b', '\n', '\r', '\f', '\t', '"', '\\']
                                if input_string[-1] in escape:
                                    self.text = input_string[1:-1]
                                else:
                                    self.text = input_string[1:]
                            
     


