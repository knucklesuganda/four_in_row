import os
from kivy import Config

Config.set('graphics', 'multisamples', '0')
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
from GameWidget import GameWidget
from StartWidget import StartWidget
from kivymd.uix.label import MDLabel
from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout


class Main(MDApp):
    def __init__(self):
        super(Main, self).__init__()
        self.title = "Four in a row"
        self.root = Builder.load_file("style.kv")
        self.current_widget = MDBoxLayout()

        self.start_widget = StartWidget(self.start_game)
        self.current_widget.add_widget(self.start_widget)

    def start_game(self):
        self.current_widget.clear_widgets()
        self.current_widget.add_widget(GameWidget(self.return_back))

    def return_back(self):
        self.current_widget.clear_widgets()
        self.current_widget.add_widget(self.start_widget)

    def build(self):
        return self.current_widget


if __name__ == '__main__':
    Main().run()
