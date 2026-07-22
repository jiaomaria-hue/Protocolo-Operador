from random import randint
import time
from operator import itemgetter
dicio = {}
for c in range(1, 5):
    valor_dado = randint(0, 6)
    dicio[f'jogador {c}'] = valor_dado
print("\nSorteando valores...")
for k, v in dicio.items():
    print(f"{k} tirou {v}")
    time.sleep(1)
ranking = sorted(dicio.items(), key=itemgetter(1), reverse=True)
print("\n--- RANKING FINAL---")
for posicao, (jogador, dado) in enumerate(ranking, start=1):
    print(f"{posicao}º Lugar: {jogador} com {dado} pontos.")