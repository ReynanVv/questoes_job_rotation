string_original = "Olá, mundo!"
string_invertida = ""

# Percorre a string original da direita para a esquerda e adiciona cada caractere na nova string invertida
for i in range(len(string_original)-1, -1, -1):
    string_invertida += string_original[i]

print("String original:", string_original)
print("String invertida:", string_invertida)
