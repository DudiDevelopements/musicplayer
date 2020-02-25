# Importa o kivy:
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

# Importa o necessario para reproduzir o som:
import pygame
import os

# Inicializa o pygame
pygame.init()


def play_music(music_path):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

    pygame.time.Clock()
    clock.tick(10)


def stop_music():
    pygame.mixer.music.stop()


class RootWidget(FloatLayout):
    pass


class PlayApp(App):

    def build(self):
        return RootWidget()


PlayApp().run()
