import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        msg = input("Mensagem: ") + "\n"
        client.sendto(msg.encode(), ("127.0.0.1", 4466))
        data, sander = client.recvfrom(1024)
        print(sander[0] + ": " + data.decode())
        if data.decode() == "sair\n" or msg == "sair\n":
            break
    client.close()
except Exception as error:
    print("Erro de conexao")
    print(error)