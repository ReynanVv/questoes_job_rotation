# Solicita ao usuário um número para verificar se pertence à sequência de Fibonacci
num = int(input(
    "Digite um número inteiro para verificar se pertence à sequência de Fibonacci: "))

def fibonacci(num):
    # Define os dois primeiros valores da sequência
    a, b = 0, 1
    # Inicia um loop para calcular os próximos valores da sequência enquanto estes forem menores ou iguais ao número informado
    while b <= num:
        # Se o número informado for igual a um dos valores da sequência, imprime uma mensagem e encerra o programa
        if b == num:
            print(f"O número {num} pertence à sequência de Fibonacci.")
            break
        # Calcula o próximo valor da sequência e atualiza os valores de a e b
        a, b = b, a + b
    # Se o número informado for maior do que o último valor da sequência, imprime uma mensagem informando que não pertence à sequência
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

fibonacci(num=num)
