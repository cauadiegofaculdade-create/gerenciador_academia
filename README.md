# Gerenciador de Academia / Treinos

**Disciplina:** Programação de Computadores  
**Professora:** Andrea Ono Sakai  
**Tema Escolhido:** Academia / Treinos (Avançado)  
**Integrantes:** Cauã Diego e Murilo  
**Período:** 2026/1

---

# Requisitos Atendidos

## Obrigatórios:
- [x] Cadastrar aluno (nome, modalidade, dias/semana, objetivo)
- [x] Listar alunos ativos com status
- [x] Fila de atendimento presencial (FIFO)

## Bônus Implementados:
- [x] Registrar Check-in de treino (Pilha LIFO)
- [x] Ver Histórico de Sessões (com `reversed()`)
- [x] Contar total de sessões por aluno

---

# Conceitos Utilizados

## 1. Fila (FIFO)
Utilizamos a `fila_atendimento` para controlar a ordem de atendimento presencial.  
O aluno que entra primeiro é o primeiro a ser chamado.

```python
fila_atendimento.append(aluno)        # entra no final
aluno = fila_atendimento.pop(0)      # sai do início (FIFO)
```

---

## Cada aluno tem uma pilha de sessões. O último check-in registrado aparece primeiro no histórico.

```python
aluno['sessoes'].append(sessao)                    # empilha
for sessao in reversed(aluno['sessoes']):         # mostra do mais recente ao mais antigo Dicionário
```

## Cada aluno é um dicionário que agrupa todas as suas informações.

```python
aluno = {
    "id": 1,
    "nome": "João Silva",
    "modalidade": "Musculação",
    "status": "Ativo",
    "sessoes": []   # pilha de check-ins
}
```

## Lista e Tupla

```python
Lista: Usada em alunos = [] e fila_atendimento = [] por ser mutável.
Tupla: Usada em status e modalidades por ser imutável (protege valores fixos).
```

## Modularização
# O projeto foi dividido em 4 arquivos:

- dados.py → Variáveis globais
- utils.py → Funções auxiliares
- tarefas.py → Regras de negócio
- main.py → Menu principal

# Como Executar
- Tenha Python 3.10+ instalado
- Coloque todos os arquivos na mesma pasta
- Execute: python main.py

## Funcionalidades Implementadas
# Obrigatórias:

- Cadastrar aluno (nome, modalidade, dias/semana, objetivo)
- Listar alunos ativos com status
- Fila de atendimento presencial (FIFO)

# Bônus:

- Registrar check-in de treino
- Ver histórico de sessões (Pilha LIFO)
- Contar total de sessões por aluno

## Dificuldades e Aprendizados

- Durante o projeto tive dificuldade para entender como usar pilha dentro do dicionário do aluno e como gerenciar a fila FIFO sem adicionar todos os alunos automaticamente.
- Aprendi a importância da organização, dividir o código em vários arquivos ajudou muito na manutenção. Também melhorei bastante o uso de funções, dicionários e como eu exergava o jeito prático de FIFO e LIFO.
- Me ajudou muito aprender a reutilizar funções como `buscar_aluno_por_id()` em várias partes do sistema. No final, o projeto me ajudou a entender bem os conceitos vistos nas aulas.
