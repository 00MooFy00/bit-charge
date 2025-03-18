from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

# Импортируем наши экраны
from screens import start_screen
StartScreen = start_screen.StartScreen
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
