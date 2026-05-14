# Regras de negócio e funções principais do sistema de Academia

from dados import (
    alunos,
    proximo_id,
    fila_atendimento,
    status,
    modalidades
)

from utils import linha,titulo

# Funçao para cadastrar um novo aluno
def cadastrar_aluno():
    titulo("Cadastrar Novo Aluno")
    
    nome = input("Digite o nome do aluno: ")
    modalidade = escolha_modalidade()
    
    dias = input("Dias por semana de treino (ex: 3): ")
    objetivo = input("Objetivo principal (ex: Hipertrofia, Emagrecimento): ")

    dados_alunos = {
        "id": len(alunos) + 1,
        "nome": nome,
        "modalidade": modalidade,
        "dias_por_semana": dias,
        "objetivo": objetivo,
        "status": status[0],
        "sessoes": [] 
    }

    alunos.append(dados_alunos)
    fila_atendimento.append(dados_alunos)

    titulo("Aluno cadastrado com sucesso!")
    print(f"ID: {dados_alunos["id"]}")
    print(f"Nome: {nome}")
    print(f"Modalidade: {modalidade}")
    print(f"Dias/semana: {dias}")
    print(f"Objetivo: {objetivo}")

# Funçao para escolha de modalidades
def escolha_modalidade():
    while True:
        titulo("Modalidades Disponíveis")
        
        for i in range(len(modalidades)):
            print(f"{i+1}. {modalidades[i]}")
        
        opcao = input("Digite o número da modalidade: ")

        if opcao == "1":
            return modalidades[0]
        elif opcao == "2":
            return modalidades[1]
        elif opcao == "3":
            return modalidades[2]
        elif opcao == "4":
            return modalidades[3]
        elif opcao == "5":
            return modalidades[4]
        else:
            print(f"Opção inválida!, Digite a opção correta.")

# Função de consultar alunos registrados
def alunos_registrados():
    titulo("Alunos Registrados")

    for i, aluno in enumerate(alunos, start=1):
        print(f"""
        ID: {aluno['id']}
        Nome: {aluno['nome']}
        Modalidade: {aluno['modalidade']}
        Dias por Semana: {aluno['dias_por_semana']}
        Objetivo: {aluno['objetivo']}
        Status: {aluno['status']}
        """)
        linha()

