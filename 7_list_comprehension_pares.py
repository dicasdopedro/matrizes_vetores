# Criando um vetor com números de 1 a 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando List Comprehension para criar um novo vetor com apenas os números pares
pares = [x for x in numeros if x % 2 == 0]

print(pares)  # Saída: [2, 4, 6, 8, 10]