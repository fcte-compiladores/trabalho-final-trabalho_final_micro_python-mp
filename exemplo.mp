 x = 7
    y = x * 3 + 1
    imprima(y)

a = "Olá, mundo!"
imprima(a)
imprima("Teste de string")

a = "Olá, "
b = "mundo!"
imprima(a + b)  # Saída: Olá, mundo!
imprima("Valor: " + 123)  # Saída: Valor: 123

a = 5
b = 10
imprima(a < b)         # True
imprima(a == 5 and b != 7)  # True
imprima(not (a > b))   # True
imprima(a > b)


x = 3
if x > 5:
    imprima("maior que 5")
else:
    imprima("menor ou igual a 5")

def soma(a, b):
    return a + b

x = soma(2, 3)
imprima(x)  # Saída: 5
