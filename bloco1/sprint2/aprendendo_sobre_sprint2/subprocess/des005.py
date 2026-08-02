import subprocess

resultado = subprocess.run(
    ['which', 'curl'],
    capture_output=True,
    text=True
)
if resultado.returncode == 0:
    print(f'Curl instalado em: {resultado.stdout.strip()}')
else:
    print('Curl não está instalado')