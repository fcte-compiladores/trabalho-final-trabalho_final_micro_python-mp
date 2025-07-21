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

    def eq(self, items):
        return ('eq', items[0], items[1])
    def ne(self, items):
        return ('ne', items[0], items[1])
    def gt(self, items):
        return ('gt', items[0], items[1])
    def lt(self, items):
        return ('lt', items[0], items[1])
    def ge(self, items):
        return ('ge', items[0], items[1])
    def le(self, items):
        return ('le', items[0], items[1])
    def and_op(self, items):
        return ('and', items[0], items[1])
    def or_op(self, items):
        return ('or', items[0], items[1])
    def not_op(self, items):
        return ('not', items[0])

    def func_def(self, items):
        name = str(items[0])
        params = items[1] if isinstance(items[1], list) else []
        block = items[2]
        stmts = block if isinstance(block, list) else [block]
        return ('func_def', name, params, stmts)
    def params(self, items):
        return [str(i) for i in items]
    def func_call(self, items):
        name = str(items[0])
        args = items[1] if len(items) > 1 else []
        return ('func_call', name, args)
    def args(self, items):
        return items
    def return_stmt(self, items):
        return ('return', items[0])

    def if_(self, items):
        cond = items[0]
        then_block = items[1].children if hasattr(items[1], 'children') else (items[1] if isinstance(items[1], list) else [items[1]])
        if len(items) == 3 and items[2] is not None:
            else_block = items[2].children if hasattr(items[2], 'children') else (items[2] if isinstance(items[2], list) else [items[2]])
        else:
            else_block = None
        return ('if', cond, then_block, else_block)

    def while_(self, items):
        cond = items[0]
        block = items[1].children if hasattr(items[1], 'children') else (items[1] if isinstance(items[1], list) else [items[1]])
        return ('while', cond, block)

    def do_while_stmt(self, items):
        block = items[0].children if hasattr(items[0], 'children') else (items[0] if isinstance(items[0], list) else [items[0]])
        cond = items[1]
        return ('do_while', block, cond)

    def statement(self, items):
        # Retorna apenas o primeiro item que é o statement real
        for item in items:
            if not hasattr(item, 'type') or item.type not in ('SEMICOLON', 'LBRACE', 'RBRACE'):
                return item
        return None

    def block(self, items):
        # Filtra apenas statements válidos
        return [item for item in items if not hasattr(item, 'type') or item.type not in ('SEMICOLON', 'LBRACE', 'RBRACE')]

    def start(self, items):
        return list(items)