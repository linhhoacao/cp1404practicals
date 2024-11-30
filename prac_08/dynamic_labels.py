"""
CP1404/Practical 8
Dynamic Labels
Estimate time: 30'
Actual time: 35'
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class DynamicLabelsApp(App):
    def build(self):
        names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

        main_layout = BoxLayout(orientation='vertical')
        for name in names:
            button = Button(text=name, font_size=24)
            button.bind(on_press=self.on_button_click)
            main_layout.add_widget(button)

        return main_layout

    def on_button_click(self, button):
        button.background_color = (0, 0.5, 0.5, 1)  # Change button color on click


DynamicLabelsApp().run()