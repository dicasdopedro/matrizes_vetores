# Criando um vetor com nomes de frutas
frutas = ["maçã", "banana", "laranja", "uva", "manga"]

# Acessando elementos do vetor
print(frutas[0])  # Saída: maçã
print(frutas[2])  # Saída: laranja

# Alterando o terceiro elemento
frutas[2] = "abacaxi"
print(frutas)  # Saída: ['maçã', 'banana', 'abacaxi', 'uva', 'manga']

# Adicionando um novo elemento ao vetor
frutas.append("melancia")
print(frutas)  # Saída: ['maçã', 'banana', 'abacaxi', 'uva', 'manga', 'melancia']

# Removendo um elemento do vetor
frutas.remove("uva")
print(frutas)  # Saída: ['maçã', 'banana', 'abacaxi', 'manga', 'melancia']