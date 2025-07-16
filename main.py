import sys

from lark import Lark
from ast_builder import ASTBuilder
from interpreter import Interpreter

# Carrega a gramática
with open("grammar.lark", encoding="utf-8") as f:
    grammar = f.read()

parser = Lark(grammar, parser='lalr', transformer=ASTBuilder())
interpreter = Interpreter()

if len(sys.argv) < 2:
    print("Uso: python main.py <arquivo_fonte>")
    sys.exit(1)

with open(sys.argv[1], encoding="utf-8") as f:
    codigo = f.read()

tree = parser.parse(codigo)
for stmt in tree.children:
    interpreter.exec(stmt)
