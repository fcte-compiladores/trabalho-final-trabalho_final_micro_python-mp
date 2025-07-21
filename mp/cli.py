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
        print("Uso: mp <arquivo_fonte> [--arvore]")
        sys.exit(1)

    show_tree = '--arvore' in sys.argv
    filename = sys.argv[1]
    if show_tree and filename == '--arvore' and len(sys.argv) > 2:
        filename = sys.argv[2]

    with open(filename, encoding="utf-8") as f:
        codigo = f.read()

    # Parse SEM transformer para visualizar a árvore sintática concreta
    if show_tree:
        parser_sem_transformer = Lark(grammar, parser='lalr')
        tree = parser_sem_transformer.parse(codigo)
        print(tree.pretty())
        sys.exit(0)

    tree = parser.parse(codigo)
    if isinstance(tree, list):
        for stmt in tree:
            interpreter.exec(stmt)
    else:
        interpreter.exec(tree)


if __name__ == "__main__":
    main()