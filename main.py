# Importa o kivy:
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button

# Importa o necessario para reproduzir o som:
import pygame
import os

# Inicializa o pygame
pygame.init()

music_path = ''


def play_music():
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

    pygame.time.Clock()
    clock.tick(10)


def stop_music():
    pygame.mixer.music.stop()


class TextInput(Widget):
    pass


class RootWidget(FloatLayout):
    pass


class PlayApp(App):

    def build(self):
        return RootWidget()

    def printPath(self):
        music_path = self.root.ids.pathinput.text
        print(music_path)


PlayApp().run()
