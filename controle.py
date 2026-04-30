pip install colorama

from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Lista com as situações do reservatório
situacoes = [
    "Muito baixo (crítico)",  # Nível 1
    "Baixo",                  # Nível 2
    "Médio",                  # Nível 3
    "Alto",                   # Nível 4
    "Muito alto (alerta)"     # Nível 5
]

# Função que retorna a cor conforme o nível
def cor_por_nivel(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE  # padrão

# Simulação: percorre todos os níveis
for nivel in range(1, 6):
    cor = cor_por_nivel(nivel)
    mensagem = situacoes[nivel - 1]
    print(cor + f"Nível {nivel}: {mensagem}" + Style.RESET_ALL)

