import socket
from concurrent.futures import ThreadPoolExecutor

ALVO = 'google.com'

def testar_porta(porta):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((ALVO, porta)) == 0:
                print(f"Porta {porta}: ABERTA")
    except Exception:
        pass

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(testar_porta, range(1, 1025))