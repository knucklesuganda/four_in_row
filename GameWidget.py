from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.label import MDLabel, MDIcon
from kivy.clock import Clock
from kivymd.app import MDApp
from Game import Game


class GameWidget(MDBoxLayout):
    def __init__(self):
        super(GameWidget, self).__init__()
        self.orientation = "vertical"
        self.game = Game()
        self.game_grid = MDGridLayout(cols=5)
        self.error_label = MDLabel(text="", color=[1, 0, 0, 1])

        for i in range(20):
            self.game_grid.add_widget(MDIcon(icon="moon-new"))

        self.game_controls = MDBoxLayout(orientation="horizontal")
        self.game_controls.add_widget(MDIconButton(icon="arrow-collapse-left",
                                                   on_press=lambda _: self.move(True)))
        self.game_controls.add_widget(MDIconButton(icon="arrow-down-bold",
                                                   on_press=self.drop_cell))
        self.game_controls.add_widget(MDIconButton(icon="arrow-collapse-right",
                                                   on_press=lambda _: self.move(False)))

        self.add_widget(MDLabel(text=MDApp.get_running_app().title))
        self.add_widget(self.error_label)
        self.add_widget(self.game_grid)
        self.add_widget(self.game_controls)

    def drop_cell(self, instance):
        try:
            self.game.move("drop")
            self.update_game()
        except:
            self.error_label.text = "Position occupied!"

    def update_game(self):
        self.remove_widget(self.game_grid)
        self.game_grid = MDGridLayout(cols=5)
        self.add_widget(self.game_grid)

        for i in range(self.game.get_pos() - 1):
            self.game_grid.add_widget(MDIcon())
        self.game_grid.add_widget(MDIcon(icon="album"))

        if self.game.get_pos() < 5:
            for i in range(5 - self.game.get_pos()):
                self.game_grid.add_widget(MDIcon())

        print(self.game.get_pos())

        for row in self.game.show_field():
            for chip in row:
                if chip == 0:
                    self.game_grid.add_widget(MDIcon(icon="moon-new"))
                elif chip == 1:
                    self.game_grid.add_widget(MDIcon(icon="numeric-1-circle"))
                elif chip == 2:
                    self.game_grid.add_widget(MDIcon(icon="numeric-2-circle"))

        self.remove_widget(self.game_controls)
        self.add_widget(self.game_controls)

    def move(self, is_left):
        if is_left:
            self.game.move("left")
        else:
            self.game.move("right")
        self.update_game()
