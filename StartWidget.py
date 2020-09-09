from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.app import MDApp


class StartWidget(MDBoxLayout):
    def __init__(self, start_game):
        super(StartWidget, self).__init__()
        self.add_widget(MDLabel(text=MDApp.get_running_app().title, font_style="H4"))
        buttons_box = MDBoxLayout(orientation="vertical", size_hint=(None, None))

        buttons_box.add_widget(MDFlatButton(text="Start game", on_press=lambda _: start_game()))
        buttons_box.add_widget(MDFlatButton(text="Exit", on_press=self.exit_game))
        self.add_widget(buttons_box)

    def exit_game(self, _):
        exit(0)

