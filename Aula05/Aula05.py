'''
lista = ["carro", "peixe", 123, 111]
novaLista = ["pedra", lista]
print(novaLista)
print(lista[0])
print(novaLista[1])
print(novaLista[1][2])
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])

print(len(lista))
print(len(novaLista))
print(len(novaLista[1]))
print(lista+novaLista)
print(lista*3)
print("peixe" in lista) #Verifica se "peixe" está dentro da lista

lista = ["carrodefabio", "peixe", 123, 111]
print (lista[0])

vetorDeNumeros = [14.55, 67, 89.88, 10, 21.5]
print(min(vetorDeNumeros))
print(max(vetorDeNumeros))
print(sum(vetorDeNumeros))

livros = ['Java', 'SqlServer', 'Delphi', 'Python', 'Java']
livros.append('Android')
print(livros)
print(livros.count("Java"))

listaDeNumeros = [66.25, 333,  -1, 3333, 1, 1234.5]
print(listaDeNumeros.index(-1))

listaDeNumeros.sort()
print(listaDeNumeros)

a = [33,33,33]
b = [33,33,33]
print(a==b)
print(a is b)
b[0] = 3
print(a)
b = a
b[0] = 3
print(a)

c = [10, 20, 30]
d = c[:] #[:]Faz um clone
d[0] = 40
print(d)

tupla = (1,2,3,4); print(tupla)
tupla = (1,); print(tupla)
tupla = (); print(tupla)

tupla = ("João", "e", "Maria")
print(tupla[0])
print(tupla[0:2])

p = "python"
print(p[0:0]);print(p[0:1]);print(p[1:2])
print(p[1:2])
'''

agenda = {"Maria":[988252397, 988442521]}; print(agenda)
print(agenda["Maria"])

agenda = {"Maria":[988252397, 988442521], "Pedro":[988252397, 988442521]}; print(agenda)
print(agenda["Pedro"])