# Trabalho_Compiladores

## Descrição

Este projeto implementa uma linguagem de programação simples, interpretada em Python usando a biblioteca [Lark](https://github.com/lark-parser/lark). A linguagem suporta operações aritméticas, atribuição de variáveis, comandos de impressão (`imprima`), estruturas condicionais (`if`), de repetição (`while`), **strings** (com acentuação), **concatenação de strings** e **comentários**.

## Sintaxe da Linguagem

- **Atribuição:**
  ```
  x = 10
  y = x * 2 + 5
  texto = "Olá, mundo!"
  ```
- **Impressão:**
  ```
  imprima(y)
  imprima("Mensagem com acentuação: çãõé")
  imprima("Oi, " + "Lucas!")
  imprima("Valor: " + 123)
  ```
- **Concatenação de strings:**
  - Use `+` para juntar strings ou strings e números:
    ```
    nome = "Lucas"
    imprima("Olá, " + nome)
    imprima("Resultado: " + 42)
    ```
- **Comentário:**
  - Qualquer texto após `#` na linha é ignorado:
    ```
    imprima("Olá!")  # Isso é um comentário
    ```
- **Condicional:**
  ```
  if x > 0:
      imprima(x)
  ```
- **Repetição:**
  ```
  while x > 0:
      imprima(x)
      x = x - 1
  ```

## Exemplo de Código

Arquivo: `exemplo.mp`
``` 
x = 7
nome = "Lucas"
imprima("Olá, " + nome)
# Exemplo de comentário
imprima(x + 1)
```

## Como Executar

1. **Requisitos:**
   - Python 3.11+
   - Instale a dependência Lark:
     ```
     pip install lark
     ```

2. **Execute um programa da linguagem:**
   ```
   python main.py exemplo.mp
   ```
   O interpretador irá ler e executar o código do arquivo indicado.

3. **Dicas de encoding:**
   - Certifique-se de que seus arquivos de código-fonte estejam salvos em UTF-8 para garantir que acentuação e caracteres especiais funcionem corretamente.
   - O interpretador já lê os arquivos como UTF-8 por padrão.

4. **Extensão de arquivo:**
   Você pode usar qualquer extensão para seus programas (ex: `.mp`, `.minilang`, `.lucas`), desde que o conteúdo siga a sintaxe da linguagem.

## Estrutura do Projeto

- `main.py` — Ponto de entrada. Lê o arquivo-fonte, faz o parsing e executa.
- `grammar.lark` — Define a gramática da linguagem.
- `ast_builder.py` — Constrói a árvore sintática abstrata (AST).
- `interpreter.py` — Executa os comandos da linguagem a partir da AST.
- `exemplo.mp` — Exemplo de código-fonte.

## Gramática Resumida

```
?start: statement+
?statement: assign_stmt | print_stmt | if_stmt | while_stmt
assign_stmt: NAME "=" expr      -> assign
print_stmt: "imprima" "(" expr ")" -> print
if_stmt: "if" expr ":" block     -> if
while_stmt: "while" expr ":" block -> while
block: statement+
?expr: expr "+" term | expr "-" term | term
?term: term "*" factor | term "/" factor | factor
?factor: NUMBER | NAME | ESCAPED_STRING | "(" expr ")"
NAME: /[a-zA-Z_][a-zA-Z0-9_]*/
%import common.NUMBER
%import common.NEWLINE
%import common.WS_INLINE
%import common.ESCAPED_STRING
%ignore WS_INLINE
%ignore NEWLINE
%ignore /#[^\n]*/
```

## Fluxo de Execução

```mermaid
flowchart TD
    A["Arquivo fonte .mp"] --> B["Parser (Lark)"]
    B --> C["ASTBuilder"]
    C --> D["Árvore Sintática"]
    D --> E["Interpreter"]
    E --> F["Saída no terminal"]


