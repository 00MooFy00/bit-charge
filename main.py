# main.py

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from db_utils import init_db
from screens.start_screen import StartScreen
from screens.register_screen import RegisterScreen
from screens.login_screen import LoginScreen
from screens.confirm_code_screen import ConfirmCodeScreen
from screens.main_map_screen import MainMapScreen

class BitChargeApp(MDApp):
    def build(self):
        # Инициализируем БД (создаст файл, если нет)
        init_db()

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        sm = ScreenManager()
        sm.add_widget(StartScreen(name='main'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(ConfirmCodeScreen(name='confirm_code'))
        sm.add_widget(MainMapScreen(name='map'))

        sm.current = 'main'
        return sm

if __name__ == "__main__":
    BitChargeApp().run()
