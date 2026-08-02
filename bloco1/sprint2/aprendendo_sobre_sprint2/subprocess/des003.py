import subprocess

resposta = subprocess.run(['df', '-h'], capture_output=True, text=True)
print(resposta.stdout)