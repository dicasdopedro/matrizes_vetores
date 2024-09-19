# Criando um vetor com números
numeros = [10, 20, 30, 40, 50, 60, 70, 80]

# Fatiando o vetor (pegando do índice 2 até o 5, sem incluir o 5)
sub_lista = numeros[2:5]
print(sub_lista)  # Saída: [30, 40, 50]

# Fatiando o vetor (pegando os três primeiros elementos)
primeiros_tres = numeros[:3]
print(primeiros_tres)  # Saída: [10, 20, 30]

# Fatiando o vetor (pegando os três últimos elementos)
ultimos_tres = numeros[-3:]
print(ultimos_tres)  # Saída: [60, 70, 80]

# Fatiando o vetor (pegando todos os elementos com salto de 2)
com_salto = numeros[::2]
print(com_salto)  # Saída: [10, 30, 50, 70]