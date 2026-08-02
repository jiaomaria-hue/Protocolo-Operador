import subprocess

resultado = subprocess.run(['whoami'], capture_output=True, text=True)
print(resultado.stdout)