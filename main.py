# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.core.audio import SoundLoader, Sound
from kivy.uix.filechooser import FileSystemLocal
from kivy.uix.floatlayout import FloatLayout

"""

    Projeto: 'Player de música (com kivy)'
    De: Marcilio


    Onde está escrito 'coloque o path da musica aqui', você devera colocar o
    path inteiro da pasta de onde estão as musicas como:

    'C:/Users/usuario/full/path/Player/musicas/' 

    tem que ter o barra no final ou você recebera um erro

"""


# Classe principal do app
class MusicPlayer(FloatLayout):

    # Função que é executada ao iniciar
    def __init__(self, **kwargs):
        super(MusicPlayer, self).__init__(**kwargs)

        file_system = FileSystemLocal()

        # Atribui a variável lista listaMusicas
        self.listaMusicas = []

        # Verifica cada .mp3 que estiver na pasta escrita e coloca na lista 'listaMusicas'
        for arquivoMusica in file_system.listdir('F://marcilinho/PythonP/Player/musicas'):
            if '.mp3' in arquivoMusica:
                self.listaMusicas.append(arquivoMusica)

        self.indexMusicaAtual = 0

        # Carrega a musica com o index que esta tocando
        self.musica = SoundLoader.load(
            'F:/marcilinho/PythonP/Player/musicas/' +
            self.listaMusicas[self.indexMusicaAtual])

        Sound.volume = 1

############### Funções Adicionais ###############

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

    ############### Funções Principais ###############

    # Função que é chamada ao clicar no botão "Reproduzir"
    def play_music(self):

        # Da play da musica que foi carregada no init
        self.musica.play()
        self.mostraNomeMusica()
        self.verificarIndex()

    # Função que é chamada ao clicar no botão "Parar"
    def proxima(self):
        self.musica.stop()
        self.indexMusicaAtual += 1

        self.musica = SoundLoader.load(
            'F:/marcilinho/PythonP/Player/musicas/' +
            self.listaMusicas[self.indexMusicaAtual])

        self.musica.play()
        self.mostraNomeMusica()
        self.verificarIndex()

    # Função que ao clicar em 'proxima' adiciona em 1 no index
    def anterior(self):
        self.musica.stop()
        self.indexMusicaAtual -= 1

        self.musica = SoundLoader.load(
            'F:/marcilinho/PythonP/Player/musicas/' +
            self.listaMusicas[self.indexMusicaAtual])

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


# Função que da run no app
if __name__ == '__main__':
    PlayApp().run()
