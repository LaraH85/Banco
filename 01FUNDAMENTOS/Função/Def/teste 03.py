def soma(a, b):
    print(a + b)

soma(10, 20)
soma(8,5)

def soma(a, b):
    return a + b

resultado = soma(5, 8)
print(resultado)

def calcular(a,b):
    soma = a + b
    produto = a * b
    return soma, produto

soma, produto = calcular(5,3)
print(soma)
print(produto)

def chamada(nome= 'Visitor'):
    print('Hello', nome)

chamada()
chamada('Carlos')

def teste():
    x = 10
    print(x)

name = 'Ana'

def show():
    print(name)

show()