import subprocess

def check_config(param, expected_value):
    result = subprocess.run(
        ['grep', f'^{param}', '/etc/ssh/sshd_config'],
        capture_output=True, text=True
    )
    output = result.stdout.strip()
    if expected_value in output:
        print(f"[OK] {param} configurado com sucesso")
    else:
        print(f"[NAO] {param} nao configurado e nem seguro!")

print('===== hardening config =====')
check_config("PermitRootLogin", "no")
check_config("PasswordAuthentication", "no")
check_config("MaxAuthTries", "3")