from lark import Transformer

class ASTBuilder(Transformer):
    def number(self, items):
        return ('number', float(items[0]))

    def var(self, items):
        return ('var', str(items[0]))

    def assign(self, items):
        return ('assign', str(items[0]), items[1])

    def print(self, items):
        return ('print', items[0])

    def add(self, items):
        return ('add', items[0], items[1])

    def sub(self, items):
        return ('sub', items[0], items[1])

    def mul(self, items):
        return ('mul', items[0], items[1])

    def div(self, items):
        return ('div', items[0], items[1])

    def string(self, items):
        return ('string', str(items[0]))
