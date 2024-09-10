# Verifique se uma palavra é um palíndromo (mesma leitura de trás para frente)
palavra = input("Digite uma palavra: ")

# ::-1 é um fatiamento(slicing) da string. 
# o primeiro : indica que queremos a string toda e :-1 indica que queremos ela invertida
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo!")

# Slicing: maneira de acessar subseção de uma lista, string ou qualquer sequência.
# sintaxe: sequencia[inicio:fim:passo]