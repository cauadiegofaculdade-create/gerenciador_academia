# ponto de entrada — menu e navegação
from utils import titulo
from tarefas import cadastrar_aluno,alunos_registrados

# Menu de navegação
def mostrar_menu():
    titulo("Gerenciador de Academia / Treinos")
    print("1. Cadastrar Aluno")
    print("2. Alunos Registrados")
    print("3. Sair")

while True:
    mostrar_menu()

    opcao = input("Digite uma opção: ")
    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2": 
        alunos_registrados()   
    elif opcao == "3":
        print("Saindo do Programa...")
        break
    else:
        print("Opção inválida!")       

