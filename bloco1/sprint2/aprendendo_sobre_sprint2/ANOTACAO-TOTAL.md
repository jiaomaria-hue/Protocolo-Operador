# 📚 Anotações Sprint 2 — Módulos Python

> Referência pessoal — Protocolo Operador

---

## Módulo `os` — Sistema Operacional

```python
import os
```

### Navegação
```python
os.getcwd()              # pasta atual
os.chdir('/caminho')     # muda de pasta
os.listdir('/caminho')   # lista conteúdo
```

### Pastas
```python
os.mkdir('pasta')                    # cria uma pasta
os.makedirs('a/b/c')                 # cria pastas aninhadas
os.makedirs('pasta', exist_ok=True)  # cria sem erro se já existir
os.rmdir('pasta_vazia')              # deleta pasta vazia
import shutil
shutil.rmtree('pasta_com_conteudo')  # deleta pasta com conteúdo
```

### Arquivos
```python
os.remove('arquivo.txt')             # deleta arquivo
os.rename('antigo.txt', 'novo.txt')  # renomeia
```

### `os.path`
```python
os.path.exists('/caminho')           # existe? True/False
os.path.isfile('/caminho')           # é arquivo? True/False
os.path.isdir('/caminho')            # é pasta? True/False
os.path.join('pasta', 'arquivo.txt') # monta caminho completo
os.path.getsize('arquivo.txt')       # tamanho em bytes
os.path.basename('/pasta/arquivo.txt') # 'arquivo.txt'
os.path.dirname('/pasta/arquivo.txt')  # '/pasta'
os.path.splitext('arquivo.txt')        # ('arquivo', '.txt')
```

### Variáveis de ambiente
```python
os.getenv('HOME')        # valor da variável
os.environ.copy()        # cópia de todas as variáveis
```

### Padrão comum
```python
# listar só arquivos .py
for item in os.listdir('/caminho'):
    if item.endswith('.py'):
        print(item)

# separar arquivos de pastas
for item in os.listdir('/caminho'):
    caminho = os.path.join('/caminho', item)
    if os.path.isfile(caminho):
        print(f'{item} é arquivo')
    else:
        print(f'{item} é pasta')

# criar pasta se não existir
os.makedirs('/caminho', exist_ok=True)
```

---

## Módulo `subprocess` — Executar Comandos

```python
import subprocess
```

### Básico
```python
resultado = subprocess.run(['comando', 'arg1', 'arg2'],
                           capture_output=True,
                           text=True)
print(resultado.stdout)    # output do comando
print(resultado.stderr)    # erros
print(resultado.returncode) # 0 = sucesso
```

### Parâmetros
| Parâmetro | O que faz |
|---|---|
| `capture_output=True` | captura o output |
| `text=True` | retorna string em vez de bytes |
| `cwd='/caminho'` | pasta onde rodar o comando |
| `shell=True` | roda via shell do sistema |

### Exemplos
```python
# whoami
r = subprocess.run(['whoami'], capture_output=True, text=True)
print(r.stdout)

# ls em pasta específica
r = subprocess.run(['ls', '-la'], capture_output=True, text=True,
                   cwd='/home/joao/Documentos')
print(r.stdout)

# verificar se programa está instalado
r = subprocess.run(['which', 'curl'], capture_output=True, text=True)
if r.returncode == 0:
    print(f'Instalado em: {r.stdout.strip()}')

# curl para API
r = subprocess.run(['curl', '-s', 'https://ipinfo.io/8.8.8.8/json'],
                   capture_output=True, text=True)
print(r.stdout)
```

---

## Módulo `socket` — Redes

```python
import socket
```

### Básico
```python
socket.gethostbyname('google.com')    # resolve IP
socket.gethostname()                   # hostname da máquina
socket.getaddrinfo('google.com', 80)  # todos os IPs
```

### Testar porta
```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
resultado = s.connect_ex(('google.com', 80))
# 0 = aberta, outro número = fechada
s.close()
```

### Com `with` (fecha automaticamente)
```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(1)
    if s.connect_ex(('google.com', 80)) == 0:
        print('Porta aberta')
```

### UDP
```python
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.settimeout(1)
    s.sendto(b'', ('alvo', 53))
    s.recvfrom(1024)
```

### Tipo de socket
| Constante | Significado |
|---|---|
| `AF_INET` | IPv4 |
| `AF_INET6` | IPv6 |
| `SOCK_STREAM` | TCP |
| `SOCK_DGRAM` | UDP |

---

## Módulo `requests` — HTTP

```python
import requests
```

### Básico
```python
resposta = requests.get('https://ipinfo.io/8.8.8.8/json')
dados = resposta.json()        # converte para dicionário
print(resposta.status_code)    # 200 = ok
print(resposta.text)           # texto bruto
```

### Com tratamento de erro
```python
try:
    resposta = requests.get('https://api.exemplo.com', timeout=5)
    dados = resposta.json()
except requests.exceptions.ConnectionError:
    print('Sem conexão')
except requests.exceptions.Timeout:
    print('Timeout')
except requests.exceptions.JSONDecodeError:
    print('Resposta inválida')
```

### Verificar IP com requests
```python
import requests

ip = input('IP: ')
resposta = requests.get(f'https://ipinfo.io/{ip}/json')
dados = resposta.json()

if dados.get('ip') is None:
    print('IP inválido')
else:
    print(f"Cidade: {dados.get('city')}")
    print(f"ISP: {dados.get('org')}")
```

---

## Threading — Concorrência

```python
from concurrent.futures import ThreadPoolExecutor
```

### Por que usar
Sem threading: porta 1 → espera → porta 2 → espera → ... (lento)
Com threading: 100 portas ao mesmo tempo (rápido)

### Básico
```python
def tarefa(item):
    # processa um item
    pass

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(tarefa, lista_de_itens)
```

### Port Scanner com threading
```python
import socket
from concurrent.futures import ThreadPoolExecutor

TIMEOUT = 0.5
ALVO = 'scanme.nmap.org'

def testar_porta(porta):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        if s.connect_ex((ALVO, porta)) == 0:
            print(f'Porta {porta} aberta')

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(testar_porta, range(1, 1025))
```

### Como classe
```python
class PortScanner:
    def __init__(self, alvo):
        self.alvo = alvo
        self.portas_abertas = []

    def testar_porta(self, porta):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((self.alvo, porta)) == 0:
                self.portas_abertas.append(porta)

    def scan(self):
        with ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(self.testar_porta, range(1, 1025))
        return self.portas_abertas
```

---

## `re` — Expressões Regulares (Regex)

```python
import re
```

### Para que serve
Encontrar padrões em texto — IPs, emails, hashes em logs gigantes.

### Básico
```python
texto = "IP 192.168.1.1 tentou acessar porta 22"

# encontra o primeiro match
match = re.search(r'\d+\.\d+\.\d+\.\d+', texto)
print(match.group())  # 192.168.1.1

# encontra todos os matches
matches = re.findall(r'\d+', texto)
print(matches)  # ['192', '168', '1', '1', '22']
```

### Padrões principais
| Padrão | Significado |
|---|---|
| `\d` | dígito (0-9) |
| `\d+` | um ou mais dígitos |
| `\w` | letra ou dígito |
| `\s` | espaço |
| `.` | qualquer caractere |
| `+` | um ou mais |
| `*` | zero ou mais |
| `{3}` | exatamente 3 vezes |

### Extrair IP de log
```python
import re

log = "2026-08-10 192.168.1.100 tentou acesso SSH"
ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log)
if ip:
    print(ip.group())  # 192.168.1.100
```

---

## Tabela Resumo

| Módulo | Para que serve |
|---|---|
| `os` | arquivos, pastas, sistema |
| `subprocess` | executar comandos do terminal |
| `socket` | conexões de rede TCP/UDP |
| `requests` | requisições HTTP a APIs |
| `threading` | tarefas em paralelo |
| `re` | encontrar padrões em texto |