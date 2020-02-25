"""

    Projeto: 'Player de música (com kivy)'
    De: Marcilio (e um pouco de Deyvid)

"""

# Importa o kivy:
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
from kivy.core.audio import Sound
from kivy.uix.filechooser import FileSystemLocal
from kivy.uix.widget import Widget
from kivy.uix.button import Button

# Classe principal do app
class MusicPlayer(FloatLayout):

    # Ao inicializar procura por arquivos com final .mp3
    def __init__(self, **kwargs):
        super(MusicPlayer, self).__init__(**kwargs)

        file_system = FileSystemLocal()

        self.listaMusicas = []

        for arquivoMusica in file_system.listdir('coloque o source da musica aqui'):
            if '.mp3' in arquivoMusica:
                self.listaMusicas.append(arquivoMusica)

        self.indexMusicaAtual = 0
        print(self.indexMusicaAtual)
        print(self.listaMusicas)

    # Função que é chamada ao clicar no botão "Reproduzir"
    def play_music(self):
        
        self.musica = SoundLoader.load('coloque o source da musica aqui'+self.listaMusicas[self.indexMusicaAtual])

        self.musica.play()
        self.indexMusicaAtual = self.indexMusicaAtual + 1

        if self.indexMusicaAtual == len(self.listaMusicas):
            self.indexMusicaAtual = 0

        print(self.indexMusicaAtual)

    # Função que é chamada ao clicar no botão "Parar"
    def stop_music(self):
        self.musica.stop()


# Classe que builda o app
class PlayApp(App):

    def build(self):
        return MusicPlayer()


# Função que da run no app
PlayApp().run()
