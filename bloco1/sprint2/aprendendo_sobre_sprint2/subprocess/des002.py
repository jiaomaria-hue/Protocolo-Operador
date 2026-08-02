import subprocess

resultado = subprocess.run(
    ['ls', '-la'],
    capture_output=True,
    text=True,
    cwd='/home/joao/Documentos/Protocolo-Operador/bloco1/sprint1/projetos_proprios'
)
print(resultado.stdout)