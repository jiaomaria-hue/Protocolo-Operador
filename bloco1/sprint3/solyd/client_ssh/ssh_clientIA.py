import paramiko
import getpass

host = input("Host/IP: ")
user = input("Usuario SSH: ")
senha = getpass.getpass("Senha SSH: ")


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(host, username=user, password=senha, port=22)
    print("[+] Conexão SSH estabelecida com sucesso!")

    stdin, stdout, stderr = client.exec_command("ls -la")

    resultado = stdout.read().decode("utf-8")
    erros = stderr.read().decode("utf-8")

    if resultado:
        print("\n--- Saida de comando ---")
        print(resultado)

    if erros:
            print("\n--- Erros ---")
            print(erros)
except paramiko.ssh_exception.AuthenticationException:
    print("[!] ERRO: Usuário ou senha incorretos.")
except Exception as e:
    print(f"[!] ERRO DE CONEXÃO: {e}")
finally:
    # 4. Sempre fecha a sessão
    client.close()

