# 🪖 LOG DE GUERRA — PROTOCOLO OPERADOR

## [31/05/2026] — Entrada #001: Ativação, Incidente e Recuperação Total

### 1. O que aconteceu
- Iniciei oficialmente o Protocolo de 18 Meses na trilha Purple Team.
- Durante a organização manual das pastas e sincronização do GitHub, cometi um erro de execução e acabei deletando acidentalmente todos os meus scripts Python locais (`exercicio005.py`, `exercicio007.py`, `exercicio013.py`) e o arquivo de anotações do Jupyter (`jupyter.ipynb`).

### 2. Ações de Emergência
- **Análise de Dano:** Percebi a tempo que, embora os arquivos tivessem sumido do disco, as abas do VS Code ainda mantinham os códigos carregados na memória (RAM).
- **Extração Manual:** Tirei capturas de tela das abas abertas contendo toda a matéria das Aulas 4, 6, 7 e 8.
- **Recuperação:** Reconstruí a estrutura dos códigos de cálculo de média, sucessor/antecessor e aumento salarial de 15%.

### 3. Conceitos Python Consolidados

**Tipos Primitivos**
- `int` — inteiros
- `float` — decimais com ponto
- `bool` — `True` / `False`
- `str` — textos entre aspas

**Validadores**
- `.isnumeric()` — verifica se é número
- `.isalpha()` — verifica se é letra
- `.isalnum()` — verifica se é alfanumérico
- `.isupper()` — verifica se está em maiúsculo

**Ordem de Precedência**
```
() → ** → * / // % → + -
```

**Formatação Avançada**
- Alinhamentos: `<` (esquerda), `>` (direita), `^` (centro)
- Casas decimais: `:.2f` ou `:.3f` dentro de f-strings ou `.format()`

**Módulos (Aula 8)**
- `import math` — funções matemáticas
- `import random` — números aleatórios
- `from math import sqrt` — importação específica

### 4. Status do Lab
- Ambiente 100% recuperado
- Exercícios refeitos e salvos no disco
- Repositório Protocolo-Operador no GitHub operacional
- Anotações estruturadas para o próximo nível

### 5. Lição Aprendida
> **"Sem commit, não existe."**
> Todo arquivo criado vai pro GitHub no mesmo dia. Sem exceção.

### 6. Próximo Passo
- Resolver os desafios práticos do 16 ao 21 da Aula 8
- Commitar cada exercício imediatamente após criar

### 3 de junho proximos passos
- **2026-06-03 — Meta definida: Home Lab (DC + Win10 + Kali) operacional até 05/06/2026**

### 4 de junho 
1. Objetivo Operacional
Estabelecer ambiente de desenvolvimento isolado e profissional no Zorin OS (base Debian) para início das atividades de Python (Fase 1 - Bloco A).

2. Configurações Realizadas
Ambiente Isolado (venv): Criado com sucesso para evitar poluição do SO principal.

Integração VS Code:

Terminal integrado configurado e ativado (source venv/bin/activate).

Interpretador Python do VS Code apontado para o executável dentro da venv.

Dependências: Biblioteca Pillow instalada via pip para manipulação de imagem.

Comando de verificação: python -c "from PIL import Image; print('Pillow instalado com sucesso!')"

3. Conceitos Dominados
Virtual Environments: Isolamento de dependências como pré-requisito de engenharia.

Gerenciamento de Pacotes: Uso do pip para expansão de capacidades do Python.

ASCII Art (Lógica Hacker): Compreensão do mapeamento de densidade de pixels em caracteres (conversão de matrizes de dados em representação visual).

Sistemas de Permissão: Entendimento básico da lógica de os.access (o primeiro passo para identificar brechas em servidores).

4. Pendências / Próximos Passos (Julho)
[x] Iniciar Bloco A: Scripts de automação de sistema (Bash + Python).

[x] Configurar Lab de VMs (VirtualBox: Kali + Windows 10 + Windows Server).

[x] Criar script de scanner de permissões funcional.

## 24/06/2026 - Quarta feira, sprint 1, bloco 1. python puro.

### 🚨 ONDE QUEBROU (Problemas)
- nada, pois hoje eu so fiz a aula do gustavo guanabara
### 💡 A DESCOBERTA (O que você entendeu)
- os fatiamentos ajudam bastante nas tarefas.
- os desafios que mais me intrigaram.

### 🛡️ A HIPÓTESE (Purple Team)
- Frases escondidas. como Salve O neymar com amor e Salvamento. SOS


# ⚔️ LOG DE GUERRA — Protocolo Operador
> "Sem commit, não existe. Sem log, não aprendeu."
---

## [001] — 25/06/2025 — gustavo guanabara. aula 9.

**Sprint:** 1 · **Área:** Linux / Terminal

**Contexto:**
fazendo o curso do gustavo guanabara, e entrando em outro episodio.

**Erro exato (se nao tiver, fale do seu erro no python.):**
1. Esperava ver só o primeiro nome, mas o print mostrava o nome inteiro.

**Tentativas:**
1. Rodei `exercicio 24` — funcionou, mas queria entender
   porque so mostrava o nome todo e nao o primeiro nome
2. pesquisei no canal de desafios dele e funcionou.
3. Descobri que so era adcionar um [:5]
**Solução:**
cidade = str(input('digite o nome de uma cidade: ')).lower().strip()
print(cidade[:5] == 'santo')
```
E adicionei na primeira linha do script:
variavel, input str e .lower() .strip()
o .lower() = serve pra deixar tudo minusculo. ja o strip tira todos os espaços indejesados.

**Por que funciona:**
o script precisa saber onde começa e onde vai o fim, entao ele vé se aparece o nome 'santo' de primeiro ou nao.

**Lição permanente:**
Fatiamento de string em Python usa [inicio:fim].
cidade[:5] retorna os 5 primeiros caracteres.
Sem fatiamento, a comparação nunca funcionaria para nomes parciais.

**Tempo perdido:** 25 min por causa das atividades, que eram 5
**Nunca mais:** X

------------------------------------------------------------

## [002] — 25/06/2025 — IP como float quebrava a comparação

**Sprint:** 1 · **Área:** Python / Condicionais

**Contexto:**
Criando um simulador de verificação de IP com if/elif/else.

**Erro exato:**
Usei float() para capturar o IP. A comparação nunca batia porque
float arredonda e o usuário nunca digitaria o valor exato.

**Solução:**
IP é string, não número. Trocado para input() sem conversão.
A comparação com == passou a funcionar corretamente.

**Por que funciona:**
input() retorna string por padrão. Comparar string com string
é direto. Float com float em IP nunca vai funcionar porque
192.168.0.1 não é um número válido em Python.

**Lição permanente:**
IPs, CPFs, telefones e códigos são strings, não números.
Nunca usar int() ou float() para capturar esses valores.

**Tempo perdido:** 10 min
**Nunca mais:** ✅

---

#[003] — 26/06/2026 — Terminando mundo 1 python gustavo guanabara
Sprint: 1 · Área: Python / Condicionais

Contexto:
Execução dos exercícios 029 (Radar eletrônico) e 030 (Par ou Ímpar).

Erro exato:
Os meus erros principais foram a dependência excessiva de tentativa e erro, a falha em validar a lógica antes da formatação (ex: % para paridade e cálculo de multa no radar) e a priorização de conceitos superficiais sobre fundamentos essenciais.

Solução:
Validação rigorosa antes da codificação. Aplicação de "Boundary Testing" (testar os limites) e desenho do fluxo lógico no papel antes de iniciar qualquer sintaxe no VS Code.

Por que funciona:
Ao separar a lógica de negócio (cálculos) da interface (exibição), garanto que falhas de formatação não corrompam o fluxo condicional. O uso do operador módulo (%) e o isolamento de blocos de decisão tornam o código determinístico.

Lição técnica permanente:
Todo fluxo condicional deve ser precedido por validação de Type Casting e seguido por um teste de limite; o código é apenas a expressão final de uma lógica impecável desenhada previamente.

Tempo perdido: 15 min
Nunca mais: X

## [004] — 27/06/2026 — Primeiro port scanner com socket

**Sprint:** 1 · **Área:** Python / Socket

**Contexto:**
Aprendi o módulo socket do Python e construí um port scanner
que testa portas abertas em um alvo.

**O que aprendi:**
- socket.socket() cria uma "tomada" de conexão
- connect_ex() tenta conectar numa porta — retorna 0 se aberta
- settimeout(1) evita esperar infinitamente por portas fechadas
- range(1, 1025) gera números de 1 até 1024
- O for percorre cada número e testa a porta

**O que ainda não entendo:**
- Como funciona threading para acelerar o scan
- Por que algumas portas retornam números diferentes de 0 e 11
**Resultado:**
scanme.nmap.org — porta 22 (SSH) e porta 80 (HTTP) abertas.

**Lição permanente:**
Nunca nomear um arquivo com o mesmo nome de uma biblioteca
Python — causa conflito no import.

**Tempo perdido:** 10 min (KeyboardInterrupt + arquivo socket.py)
**Nunca mais:** ✅ — arquivo socket.py