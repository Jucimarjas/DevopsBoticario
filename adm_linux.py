# importando bibliotecas para automação de Processos e tarefas
import subprocess as sp
import os
import time
from datetime import datetime

# Função para instalar pacotes essenciais do linux
def install_essential_packages():
    packages = ["vim", "curl", "wget", "htop", "git"]

    for package in packages:
        print(f"Instalando {package}...")
        sp.run(["sudo", "apt", "install", "-y", package])

    print("Pacotes essenciais instalados com sucesso")

# atualização dos pacotes    
def update_packages():
    try:
        # Executa o comando para atualizar os pacotes
        sp.run(['sudo', 'apt', 'update', '-y'], check=True)
        sp.run(['sudo', 'apt', 'upgrade', '-y'], check=True)
        print("Pacotes atualizados com sucesso!")
    except sp.CalledProcessError as e:
        print(f"Erro ao atualizar pacotes: {e}")

# Função para limpar tela de seleção
def limpar_tela():
    print("Limpando a tela ......")
    time.sleep(8)
    print("Fim da Automatização")
    time.sleep(6)
    os.system("clear")    
    
# Chamando Funções    
install_essential_packages()
update_packages()
limpar_tela()

def registrar_log_no_desktop(mensagem, nome_arquivo="log.txt"):
    # Diretório do desktop do usuário
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    caminho_arquivo = os.path.join(desktop, nome_arquivo)
    
    # Formatar a mensagem do log
    log_message = f"{datetime.now()} - {mensagem}\n"
    
    # Escrever no arquivo de log
    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(log_message)

    print(f'Log registrado com sucesso no arquivo "{nome_arquivo}" no desktop!')

# Exemplo de uso:
mensagem = "O script foi executado com sucesso."
registrar_log_no_desktop(mensagem)
