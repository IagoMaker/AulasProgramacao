'''
def soma(num1, num2):
    somatorio = num1 + num2
    print("SOMA = ", somatorio)

soma(2,5)

def mensagemDeErro():
    """Função chamada sempre que houver um erro"""
    print("Erro!!!")
    print("Infelizmente você terá que fazer tudo novamente")
    print("Nada do que você fez está certo!!")

mensagemDeErro()
mensagemDeErro()
mensagemDeErro()

def soma(x,y):
    return x+y

primeiroParametro = int(input("Digite o primeiro numero: "))
segundoParametro = int(input("Digite o segundo numero: "))

y = soma(primeiroParametro, segundoParametro)
print(y)

def arbitrary(x,y, *more):
    """Função com dois ou mais parâmetros"""
    print("x = ", x, ", y = ", y)
    print("Parâmetros arbitrários: ", more)

arbitrary(2,3)
arbitrary(2,3, "oi", "xau")

def my_func():
    x = 10
    print("Value inside function: ", x)

x = 20
my_func()
print("Value outside function: ", x)

def nomesPaises(Paises = "Noruega"):
    print("Eu vim da: ", Paises)

nomesPaises("Venezuela")
nomesPaises()

def listaDeComidas(comidas):
    """Programa para imprimir a lista de comidas passadas"""
    for comida in comidas:
        print(comida)

listaDeComidas(["Banana", "Maçã", "Pera", "Abacaxi"])

def recursao(k):
    if (k > 0):
        resultado = k + recursao(k-1)
        print(resultado)
    else:
        resultado = 0
    return resultado

print(recursao(6))
'''
cube = lambda x: x*x*x
print(cube(7))
