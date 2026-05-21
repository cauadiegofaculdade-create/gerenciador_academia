# ponto de entrada — menu e navegação
from utils import titulo
from tarefas import (
    cadastrar_aluno, 
    alunos_registrados, 
    adicionar_na_fila,
    chamar_proximo_atendimento,
    registrar_checkin,
    ver_historico_sessoes
)

# Menu de navegação
def mostrar_menu():
    titulo("Gerenciador de Academia / Treinos")
    print("1. Cadastrar Novo Aluno")
    print("2. Listar Alunos Ativos")
    print("3. Adicionar Aluno na Fila de Atendimento")
    print("4. Chamar Próximo da Fila")
    print("5. Registrar Check-in / Sessão")
    print("6. Ver Histórico de Sessões")
    print("7. Sair")

while True:
    mostrar_menu()
    
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        alunos_registrados()
    elif opcao == "3":
        adicionar_na_fila()
    elif opcao == "4":
        chamar_proximo_atendimento()
    elif opcao == "5":
        registrar_checkin()
    elif opcao == "6":
        ver_historico_sessoes()
    elif opcao == "7":
        print("Saindo do programa... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")

    input("Pressione ENTER para continuar...")     

