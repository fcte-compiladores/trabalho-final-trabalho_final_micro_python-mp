import subprocess
import sys
from pathlib import Path
import os

BASE_DIR = Path(__file__).parent
PROJECT_ROOT = BASE_DIR.parent
MAIN = str(PROJECT_ROOT / "main.py")

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

def run_code(file):
    result = subprocess.run([PYTHON_EXEC, MAIN, str(BASE_DIR / file)], capture_output=True, encoding="utf-8")
    if result.returncode != 0:
        print(f"STDERR para {file}:\n{result.stderr}")
    return result.stdout

def test_cases():
    for fname, expected in TEST_CASES:
        output = run_code(fname)
        assert output == expected, f"Erro no teste {fname}:\nEsperado:\n{expected}\nObtido:\n{output}" 