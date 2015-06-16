from xkcd_types.utils import compute_ranges
from xkcd_types.gen.TypesParser import TypesParser
from xkcd_types.gen.TypesVisitor import TypesVisitor


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
