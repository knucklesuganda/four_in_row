from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.app import MDApp


class StartWidget(MDBoxLayout):
    def __init__(self, start_game, change_theme):
        super(StartWidget, self).__init__()
        self.add_widget(MDLabel(text=MDApp.get_running_app().title, font_style="H4",
                                size_hint=(1, 1), halign="left"))
        buttons_box = MDBoxLayout(orientation="vertical", size_hint=(1, None), spacing=4)
        theme_cls = MDApp.get_running_app().theme_cls

        buttons_box.add_widget(MDRaisedButton(text="Start game", on_press=lambda _: start_game(),
                                              md_bg_color=theme_cls.primary_color))
        buttons_box.add_widget(MDRaisedButton(text="Change theme", on_press=lambda _: change_theme(),
                                              md_bg_color=theme_cls.primary_color))
        buttons_box.add_widget(MDRaisedButton(text="Exit", on_press=self.exit_game,
                                              md_bg_color=theme_cls.primary_color))
        self.add_widget(buttons_box)

    def exit_game(self, _):
        exit(0)

