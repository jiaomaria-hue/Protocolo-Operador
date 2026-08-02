import subprocess
ip = input('Digite um ip: ')
resultado = subprocess.run(
    ['curl', '-s', f'https://ipinfo.io/{ip}/json'],
    capture_output=True,
    text=True
)
print(resultado.stdout)