import time
from rich import print
from rich.text import Text

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
    
    def __rich__(self):
        t = Text()
        t.append("📘 Você acabou de abrir o livro '", style="blue")
        t.append(self.titulo, style="red")
        t.append(f"' que tem {self.paginas} páginas no total. Você agora está na página 1", style="blue")
        return t

    def avancar_paginas(self, numero):
        pagina_alv = self.pagina_atual + numero
        

        if pagina_alv > self.paginas:
            sobra = self.paginas - self.pagina_atual
            if sobra > 0:
                self._animar_paginas(self.pagina_atual + 1, self.paginas)
                print(f" [white]Você avançou [cyan]{sobra}[/] páginas e agora está na [magenta]página[/] [cyan]{self.paginas}[/]")
            
            print(f'[red]■[/] [red]Você chegou ao final do livro \'{self.titulo}\'[/]')
            self.pagina_atual = self.paginas
            return

        pagina_antiga = self.pagina_atual
        self._animar_paginas(pagina_antiga + 1, pagina_alv)
        self.pagina_atual = pagina_alv
        print(f" [white]Você avançou [cyan]{numero}[/] páginas e agora está na [magenta]página[/] [cyan]{self.pagina_atual}[/]")

    def _animar_paginas(self, inicio, fim):
        for i in range(inicio, fim + 1):
            print(f'[white]Pág{i}[/] [magenta]▶[/]', end=' ')
            time.sleep(0.5) 

# --- Execução ---
l1 = Livro(titulo="10 coisas que aprendi", paginas=20)
print(l1)

l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(5) 