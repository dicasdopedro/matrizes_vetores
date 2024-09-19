# Criando um vetor com números
meu_vetor = [10, 20, 30, 40, 50]

# Acessando o primeiro e o terceiro elemento do vetor
primeiro_elemento = meu_vetor[0]
terceiro_elemento = meu_vetor[2]
print(primeiro_elemento)  # Saída: 10
print(terceiro_elemento)  # Saída: 30

# Mudando o segundo elemento do vetor
meu_vetor[1] = 25
print(meu_vetor)  # Saída: [10, 25, 30, 40, 50]

# Adicionando um elemento ao vetor
meu_vetor.append(60)
print(meu_vetor)  # Saída: [10, 25, 30, 40, 50, 60]

# Removendo o valor 30
meu_vetor.remove(30)
print(meu_vetor)  # Saída: [10, 25, 40, 50, 60]

# Removendo o segundo elemento (índice 1)
del meu_vetor[1]
print(meu_vetor)  # Saída: [10, 40, 50, 60]

# Imprimindo cada elemento do vetor
for elemento in meu_vetor:
    print(elemento)

    soma = 0
for elemento in meu_vetor:
    soma += elemento
print(soma)  # Saída: 160 (soma dos elementos de [10, 40, 50, 60])
