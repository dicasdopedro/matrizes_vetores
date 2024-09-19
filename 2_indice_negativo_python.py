# Criando um vetor com números
numeros = [10, 20, 30, 40, 50]

# Acessando elementos com índices negativos
print(numeros[-1])  # Saída: 50 (último elemento)
print(numeros[-2])  # Saída: 40 (penúltimo elemento)
print(numeros[-3])  # Saída: 30 (antepenúltimo elemento)

# Alterando o valor do último elemento usando índice negativo
numeros[-1] = 100
print(numeros)  # Saída: [10, 20, 30, 40, 100]