# Bubble sort simples para 3 valores
x = 3
y = 1
z = 2
if (x > y) {
    t = x
    x = y
    y = t
}
if (y > z) {
    t = y
    y = z
    z = t
}
if (x > y) {
    t = x
    x = y
    y = t
}
imprima(x)
imprima(y)
imprima(z) 