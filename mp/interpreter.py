class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class Interpreter:
    def __init__(self):
        self.env = {}  # Tabela de variáveis
        self.functions = {}  # Tabela de funções

    def eval(self, node, local_env=None):
        env = local_env if local_env is not None else self.env
        match node:
            case ('number', value):
                return value
            case ('var', name):
                return env.get(name, 0)
            case ('string', value):
                return value
            case ('add', left, right):
                l = self.eval(left, env)
                r = self.eval(right, env)
                if isinstance(l, str) or isinstance(r, str):
                    return str(l) + str(r)
                return l + r
            case ('sub', left, right):
                return self.eval(left, env) - self.eval(right, env)
            case ('mul', left, right):
                return self.eval(left, env) * self.eval(right, env)
            case ('div', left, right):
                return self.eval(left, env) / self.eval(right, env)
            case ('eq', left, right):
                return self.eval(left, env) == self.eval(right, env)
            case ('ne', left, right):
                return self.eval(left, env) != self.eval(right, env)
            case ('gt', left, right):
                return self.eval(left, env) > self.eval(right, env)
            case ('lt', left, right):
                return self.eval(left, env) < self.eval(right, env)
            case ('ge', left, right):
                return self.eval(left, env) >= self.eval(right, env)
            case ('le', left, right):
                return self.eval(left, env) <= self.eval(right, env)
            case ('and', left, right):
                return bool(self.eval(left, env)) and bool(self.eval(right, env))
            case ('or', left, right):
                return bool(self.eval(left, env)) or bool(self.eval(right, env))
            case ('not', value):
                return not bool(self.eval(value, env))
            case ('func_call', name, args):
                if name not in self.functions:
                    raise ValueError(f"Função '{name}' não definida.")
                func_params, func_block = self.functions[name]
                if len(args) != len(func_params):
                    raise ValueError(f"Função '{name}' espera {len(func_params)} argumentos, recebeu {len(args)}.")
                local = dict(zip(func_params, [self.eval(arg, env) for arg in args]))
                stmts = func_block if isinstance(func_block, list) else [func_block]
                try:
                    for stmt in stmts:
                        self.exec(stmt, local)
                except ReturnException as ret:
                    return ret.value
                return None
            case _:
                raise ValueError(f"Nó inválido: {node}")

    def exec(self, node, local_env=None):
        env = local_env if local_env is not None else self.env
        match node:
            case ('assign', name, expr):
                env[name] = self.eval(expr, env)
            case ('print', expr):
                print(self.eval(expr, env))
            case ('func_def', name, params, block):
                stmts = block.children if hasattr(block, 'children') else (block if isinstance(block, list) else [block])
                self.functions[name] = (params, stmts)
            case ('return', expr):
                value = self.eval(expr, env)
                raise ReturnException(value)
            case _:
                # Suporte a blocos (lista de statements)
                if isinstance(node, list):
                    for stmt in node:
                        self.exec(stmt, env)
                else:
                    raise ValueError(f'Nó inválido: {node}')
