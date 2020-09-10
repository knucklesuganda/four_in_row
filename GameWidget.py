from kivymd.app import MDApp

from Game import Game
from kivy.uix.popup import Popup
from kivymd.uix.label import MDIcon, MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDIconButton, MDRaisedButton


class ControlsBox(MDBoxLayout):
    pass


class GameField(MDGridLayout):
    pass


class GameWidget(MDBoxLayout):
    def __init__(self, return_back):
        super(GameWidget, self).__init__()
        self.orientation = "vertical"
        self.return_back = return_back
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

    def win(self):
        theme_cls = MDApp.get_running_app().theme_cls
        win_popup = Popup(title=f"User {self.game.current_player} won!")

        content = MDBoxLayout(orientation="vertical", md_bg_color=theme_cls.primary_dark)
        content.add_widget(MDLabel(text=f"User {self.game.current_player} won!",
                                   theme_text_color='Primary', halign="center"))
        content.add_widget(MDRaisedButton(text="Exit", on_press=lambda x: self.game_win_return(win_popup),
                                          size_hint=(1, None), md_bg_color=theme_cls.primary_color,
                                          font_size="20"))

        win_popup.content = content
        win_popup.open()

    def update_game(self):
        if not self.game.is_running:
            self.win()
            return

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

    def game_win_return(self, popup):
        popup.dismiss()
        self.return_back()
