# screens/login_screen.py

from screens.base_screen import BaseScreen
from kivymd.uix.textfield import MDTextField
from widgets.custom_buttons import RoundGradientButton

def login_user(email, password):
    print(f"[DEBUG] Логин: {email}, Пароль: {password}")

class LoginScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Поля ввода: ~1/3 экрана по ширине
        self.field_email = MDTextField(
            hint_text="Email",
            mode='rectangle',  # или 'fill_rounded' с меньшим скруглением
            size_hint=(0.3, None),  # 30% экрана
            height=44,
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
        )
        self.add_widget(self.field_email)

        self.field_password = MDTextField(
            hint_text="Пароль",
            mode='rectangle',
            size_hint=(0.3, None),
            height=44,
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            password=True
        )
        self.add_widget(self.field_password)

        # Кнопка "Войти" (оранжевая, пошире, допустим 0.4)
        self.btn_login = RoundGradientButton(
            text='Войти',
            size_hint=(0.4, None),  # На 30% шире, чем поле (0.4 против 0.3)
            height=50,  # Чем больше высота, тем более "пилюля"
            pos_hint={'center_x': 0.5, 'center_y': 0.38},
            on_press=self._on_login,
            # По умолчанию у тебя color_bottom=(1,0.3,0,1) и color_top=(1,0.6,0,1)
            # Можно менять, если хочешь другой оранжевый
        )
        self.add_widget(self.btn_login)

        # Кнопка "Назад" (чёрная)
        self.btn_back = RoundGradientButton(
            text='Назад',
            size_hint=(0.4, None),
            height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.28},
            color_bottom=(0, 0, 0, 1),
            color_top=(0.2, 0.2, 0.2, 1),
            on_press=lambda x: setattr(self.manager, 'current', 'main')
        )
        self.add_widget(self.btn_back)

    def _on_login(self, instance):
        email = self.field_email.text
        password = self.field_password.text
        login_user(email, password)
