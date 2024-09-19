# Criando um vetor com as notas dos alunos
notas = [7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 6.0, 10.0]

# 1. Calculando a média das notas
media = sum(notas) / len(notas)
print(f"Média das notas: {media:.2f}")  # Saída: Média das notas: 7.81

# 2. Encontrando a maior e a menor nota
maior_nota = max(notas)
menor_nota = min(notas)
print(f"Maior nota: {maior_nota}")  # Saída: Maior nota: 10.0
print(f"Menor nota: {menor_nota}")  # Saída: Menor nota: 6.0

# 3. Contando quantos alunos tiveram notas acima de 7.0
notas_acima_7 = len([nota for nota in notas if nota > 7.0])
print(f"Número de alunos com notas acima de 7.0: {notas_acima_7}")  # Saída: 6

# 4. Verificando quantos alunos tiveram nota 10
alunos_nota_10 = notas.count(10.0)
print(f"Número de alunos com nota 10: {alunos_nota_10}")  # Saída: 1