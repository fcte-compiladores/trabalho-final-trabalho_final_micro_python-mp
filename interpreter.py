class Interpreter:
    def __init__(self):
        self.env = {}  # Tabela de variáveis

    def eval(self, node):
        match node:
            case ('number', value):
                return value
            case ('var', name):
                return self.env.get(name, 0)
            case ('string', value):
                return value
            case ('add', left, right):
                l = self.eval(left)
                r = self.eval(right)
                if isinstance(l, str) or isinstance(r, str):
                    return str(l) + str(r)
                return l + r
            case ('sub', left, right):
                return self.eval(left) - self.eval(right)
            case ('mul', left, right):
                return self.eval(left) * self.eval(right)
            case ('div', left, right):
                return self.eval(left) / self.eval(right)
            case _:
                raise ValueError(f"Nó inválido: {node}")

    def exec(self, node):
        match node:
            case ('assign', name, expr):
                self.env[name] = self.eval(expr)
            case ('print', expr):
                print(self.eval(expr))
