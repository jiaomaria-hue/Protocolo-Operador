import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Erro: Site inacessível')
else:
    print('Sucesso!')