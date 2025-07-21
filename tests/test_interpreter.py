import subprocess
import sys
from pathlib import Path
import os
import pytest

BASE_DIR = Path(__file__).parent
PROJECT_ROOT = BASE_DIR.parent
MAIN = str(PROJECT_ROOT / "mp" / "cli.py")

# Use o Python do venv se existir
VENV_PY = PROJECT_ROOT / ".venv" / "Scripts" / "python.exe"
PYTHON_EXEC = str(VENV_PY) if VENV_PY.exists() else sys.executable

# Lista de casos de teste: (nome do arquivo, saída esperada)
TEST_CASES = [
    ("aritmetica.mp", "22.0\n"),
    ("string.mp", '"Olá, mundo!"\n"Teste de string"\n'),
    ("concat.mp", '"Olá, ""mundo!"\n"Valor: "123.0\n'),
    ("comparacao.mp", "True\nFalse\nTrue\n"),
    ("logicos.mp", "True\nTrue\n"),
    ("comentario.mp", '"Olá!"\n'),
    ("funcao.mp", "5.0\n"),
]

@pytest.fixture(scope="module")
def python_exec():
    return PYTHON_EXEC

@pytest.fixture(scope="module")
def main_script():
    return MAIN

@pytest.mark.parametrize("fname,expected", TEST_CASES)
def test_interpreter_cases(fname, expected, python_exec, main_script):
    file_path = str(BASE_DIR / fname)
    result = subprocess.run([python_exec, "-X", "utf8", "-m", "mp.cli", file_path], capture_output=True, encoding="utf-8", errors="replace")
    assert result.returncode == 0, f"Erro ao executar {fname}:\nSTDERR:\n{result.stderr}"
    assert result.stdout == expected, (
        f"Erro no teste {fname}:\n"
        f"Esperado:\n{expected}\n"
        f"Obtido:\n{result.stdout}"
    )

def test_no_duplicate_cases():
    seen = set()
    for fname, _ in TEST_CASES:
        assert fname not in seen, f"Arquivo de teste duplicado: {fname}"
        seen.add(fname)

def test_if_else(capsys):
    from mp.cli import ASTBuilder, Interpreter
    from lark import Lark
    import os
    grammar_path = os.path.join(os.path.dirname(__file__), '..', 'mp', 'grammar.lark')
    parser = Lark.open(grammar_path, parser='lalr', start='start')
    code = '''
    x = 10
    if x > 5:
        imprima("maior")
    else:
        imprima("menor")
    '''
    tree = parser.parse(code)
    ast = ASTBuilder().transform(tree)
    interpreter = Interpreter()
    interpreter.exec(ast)
    captured = capsys.readouterr()
    assert "maior" in captured.out

if __name__ == "__main__":
    subprocess.run(["python", "-m", "pytest", "tests/test_interpreter.py"])