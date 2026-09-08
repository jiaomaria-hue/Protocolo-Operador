# AULA 8 SOCKET E CLIENT TCP

## criando um client_tcp.py

* Para criar um client tcp precisamos **importartar** uma biblioteca chamada **socket**.
Primeiro criamos uma variavel chamada client e dentro dela colocamos uma funcao chamada **socket.socket(socket.AF_INET, socket.SOCK_STREAM)**

* Para **conectar** o client_tcp em um site/ip usamos o comando chamada client(a variavel que a gente criou emcima) **client.connect(("google.com", 80))**
Seria assim **client.connect(("site", porta))**

* Para **enviar** dados para o google(O alvo) vamos usar o comando **client.send("ola tudo bem")**. Voce acha q esse comando vai dar certo? NAO. Porq ele so aceita em bytes entao usamos o b antes das aspas, entao seria assim **client.send(b'ola tudo bom?')**

* Para **receber dados** usamos o **recv** entao seria assim client.recv(Numeros de bytes).

* Quando enviamos dados pro google. Ele nao vai responder assim **AH TUDO BEM** so voce dizendo **client.send("ola tudo bem?")** nao. Usamos a lingaguem deles que seria http pois porta 80 e http.
entao seria uma requisicao http. Isso sim ele responde. Mas ele responde como varios codigos html. Envia o html de pesquisa dele sabe?, entao pra receber bonitin usamos o .**decode()** dai recebemos melhor do que em bytes.

## iMPORTANTE!!! USAMOS O 
**GET / HTTP/1.1\nHost: www.google.com\n\n\n"**
PARA RECEBER A RESPOSTA DO GOOGLE!!

# CODIGOS PRONTOS
* Codigo para entrar no meu nc -lvp 4466:

 import socket

 client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 client.connect(("127.0.0.1", 4466))
 client.send(b"oi tudo bem?\n")
 pacotes_recebidos = client.recv(1024).decode()
 print(pacotes_recebidos)

 * Codigo para falar com o google:

 import socket

 client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 client.connect(("google.com", 80))
 client.send(b"GET / HTTP/1.1\nHost: www.google.com\n\n\n")
 pacotes_recebidos = client.recv(1024).decode()
 print(pacotes_recebidos)

 # AFINIDADE COM ERROS E TYMEOUT
  ## 1 ERRO
  * Para tratarmos de erros usamos o try e o except

  ## 2 TYMEOUT
  * Usamos o tymeout para setar o segundos q o servidor tem q responder. Entao tipo 
  **client.settimout(1)** Esperamos 1 segundo para o servidor responder. Se nao responder ele fecha
  Como se fosse assim **TA VOU ESPERAR 1 SEGUNDO. CASO NAO RESPONDER EU FECHO**

## CODIGO PRONTO TOTAL:

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

try:
    client.connect(("127.0.0.1", 4466))
    client.send(b"oi tudo bem?\n")
    pacotes_recebidos = client.recv(1024).decode()
    print(pacotes_recebidos)
except:
    print("Um erro ocorreu")