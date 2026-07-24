variavel = input()

def calcular_commits(tarefa_principal):
    print(f"Dividindo a tarefa: '{tarefa_principal}' em 5 commits:\n")
    passos = [
        "1. Estrutura base e arquivos iniciais",
        "2. Implementação da lógica principal",
        "3. Ajustes de estilo e componentes visuais",
        "4. Correção de erros e testes locais",
        "5. Documentação e finalização"
    ]
    for passo in passos:
        print(f"git commit -m '{passo}'")


calcular_commits("Criar tela de login")

altura = float(input("digite sua altura"))

anos =int(input("quantos anos voce tem" :))

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = num1 + num2
print(f"A soma dos dois números é: {soma}")

numero = float(input("Digite um número para dobrar: "))
dobro = numero * 2
print(f"O dobro de {numero} é {dobro}")


texto = input("Digite uma palavra ou frase: ")
tamanho = len(texto)
print(f"O que você digitou tem {tamanho} letras/espaços.")

celsius = float(input("Digite a temperatura em °C: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")

