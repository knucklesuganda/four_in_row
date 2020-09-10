from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.list import MDList


class ThemeWidget(ScrollView):
    def __init__(self, app, return_back):
        super(ThemeWidget, self).__init__()
        self.list = MDList()
        self.app = app

        themes = [
            'Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue',
            'Cyan', 'Teal', 'Green', 'LightGreen', 'DeepOrange', 'Brown', 'Gray', 'BlueGray',
            'Lime', 'Yellow', 'Amber', 'Orange'
        ]
        self.return_button = MDIconButton(icon="arrow-left-circle",
                                          size_hint=(1, None),
                                          pos_hint={"center_x": 0.5, "center_y": 0.7},
                                          on_press=lambda x: return_back())
        self.list.add_widget(self.return_button)

        for theme in themes:
            self.list.add_widget(
                MDRaisedButton(
                    text=theme,
                    on_press=self.change_theme,
                    size_hint=(1, None),
                    pos_hint={"center_x": 0.5, "center_y": 0.7}
                )
            )
        self.add_widget(self.list)

    def change_theme(self, instance):
        self.app.theme_cls.primary_palette = instance.text
