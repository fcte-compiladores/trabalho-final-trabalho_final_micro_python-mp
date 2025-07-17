import sys

from lark import Lark
from pathlib import Path
from .ast_builder import ASTBuilder
from .interpreter import Interpreter

BASE = Path(__file__).parent

# Carrega a gramÃ¡tica
with open(BASE / "grammar.lark", encoding="utf-8") as f:
    grammar = f.read()

parser = Lark(grammar, parser='lalr', transformer=ASTBuilder())
interpreter = Interpreter()

def main():
    if len(sys.argv) < 2:
        print("Uso: mp <arquivo_fonte>")
        sys.exit(1)

    with open(sys.argv[1], encoding="utf-8") as f:
        codigo = f.read()

    tree = parser.parse(codigo)
    if isinstance(tree, list):
        for stmt in tree:
            interpreter.exec(stmt)
    else:
        interpreter.exec(tree)


if __name__ == "__main__":
    main()