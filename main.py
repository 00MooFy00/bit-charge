# main.py

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
# Импортируем наши экраны
from screens.start_screen import StartScreen
from screens.login_screen import LoginScreen
from screens.register_screen import RegisterScreen

class BitChargeApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        sm = ScreenManager()
        sm.add_widget(StartScreen(name='main'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(LoginScreen(name='login'))

        sm.current = 'main'
        return sm

if __name__ == '__main__':
    BitChargeApp().run()
