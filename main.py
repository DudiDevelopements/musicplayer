# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.core.audio import SoundLoader, Sound
from kivy.uix.filechooser import FileSystemLocal
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty

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

    # Ao inicializar procura por arquivos com final .mp3
    def __init__(self, **kwargs):
        super(MusicPlayer, self).__init__(**kwargs)

        file_system = FileSystemLocal()

        # Atribui a variável lista listaMusicas
        self.listaMusicas = []

        # Verifica cada .mp3 que estiver na pasta escrita e coloca na lista 'listaMusicas'
        for arquivoMusica in file_system.listdir('C:/Users/Verena Ortiz/Desktop/marcilinho/PythonP/Player/musicas'):
            if '.mp3' in arquivoMusica:
                self.listaMusicas.append(arquivoMusica)

        self.indexMusicaAtual = 0
        print(self.indexMusicaAtual)
        print(self.listaMusicas)

        # Carrega a musica com o index que esta tocando
        self.musica = SoundLoader.load(
            'C:/Users/Verena Ortiz/Desktop/marcilinho/PythonP/Player/musicas/' + self.listaMusicas[
                self.indexMusicaAtual])

        Sound.volume = 1

    # Verifica se o index for maior que o numero de musicas
    def verificarIndex(self):
        if self.indexMusicaAtual > len(self.listaMusicas) - 1:
            self.indexMusicaAtual = 0

    # Função que é chamada ao clicar no botão "Reproduzir"
    def play_music(self):

        self.indexMusicaAtual = 0

        # Da play da musica que foi carregada no init
        self.musica.play()
        self.musica_text.text = StringProperty(self.listaMusicas[self.indexMusicaAtual])

        print("Tocando: " + self.listaMusicas[self.indexMusicaAtual - 1])
        self.verificarIndex()

    # Função que é chamada ao clicar no botão "Parar"
    def stop_music(self):
        self.musica.stop()
        self.indexMusicaAtual = 0

    # Função que ao clicar em 'proxima' adiciona em 1 no index
    def proxima(self):
        self.musica.stop()
        self.musica = SoundLoader.load(
            'C:/Users/Verena Ortiz/Desktop/marcilinho/PythonP/Player/musicas/' + self.listaMusicas[
                self.indexMusicaAtual])
        self.indexMusicaAtual += 1
        self.musica.play()
        print("Tocando: " + self.listaMusicas[self.indexMusicaAtual - 1])
        self.verificarIndex()

    # Função que ao clicar em 'anterior' diminui em 1 no index
    def anterior(self):
        self.musica.stop()
        self.musica = SoundLoader.load(
            'C:/Users/Verena Ortiz/Desktop/marcilinho/PythonP/Player/musicas/' + self.listaMusicas[
                self.indexMusicaAtual])
        self.indexMusicaAtual -= 1
        self.musica.play()
        print("Tocando: " + self.listaMusicas[self.indexMusicaAtual - 1])
        self.verificarIndex()


# Classe que builda o app
class PlayApp(App):

    def build(self):
        self.icon = "ico.png"
        self.title = "Player de Música"
        return MusicPlayer()


# Função que da run no app
if __name__ == '__main__':
    PlayApp().run()
