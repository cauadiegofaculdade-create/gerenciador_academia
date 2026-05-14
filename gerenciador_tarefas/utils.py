# funções auxiliares reutilizáveis

# Linha separadora visual
def linha ():
    print("=" * 50)

# Exibe um título centralizado com linhas acima e abaixo
def titulo(texto):
        linha()
        print(texto.center(50))
        linha()