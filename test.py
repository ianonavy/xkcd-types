from TypesLexer import TypesLexer
from TypesParser import TypesParser
from TypesVisitor import TypesVisitor
from antlr4 import CommonTokenStream
from antlr4.InputStream import InputStream

import readline
import io



xkcd_tests = [
    ('2+"2"', '"4"'),
    ('"2"+[]', '"[2]"'),
    ('(2/0)', 'NaN'),
    ('(2/0)+2', 'NaP'),
    ('"" + ""', '\'"+"\''),
    ('[1,2,3]+2', 'FALSE'),
    ('[1,2,3]+4', 'TRUE'),
    ('2/(2-(3/2+1/2))', 'NaN.000000000000013'),
    ('RANGE(" ")', '''('"', "!", " ", "!", '"')'''),
    ('+ 2', '12'),
    ('2+2', 'DONE'),
    ('RANGE(1,5)', '(1, 4, 3, 4, 5)'),
    ('FLOOR(10.5)', '''|
|
|
|_ _ _10.5_ _ _ '''),
]


def test_parser(repl, case, expected):
    assert repl.enter_command(case) == expected


def compute_ranges(values):
    all_values = []
    for first, second in zip(values, values[1:]):
        all_values += list(range(first, second, 1 if first < second else -1))
    return all_values + [values[-1]]


# test for compute_ranges
assert compute_ranges([0, 1]) == [0, 1]
assert compute_ranges([0, 5]) == [0, 1, 2, 3, 4, 5]
assert compute_ranges([0, 3, 0]) == [0, 1, 2, 3, 2, 1, 0]



class TypesInterpreter(TypesVisitor):

    def __init__(self, command_number, replacements):
        self.command_number = command_number
        self.replacements = replacements

    def defaultResult(self):
        return "fail"

    def aggregateResult(self, aggregate, nextResult):
        return (nextResult
                if nextResult != self.defaultResult()
                else aggregate)

    def visitTerm(self, ctx):
        return self.visitChildren(ctx)

    def visitString(self, ctx):
        return ctx.getText()[1:-1]

    def visitNum(self, ctx):
        return eval(ctx.getText())

    def visitArray(self, ctx):
        # Vulnerability here!
        return eval(ctx.getText())

    def visitAddExpr(self, ctx):
        if len(ctx.children) == 3:
            left = ctx.addExpr().accept(self)
            right = ctx.mulExpr().accept(self)

            if (isinstance(left, (int, float, complex)) and
                isinstance(right, str)):
                return '"{}{}"'.format(
                    right[:-1],
                    "".join([chr(ord(right[-1]) + left)]))
            elif (isinstance(right, (int, float, complex)) and
                isinstance(left, str)):
                return '{}{}'.format(
                    left[:-1],
                    "".join([chr(ord(left[-1]) + right)]))
            elif (isinstance(left, str) and isinstance(right, list)):
                # vulnerability here! :D
                return '"{}"'.format(str([eval(left)] + right))
            elif (isinstance(left, str) and isinstance(right, str)):
                return "'{}'".format(ctx.getText()[1:-1])
            elif (isinstance(left, list) and
                  isinstance(right, (int, float, complex))):
                return str(not right in set(left)).upper()
            elif isinstance(left, int) and isinstance(right, int):
                self.replacements[str(left)] = eval(str(self.replacements.get(left, left)) + str(ctx.ADD_OP()) + str(right))
                return "DONE"
            elif (isinstance(left, (int, float, complex)) and
                isinstance(right, (int, float, complex))):
                return eval(str(left) + str(ctx.ADD_OP()) + str(right))
        else:
            child = ctx.getChild(0).getChild(0)
            my_type = type(child)
            text = child.getText()
            if my_type in (TypesParser.NumContext,
                           TypesParser.StringContext,
                           TypesParser.ArrayContext):
                return eval(text)
        return self.visitChildren(ctx)

    def visitMulExpr(self, ctx):
        if len(ctx.children) == 3:
            left = ctx.mulExpr().accept(self)
            right = ctx.term().accept(self)
            try:
                return eval(str(left) + str(ctx.MUL_OP()) + str(right))
            except:
                ret = "NaN"
                if right == 0 and len(ctx.term().children) > 1:
                    ret += ".000000000000013"
                return ret
        else:
            return self.visitChildren(ctx)

    def visitRangeString(self, ctx):
        ascii_values = [ord(letter) for letter in ctx.getText()]
        ranges = compute_ranges(ascii_values)
        chars = [chr(val) for val in ranges]
        ret = []
        for char in chars:
            if char == '"':
                ret.append("'\"'")
            else:
                ret.append('"' + char + '"')
        return "({})".format(", ".join(ret))

    def visitRangeNums(self, ctx):
        lower = int(ctx.getChild(0).getText())
        upper = int(ctx.getChild(2).getText())
        return str(tuple(range(lower, upper + 1)))

    def visitUnaryExpr(self, ctx):
        return eval(
            str(self.command_number) +
            ctx.ADD_OP().getText() +
            ctx.NUM().getText())

    def visitFloorCall(self, ctx):
        return '''|
|
|
|_ _ _{}_ _ _ '''.format(ctx.NUM().getText())


class TypesREPL(object):

    def __init__(self):
        self.command_number = 1
        self.replacements = {}

    def run(self):
        while True:
            self.output(self.enter_command(input(self.get_prompt())))

    def replace_text(self, text):
        for key, value in self.replacements.items():
            text = text.replace(str(key), str(value))
        return text

    def get_prompt(self):
        prompt = "[{}] ".format(self.command_number)
        return self.replace_text(prompt)

    def enter_command(self, command):
        interpreter = TypesInterpreter(self.command_number, self.replacements)
        out = self.parse_command(command, interpreter)
        self.command_number += 1
        return self.replace_text(out)

    def output(self, text):
        for line in text.split("\n"):
            print("=> {}".format(line))
        print()

    def parse_command(self, command, interpreter):
        input = InputStream(command)
        lexer = TypesLexer(input)
        stream = CommonTokenStream(lexer)
        parser = TypesParser(stream)
        tree = parser.expr()
        out = io.StringIO()
        try:
            return str(interpreter.visit(tree))
        except:
            return "Syntax error"


def main():
    repl = TypesREPL()
    # for case, expected in xkcd_tests:
    #     test_parser(repl, case, expected)
    repl.run()


if __name__ == '__main__':
    main()
