import json
import os
from time import sleep

# --- CONFIGURAÇÃO DE CORES (ANSI ESCAPE CODES) ---
RESET = '\033[0m'
NEGRITO = '\033[1m'

VERMELHO = '\033[31m'
VERDE = '\033[32m'
AMARELO = '\033[33m'
AZUL = '\033[34m'
MAGENTA = '\033[35m'
CIANO = '\033[36m'

# --- SISTEMA DE ARQUIVOS (PERSISTÊNCIA) ---
ARQUIVO_DADOS = 'banco_de_dados.json'

pessoas_padrao = [
    {'nome': 'Ana Paula Vieira', 'idade': 32},
    {'nome': 'Cláudio Mendonça', 'idade': 18},
    {'nome': 'Gustavo Guanabara', 'idade': 41},
    {'nome': 'Maria Clara Peixoto', 'idade': 65},
    {'nome': 'Maurício Souza', 'idade': 19},
    {'nome': 'Nilce Pedrosa', 'idade': 43},
    {'nome': 'Pedro Gonçalves', 'idade': 18},
    {'nome': 'Rafael Albuquerque', 'idade': 38},
    {'nome': 'Renata Soares', 'idade': 13},
    {'nome': 'Zuleide Lima', 'idade': 55},
    {'nome': 'Pedro Paulo Pereira', 'idade': 30}
]

def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        salvar_dados(pessoas_padrao)
        return pessoas_padrao
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, IOError):
        print(f"{VERMELHO}Erro ao ler o banco de dados. Recarregando dados padrão.{RESET}")
        return pessoas_padrao

def salvar_dados(lista_pessoas):
    try:
        with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
            json.dump(lista_pessoas, arquivo, indent=4, ensure_ascii=False)
    except IOError:
        print(f"{VERMELHO}Erro crítico: Não foi possível salvar os dados no disco!{RESET}")

# Inicializa o banco de dados
pessoas = carregar_dados()

# --- LOOP PRINCIPAL ---
while True:
    print(f"{AZUL}--" * 20 + f"{RESET}")
    print(f"{NEGRITO}{CIANO}{'MENU PRINCIPAL':^40}{RESET}")
    print(f"{AZUL}--" * 20 + f"{RESET}")
    print(f"{AMARELO}1{RESET} - {NEGRITO}Ver pessoas cadastradas{RESET}")
    print(f"{AMARELO}2{RESET} - {NEGRITO}Cadastrar novas pessoas{RESET}")
    print(f"{AMARELO}3{RESET} - {NEGRITO}Remover uma pessoa{RESET}")  # Nova opção
    print(f"{AMARELO}4{RESET} - {NEGRITO}Sair do sistema{RESET}")
    print(f"{AZUL}--" * 20 + f"{RESET}")
    
    opcao = input(f'{NEGRITO}Escolha uma opção: {RESET}').strip()
    
    if opcao == '1':
        print(f"{CIANO}-" * 40 + f"{RESET}")
        print(f"{NEGRITO}{CIANO}{'PESSOAS CADASTRADAS':^40}{RESET}")
        print(f"{CIANO}-" * 40 + f"{RESET}")
        
        if not pessoas:
            print(f"{AMARELO}{'Nenhuma pessoa cadastrada.':^40}{RESET}")
        else:
            for p in pessoas:
                print(f"{NEGRITO}{p['nome']:<25}{RESET} {AMARELO}{p['idade']:>5}{RESET} anos")
            
        print(f"{CIANO}-" * 40 + f"{RESET}")
        sleep(2)
    
    elif opcao == '2':
        print(f"{VERDE}-" * 40 + f"{RESET}")
        print(f"{NEGRITO}{VERDE}{'NOVO CADASTRO':^40}{RESET}")
        print(f"{VERDE}-" * 40 + f"{RESET}")
        
        nome = input(f'{NEGRITO}Nome: {RESET}').strip()
        # Validação rígida para evitar números ou strings vazias no nome
        while not nome or not nome.replace(' ', '').isalpha():
            print(f'{VERMELHO}Erro! O nome deve conter apenas letras e não pode ficar em branco.{RESET}')
            nome = input(f'{NEGRITO}Nome: {RESET}').strip()
            
        while True:
            try:
                idade = int(input(f'{NEGRITO}Idade: {RESET}'))
                if idade < 0 or idade > 120:
                    print(f'{VERMELHO}ERRO! Digite uma idade válida (entre 0 e 120).{RESET}')
                    continue
                break
            except ValueError:
                print(f'{VERMELHO}Erro! Por favor, digite apenas números inteiros na idade.{RESET}')
        
        nova_pessoa = {'nome': nome, 'idade': idade}
        pessoas.append(nova_pessoa)
        salvar_dados(pessoas)
        
        print(f'\n{VERDE}Registro de {NEGRITO}{nome}{RESET}{VERDE} adicionado e salvo com sucesso!{RESET}')
        sleep(2)
        
    elif opcao == '3':
        print(f"{VERMELHO}-" * 40 + f"{RESET}")
        print(f"{NEGRITO}{VERMELHO}{'REMOVER CADASTRO':^40}{RESET}")
        print(f"{VERMELHO}-" * 40 + f"{RESET}")
        
        if not pessoas:
            print(f"{AMARELO}Não há ninguém cadastrado para remover.{RESET}")
            sleep(2)
            continue
            
        # Lista as pessoas com um índice numérico ao lado (começando em 1)
        for i, p in enumerate(pessoas, start=1):
            print(f"{AMARELO}{i:^3}{RESET} - {NEGRITO}{p['nome']:<25}{RESET} ({p['idade']} anos)")
        print(f"{VERMELHO}-" * 40 + f"{RESET}")
        
        # Validação do ID escolhido
        while True:
            try:
                escolha = int(input(f'{NEGRITO}Digite o número da pessoa que deseja remover (ou 0 para cancelar): {RESET}'))
                if escolha == 0:
                    print(f'{AMARELO}Operação cancelada.{RESET}')
                    break
                if 1 <= escolha <= len(pessoas):
                    # Traduz a escolha humana para o índice real do Python (humano escolhe 1, Python lê índice 0)
                    indice_remover = escolha - 1
                    pessoa_removida = pessoas[indice_remover]
                    
                    # Confirmação de segurança antes do drop
                    confirmar = input(f"{VERMELHO}Tem certeza que deseja apagar {NEGRITO}{pessoa_removida['nome']}{RESET}{VERMELHO}? [S/N]: {RESET}").strip().upper()
                    
                    if confirmar == 'S':
                        # Remove o dicionário correto da lista
                        pessoas.pop(indice_remover)
                        # Atualiza o arquivo JSON no disco rígido
                        salvar_dados(pessoas)
                        print(f"\n{VERDE}Registro de {NEGRITO}{pessoa_removida['nome']}{RESET}{VERDE} removido com sucesso!{RESET}")
                    else:
                        print(f"{AMARELO}Remoção cancelada pelo usuário.{RESET}")
                    break
                else:
                    print(f'{VERMELHO}Erro! Escolha um número válido da lista.{RESET}')
            except ValueError:
                print(f'{VERMELHO}Erro! Digite apenas números inteiros.{RESET}')
        sleep(2)
        
    elif opcao == '4':
        print(f'{AMARELO}Saindo do sistema...{RESET}')
        sleep(1)
        break
        
    else:
        print(f'{VERMELHO}Opção inválida! Tente novamente.{RESET}')
        sleep(1)