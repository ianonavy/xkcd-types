import readline

from antlr4 import CommonTokenStream
from antlr4.InputStream import InputStream

from xkcd_types.interpreter import TypesInterpreter
from xkcd_types.gen.TypesLexer import TypesLexer
from xkcd_types.gen.TypesParser import TypesParser


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
        prompt = "[{}]> ".format(self.command_number)
        return self.replace_text(prompt)

    def enter_command(self, command):
        interpreter = TypesInterpreter(self.command_number, self.replacements)
        out = self.parse_command(command, interpreter)
        self.command_number += 1
        return self.replace_text(out)

    def output(self, text):
        for line in text.split("\n"):
            print("  => {}".format(line))
        print()

    def parse_command(self, command, interpreter):
        input = InputStream(command)
        lexer = TypesLexer(input)
        stream = CommonTokenStream(lexer)
        parser = TypesParser(stream)
        tree = parser.expr()
        return str(interpreter.visit(tree))
