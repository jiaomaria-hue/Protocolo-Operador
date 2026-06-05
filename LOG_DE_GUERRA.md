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
[ ] Iniciar Bloco A: Scripts de automação de sistema (Bash + Python).

[ ] Configurar Lab de VMs (VirtualBox: Kali + Windows 10 + Windows Server).

[ ] Criar script de scanner de permissões funcional.