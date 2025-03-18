# screens/login_screen.py

from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from widgets.custom_buttons import RoundGradientButton

def login_user(email, password):
    """Простая заглушка логики логина"""
    print("[DEBUG] login_user called:", email, password)

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = [0.1, 0.1, 0.1, 1]

        hints = ['Email', 'Пароль']
        self.fields = []

        for i, hint in enumerate(hints):
            field = MDTextField(
                hint_text=hint,
                size_hint=(0.8, None),
                height=48,
                pos_hint={'center_x': 0.5, 'center_y': 0.65 - i * 0.12},
                password=('Пароль' in hint),
                mode='round'
            )
            self.fields.append(field)
            self.add_widget(field)

        # Кнопка "Войти"
        btn_login = RoundGradientButton(
            text='Войти',
            size_hint=(0.7, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.38},
            on_press=self._on_login
        )
        self.add_widget(btn_login)

        # Кнопка "Назад"
        btn_back = MDFlatButton(
            text='Назад',
            pos_hint={'center_x': 0.5, 'center_y': 0.20},
            text_color='white',
            on_press=lambda x: setattr(self.manager, 'current', 'main')
        )
        self.add_widget(btn_back)

    def _on_login(self, instance):
        email = self.fields[0].text
        password = self.fields[1].text
        login_user(email, password)
