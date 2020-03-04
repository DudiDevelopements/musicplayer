# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.core.audio import SoundLoader, Sound
from kivy.uix.filechooser import FileSystemLocal
from kivy.uix.floatlayout import FloatLayout

"""

    Projeto: 'Player de música (com kivy)'
    De: Marcilio

"""


# Classe principal do app
class MusicPlayer(FloatLayout):

    # Função que é executada ao iniciar
    def __init__(self, **kwargs):
        super(MusicPlayer, self).__init__(**kwargs)

        self.file_system = FileSystemLocal()

        self.listaMusicas = []

        self.path_musica = str()

        self.musicaPath = str()
        self.musica = SoundLoader.load('F:/marcilinho/PythonP/Player/musicas/')

        self.indexMusicaAtual = 0

        # F:/marcilinho/PythonP/Player/musicas/

        Sound.volume = 1


###############     Funções Adicionais     ###############

    # Verifica se o index for maior que o numero de musicas
    def verificarIndex(self):
        """
        Se o index da música for maior que a quantidade de de musicas
        ele volta o index a zero
        """
        if self.indexMusicaAtual > len(self.listaMusicas) - 1:
            self.indexMusicaAtual = 0

    def mostraNomeMusica(self):
        # Mostra no console
        print("Tocando: " + self.listaMusicas[self.indexMusicaAtual])
        # Mostra na interface
        self.ids.musica_text.text = self.listaMusicas[self.indexMusicaAtual]

    def salvaPathMusica(self):
        self.path_musica = self.ids.musica_source.text

        # Verifica cada .mp3 que estiver na pasta escrita e coloca na lista 'listaMusicas'
        for arquivoMusica in self.file_system.listdir(self.path_musica):
            if '.mp3' in arquivoMusica:
                self.listaMusicas.append(arquivoMusica)

        self.ids.musica_text.text = 'Salvo'

        print(self.path_musica)
        print('')
        print(self.listaMusicas)

    def carregaMusica(self):
        self.musicaPath = self.path_musica + self.listaMusicas[self.indexMusicaAtual]

        self.musica = SoundLoader.load(self.musicaPath)

        
###############    Funções Principais    ##############

    # Função que é chamada ao clicar no botão "Reproduzir"
    def play_music(self):
        self.carregaMusica()

        self.musica.play()
        self.mostraNomeMusica()
        self.verificarIndex()

    # Função que ao clicar em 'anterior' diminui em 1 no index
    def proxima(self):
        self.musica.stop()

        self.indexMusicaAtual += 1
        self.carregaMusica()

        self.musica.play()
        self.mostraNomeMusica()
        self.verificarIndex()

    # Função que ao clicar em 'proxima' adiciona em 1 no index
    def anterior(self):
        self.musica.stop()

        self.indexMusicaAtual -= 1
        self.carregaMusica()

        self.musica.play()
        self.mostraNomeMusica()
        self.verificarIndex()

    # Função que ao clicar em 'anterior' diminui em 1 no index
    def stop_music(self):
        self.musica.stop()
        self.indexMusicaAtual = 0

        self.ids.musica_text.text = "Nenhuma musica tocando no momento"


# Classe que builda o app
class PlayApp(App):

    def build(self):
        self.icon = "ico.png"
        self.title = "Player de Música"
        return MusicPlayer()


if __name__ == '__main__':
    PlayApp().run()
