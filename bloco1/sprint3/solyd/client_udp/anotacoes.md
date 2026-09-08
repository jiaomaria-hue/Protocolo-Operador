# AULA — CLIENT UDP

## Criando um `client_udp.py`

* Primeiro importamos a biblioteca `socket`:

```python
import socket
```

* Depois criamos o cliente UDP:

```python
client = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)
```

- `AF_INET`: usa IPv4.
- `SOCK_DGRAM`: usa UDP.

No TCP usaríamos:

```python
socket.SOCK_STREAM
```

---

## Enviando dados

No UDP não precisamos usar `connect()`. Usamos `sendto()`:

```python
client.sendto(
    msg.encode(),
    ("127.0.0.1", 4466)
)
```

O comando significa:

```python
client.sendto(dados, (ip, porta))
```

O `encode()` transforma o texto em bytes, porque o socket envia dados nesse formato.

---

## Recebendo dados

Para receber mensagens UDP usamos:

```python
data, sender = client.recvfrom(1024)
```

- `data`: mensagem recebida em bytes;
- `sender`: endereço do remetente;
- `1024`: quantidade máxima de bytes recebidos.

Para transformar os bytes em texto usamos:

```python
data.decode()
```

---

## Código completo

```python
import socket

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

try:
    while True:
        msg = input("Mensagem: ") + "\n"

        client.sendto(
            msg.encode(),
            ("127.0.0.1", 4466)
        )

        data, sender = client.recvfrom(1024)

        print(sender[0] + ": " + data.decode())

        if msg == "sair\n" or data.decode() == "sair\n":
            break

    client.close()

except Exception as error:
    print("Erro de conexao")
    print(error)
```

Para testar com Netcat:

```bash
nc -u -lvp 4466
```

No UDP:

```python
sendto()
recvfrom()
```

No TCP:

```python
send()
recv()
```