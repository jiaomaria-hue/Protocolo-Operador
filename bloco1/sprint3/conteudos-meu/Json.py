import json
f = open('cadastro.json', 'r')
meu_json = json.loads(f.read())
print(meu_json['Nome'])
f.close()
