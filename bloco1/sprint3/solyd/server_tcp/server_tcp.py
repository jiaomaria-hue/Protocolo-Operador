import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

file = open("output.txt", "w")

try:
    server.bind(("0.0.0.0", 4466))
    server.listen(5)
    print("Lintening...")

    client_socket, addres = server.accept()
    print(f"Received from: {addres[0]}")

    data = client_socket.recv(1024).decode()

    file.write(data)


    server.close()
except Exception as error:
    print("Erro: ", error)
    server.close()