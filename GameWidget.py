from kivy.uix.anchorlayout import AnchorLayout

from Game import Game
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDFlatButton, MDIconButton


class ControlsBox(MDBoxLayout):
    pass


class GameField(MDGridLayout):
    pass


class GameWidget(MDBoxLayout):
    def __init__(self, return_back):
        super(GameWidget, self).__init__()
        self.orientation = "vertical"
        self.ids.return_button.on_press = return_back

        self.game = Game()
        self.game_grid = GameField(cols=5)

        for i in range(20):
            self.game_grid.add_widget(MDIcon(icon="moon-new"))

        self.game_controls = ControlsBox()
        self.game_controls.add_widget(MDIconButton(icon="arrow-collapse-left", on_press=lambda _: self.move(True)))
        self.game_controls.add_widget(MDIconButton(icon="arrow-down-bold", on_press=self.drop_cell))
        self.game_controls.add_widget(MDIconButton(icon="arrow-collapse-right",
                                                   on_press=lambda _: self.move(False)))
        self.add_widget(self.game_grid)
        self.add_widget(self.game_controls)

        self.update_game()

    def drop_cell(self, _):
        try:
            self.game.move("drop")
            self.update_game()
        except IndexError:
            self.ids.error_label.text = "Position occupied!"

    def update_game(self):
        self.remove_widget(self.game_grid)
        self.game_grid = MDGridLayout(cols=5, pos_hint={"center": 0.5})
        self.add_widget(self.game_grid)

        for i in range(self.game.get_pos() - 1):
            self.game_grid.add_widget(MDIcon(icon="square-outline"))
        self.game_grid.add_widget(MDIcon(icon="radiobox-marked"))

        if self.game.get_pos() < 5:
            for i in range(5 - self.game.get_pos()):
                self.game_grid.add_widget(MDIcon(icon="square-outline"))

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
