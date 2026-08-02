import subprocess
class Ip:
    def __init__(self, ip):
        self.ip = ip
    def osint_basico_ip(self):
        resultado = subprocess.run(
            ['curl', '-s', f'https://ipinfo.io/{self.ip}/json'],
            capture_output=True,
            text=True
        )
        print(resultado.stdout)