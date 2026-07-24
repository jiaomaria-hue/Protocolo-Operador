class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
        self.videos = []
        self.playlists: list[Playlist] = []

    def __repr__(self):
        return f"Canal: {self.nome} ({self.inscritos} inscritos) - Vídeos: {self.videos}"

    def inscrever(self, quantidade=1):
        self.inscritos += quantidade

    def postar(self, video):
        if video in self.videos:
            print('Esse video ja foi postado')
            return
        self.videos.append(video)

    def adicionar_playlist(self, playlist):
        if playlist not in self.playlists:
            self.playlists.append(playlist)
        else:
            print('Essa playlist ja foi adicionada')

    def remover_playlist(self, playlist):
        if playlist in self.playlists:
            self.playlists.remove(playlist)
        else:
            print('EEsa playlist nao existe')

    def info_playlists(self):
        for playlist in self.playlists:
            print(f"--- Playlist: {playlist.nome} ---")
            playlist.info_videos()  # Adicionado os parênteses aqui


class CanalEmpresarial(Canal):
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome, descricao, inscritos)
        self._equipe = []

    @property
    def equipe(self):
        return self._equipe

    def adicionar_membro_equipe(self, membro):
        if membro not in self._equipe:
            self._equipe.append(membro)
        else:
            print(f'O membro {membro} ja esta na equipe')

    def remover_membro_equipe(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
        else:
            print(f'O membro {membro} não esta na equipe')
            
class Video:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.visualizacoes = 0
        self.likes = 0
        self.dislikes = 0
        self.comentarios = []

    def assistir(self):
        self.visualizacoes += 1

    def like(self):
        self.likes += 1

    def dislike(self):
        self.dislikes += 1

    def comentar(self, comentario):
        self.comentarios.append(comentario)

    def info(self):
        print(f'''Título: {self.titulo}
Descrição: {self.descricao}
Visualizações: {self.visualizacoes}
Likes: {self.likes} | Dislikes: {self.dislikes}
Comentários: {self.comentarios}\n''')


class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.videos: list[Video] = []

    def adicionar_video(self, video):
        if video not in self.videos:
            self.videos.append(video)
        else:
            print(f'Esse video ja esta na playlist')

    def remover_video(self, video):
        if video in self.videos:
            self.videos.remove(video)
        else:
            print(f'Esse video nao esta na playlist')

    def info_videos(self):
        for video in self.videos:
            video.info()

# Testando as instâncias
canal_lancode = Canal('Lan Code', 'Codigos e gatos', 34000)

video_poo = Video('Python objetos', 'Aprenda agora')
video_discordpy = Video('Aprenda discord.py', 'squarecloud')
playlist_programacao = Playlist('Programação')
playlist_programacao.adicionar_video(video_poo)
playlist_programacao.adicionar_video(video_discordpy)

video_minecraft = Video('Jogano minezin', 'Mine')
video_deltarune = Video('Jogano deltarune', 'Deltarune')
playlist_games = Playlist('Games')
playlist_games.adicionar_video(video_minecraft)
playlist_games.adicionar_video(video_deltarune)


canal_lancode.adicionar_playlist(playlist_programacao)
canal_lancode.adicionar_playlist(playlist_games)

canal_lancode.postar(video_poo)
canal_lancode.postar(video_discordpy)

canal_lancode.info_playlists()