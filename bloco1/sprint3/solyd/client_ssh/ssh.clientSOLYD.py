import paramiko
import getpass

host = input("Host/IP: ")
user = input("Usuario SSH: ")
passwd = getpass.getpass("Senha SSH: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    print("[*] Conectando ao servidor SSH...")
    client.connect(host, username=user, password=passwd, port=22, timeout=5)
    print("[+] Conectado com sucesso!\n")

    while True:
            comando = input("Comando: ").strip()

            if comando.lower() in ["exit", "quit"]:
                print("Saindo...")
                break  
            if not comando:
                 continue


            
            stdin, stdout, stderr = client.exec_command(comando)

            saida = stdout.read().decode("utf-8")
            erros = stderr.read().decode("utf-8")

            if saida:
                 print(saida, end="")
            if erros:
                print(erros)
except paramiko.ssh_exception.AuthenticationException:
    print("[!] Erro: Usuário ou senha incorretos.")
except Exception as error:
    print(f"[!] Erro de conexão/execução: {error}")

finally:
    client.close()
    print("[*] Conexão encerrada com segurança.")
    