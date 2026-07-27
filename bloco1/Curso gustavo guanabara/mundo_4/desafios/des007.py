from rich import print
from rich.panel import Panel

class ControleRemoto:
    def __init__(self):
        # Atributos protegidos para encapsulamento (conforme dica 2)
        self._ligada = False
        self._canal = 1
        self._volume = 10
        self._MIN_VOLUME = 0
        self._MAX_VOLUME = 20
        self._TOTAL_CANAIS = 5

    def ligar_desligar(self):
        self._ligada = not self._ligada
        status = "ligada" if self._ligada else "desligada"
        print(f"[yellow]A TV agora está {status}.[/yellow]")

    def mais_canal(self):
        # Validação de estado (dica 1)
        if not self._ligada:
            print("[red]Erro: A TV está desligada! Impossível alterar o canal.[/red]")
            return
        
        # Lógica cíclica usando operador de resto (dica 3)
        # Exemplo: se canal for 5, (5 % 5) + 1 = 1
        self._canal = (self._canal % self._TOTAL_CANAIS) + 1
        print(f"[cyan]Canal alterado para: {self._canal}[/cyan]")

    def menos_canal(self):
        if not self._ligada:
            print("[red]Erro: A TV está desligada! Impossível alterar o canal.[/red]")
            return
        
        # Lógica cíclica reversa
        self._canal -= 1
        if self._canal < 1:
            self._canal = self._TOTAL_CANAIS
        print(f"[cyan]Canal alterado para: {self._canal}[/cyan]")

    def mais_volume(self):
        if not self._ligada:
            print("[red]Erro: A TV está desligada! Impossível alterar o volume.[/red]")
            return
        
        if self._volume < self._MAX_VOLUME:
            self._volume += 1
            print(f"[green]Volume: {self._volume}[/green]")
        else:
            print("[yellow]Aviso: Volume já está no máximo![/yellow]")

    def menos_volume(self):
        if not self._ligada:
            print("[red]Erro: A TV está desligada! Impossível alterar o volume.[/red]")
            return
        
        if self._volume > self._MIN_VOLUME:
            self._volume -= 1
            print(f"[green]Volume: {self._volume}[/green]")
        else:
            print("[yellow]Aviso: A TV já está no mudo (mínimo)![/yellow]")

    def exibir_status(self):
        estado_txt = "[bold green]LIGADA[/bold green]" if self._ligada else "[bold red]DESLIGADA[/bold red]"
        info = (
            f"Estado: {estado_txt}\n"
            f"Canal atual: {self._canal if self._ligada else '---'}\n"
            f"Volume atual: {self._volume if self._ligada else '---'}"
        )
        print(Panel(info, title="[bold yellow]Painel da TV[/bold yellow]", border_style="blue", expand=False))

# --- Loop principal de interação do programa ---
controle = ControleRemoto()

while True:
    print("\n--- MENU DO CONTROLE ---")
    print("[ @ ] Ligar / Desligar")
    print("[ > ] Avançar Canal")
    print("[ < ] Voltar Canal")
    print("[ + ] Aumentar Volume")
    print("[ - ] Diminuir Volume")
    print("[ s ] Ver Status da TV")
    print("[ 0 ] Sair")
    
    opcao = input("Digite o comando: ").strip()

    if opcao == "0":
        print("[red]Encerrando o sistema do controle... Até logo![/red]")
        break
    elif opcao == "@":
        controle.ligar_desligar()
    elif opcao == ">":
        controle.mais_canal()
    elif opcao == "<":
        controle.menos_canal()
    elif opcao == "+":
        controle.mais_volume()
    elif opcao == "-":
        controle.menos_volume()
    elif opcao.lower() == "s":
        controle.exibir_status()
    else:
        print("[red]Comando inválido! Tente novamente.[/red]")