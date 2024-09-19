# Criando uma matriz 2x3 (2 linhas, 3 colunas)
minha_matriz = [
    [1, 2, 3],  # Primeira linha
    [4, 5, 6]   # Segunda linha
]

# Acessando o elemento da primeira linha e segunda coluna
elemento = minha_matriz[0][1]
print(elemento)  # Saída: 2

# Alterando o elemento da segunda linha, terceira coluna
minha_matriz[1][2] = 9
print(minha_matriz)  # Saída: [[1, 2, 3], [4, 5, 9]]

# Percorrendo e imprimindo cada elemento da matriz
for linha in minha_matriz:
    for elemento in linha:
        print(elemento, end=" ")  # Imprime na mesma linha
    print()  # Pula para a próxima linha

maior = minha_matriz[0][0]
for linha in minha_matriz:
    for elemento in linha:
        if elemento > maior:
            maior = elemento
print(maior)  # Saída: 9

