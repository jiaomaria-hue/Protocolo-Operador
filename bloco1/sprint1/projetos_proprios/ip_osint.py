import subprocess
from config import URL_IPINFO
class Ip:
    def __init__(self, ip):
        self.ip = ip
    def osint_basico_ip(self):
        resultado = subprocess.run(
            ['curl', '-s', f'{URL_IPINFO}'],
            capture_output=True,
            text=True
        )
        print(resultado.stdout)