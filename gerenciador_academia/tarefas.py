# Regras de negócio e funções principais do sistema de Academia

from dados import (
    alunos,
    proximo_id,
    fila_atendimento,
    status,
    modalidades
)

from utils import linha, titulo

# Funçao para cadastrar um novo aluno
def cadastrar_aluno():

    global proximo_id

    titulo("Cadastrar Novo Aluno")
    
    nome = input("Digite o nome do aluno: ")
    modalidade = escolha_modalidade()
    
    dias = input("Dias por semana de treino (ex: 3): ")
    objetivo = input("Objetivo principal (ex: Hipertrofia, Emagrecimento): ")

    dados_alunos = {
        "id": proximo_id,
        "nome": nome,
        "modalidade": modalidade,
        "dias_por_semana": dias,
        "objetivo": objetivo,
        "status": status[0],
        "sessoes": [] 
    }

    alunos.append(dados_alunos)
    proximo_id += 1

    titulo("Aluno cadastrado com sucesso!")
    print(f"ID: {dados_alunos['id']}")
    print(f"Nome: {nome}")
    print(f"Modalidade: {modalidade}")
    print(f"Dias/semana: {dias}")
    print(f"Objetivo: {objetivo}")
    linha()

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
            print(f"Opção inválida!, Digite uma opção correta.")

# Função de consultar alunos registrados (Ativos)
def alunos_registrados():
    titulo("Registro de Alunos Ativos")

    if not alunos:
        print("Nenhum aluno cadastrado ainda.")
        return

    encontrados = False

    for aluno in alunos:
        if aluno['status'] == "Ativo":
            encontrados = True
            print(f"ID: {aluno['id']}")
            print(f"Nome: {aluno['nome']}")
            print(f"Modalidade: {aluno['modalidade']}")
            print(f"Dias por Semana: {aluno['dias_por_semana']}")
            print(f"Objetivo: {aluno['objetivo']}")
            print(f"Status: {aluno['status']}")
            linha()

    if not encontrados:
        print("Nenhum aluno ativo no momento.")

# função de adicionar aluno na Fila de Atendimento
def adicionar_na_fila():
    titulo("Adicionar Aluno na Fila de Atendimento")
    
    alunos_registrados()
    
    if not alunos:
        print("Não há alunos cadastrados!")
        return 
    
    try:
        id_digitado = int(input("\nDigite o ID do aluno para adicionar na fila: "))
    except ValueError:
        print("Digite um número válido!")
        return
    
    aluno = buscar_aluno_por_id(id_digitado)
    
    if aluno is None:
        print("Aluno não encontrado!")
        return
    
    if aluno in fila_atendimento:
        print("Este aluno já está na fila de atendimento!")
        return
    
    fila_atendimento.append(aluno)
    print(f"Aluno {aluno['nome']} (ID: {aluno['id']}) adicionado na fila com sucesso!")

# Função de chamar o proximo da fila
def chamar_proximo_atendimento():
    titulo("Chamar Próximo da Fila de Atendimento")
    
    if not fila_atendimento:
        print("A fila de atendimento está vazia!")
        return
    
    aluno = fila_atendimento.pop(0)
    
    print(f"Chamando aluno:")
    print(f"ID: {aluno['id']}")
    print(f"Nome: {aluno['nome']}")
    print(f"Modalidade: {aluno['modalidade']}")
    print(f"Objetivo: {aluno['objetivo']}")
    
    print("Aluno chamado com sucesso! Próximo da fila.")

# Função de registrar check-in
def registrar_checkin():
    titulo("Registrar Check-in / Sessão de Treino")
    
    alunos_registrados()
    
    if not alunos:
        print("Não há alunos cadastrados!")
        return
    
    try:
        id_digitado = int(input("\nDigite o ID do aluno para registrar check-in: "))
    except ValueError:
        print("Digite um número válido!")
        return
    
    aluno = buscar_aluno_por_id(id_digitado)
    
    if aluno is None:
        print("Aluno não encontrado!")
        return
    
    data = input("Data do treino (DD/MM/AAAA): ")
    observacao = input("Observação do treino (opcional): ")
    
    sessao = {
        "data": data,
        "observacao": observacao
    }
    
    aluno['sessoes'].append(sessao)
    
    print(f"Check-in registrado com sucesso para {aluno['nome']}!")
    print(f"Total de sessões deste aluno: {len(aluno['sessoes'])}")    

# Função para ver histórico de sessões
def ver_historico_sessoes():
    titulo("Histórico de Sessões de Treino")
    
    alunos_registrados()
    
    if not alunos:
        print("Aluno não encontrado!")
        return
    
    try:
        id_digitado = int(input("Digite o ID do aluno para ver histórico: "))
    except ValueError:
        print("Digite um número válido!")
        return
    
    aluno = buscar_aluno_por_id(id_digitado)
    
    if aluno is None:
        print("Aluno não encontrado!")
        return
    
    titulo(f"Histórico de {aluno['nome']}")
    
    if not aluno['sessoes']:
        print("Este aluno ainda não possui sessões registradas.")
        return
    
    for i, sessao in enumerate(reversed(aluno['sessoes']), start=1):
        print(f"Sessão #{i}")
        print(f"Data: {sessao['data']}")
        print(f"Observação: {sessao['observacao']}")
        print("-" * 40)
    
    print(f"Total de sessões: {len(aluno['sessoes'])}")

# Função que busca aluno pelo o ID
def buscar_aluno_por_id(id_procurado):
    for cada_aluno in alunos:
        if id_procurado == cada_aluno['id']:
            return cada_aluno
    return None        
