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