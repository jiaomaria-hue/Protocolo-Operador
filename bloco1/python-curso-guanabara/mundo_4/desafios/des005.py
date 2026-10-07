from rich import print
from rich.panel import Panel
from rich.table import Table
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_fav = []
    def add_jogos(self, jogo):
        self.jogos_fav.append(jogo)
    def ficha(self):
        conteudo = f'[bold cyan]Nome real:[/] {self.nome}\n[bold cyan]jogos favoritos:[/]'
        for jogo in self.jogos_fav:
            conteudo += f'\n 🎮 {jogo}'

        painel = Panel(
            conteudo,
            title=f"[bold yellow]Jogador <{self.nick}>[/bold yellow]",
            title_align='left',
            border_style='bright_blue',
            expand=False
        )
        print(painel)

j1 = Gamer('PenisRonald', 'naldopeninho')
j1.add_jogos('Game of thores')
j1.add_jogos('My femboy rommate')
j1.ficha()