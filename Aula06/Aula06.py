'''
/usr/bin/python3.7 -m pip install numpy
for i in range(9):
    print(i)

for i in range(9, -1, -2):
    print(i)

for caractere in "Trabalho na Quinta":
    print(caractere)

listaNomes = ['Jose', 'Joseval', 'Josevias']

for nome in listaNomes:
    print(nome)

linguagens = ['Python', 'PHP', 'C#', 'PowerBuilder', 'Cobol']
tamanho = len(linguagens) #retorna o tamanho da lista
indices = range(tamanho) #retorna os indices que serão utilizados para acessar a lista

for i in indices:
    print(linguagens[i])

for key, value in enumerate(['p','y','t', 'h', 'o', 'h']):
    print(key, value)

linguagens = ['Python', 'C++', 'C', 'Raskel', 'Cobol']
for key, value in enumerate(linguagens):
    print("A linguaem é: ", value)
    print("O rank da linguagem é: ", key)

from numpy import random

listaDeValores = random.rand(20)
for value in listaDeValores:
    print(value)

lista1 =["q","w","e","r"]
lista2 =["i","u","y","t"]
for v1, v2 in zip(lista1, lista2):
    print (v1, v2)
'''

listaDeNomes = ['André', 'Felipe', 'Oliveira']
for nome in listaDeNomes:
    print(nome)
else:
    print("Todos os nomes foram listados!")
    


