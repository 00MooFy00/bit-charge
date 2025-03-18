from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from widgets.custom_buttons import RoundGradientButton  # твоя кнопка с градиентом

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = [0.1, 0.1, 0.1, 1]

        # Поле "Email" - прямоугольное, уже по ширине
        self.field_email = MDTextField(
            hint_text="Email",
            mode='rectangle',         # минимальное скругление
            size_hint=(0.3, None),    # 30% ширины экрана
            height=48,
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
        )
        self.add_widget(self.field_email)

        # Поле "Пароль" - может тоже rectangle (или fill_rounded).
        self.field_password = MDTextField(
            hint_text="Пароль",
            mode='rectangle',
            size_hint=(0.3, None),
            height=48,
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            password=True
        )
        self.add_widget(self.field_password)

        # Кнопка "Войти": делаем высоту побольше
        self.btn_login = RoundGradientButton(
            text='Войти',
            size_hint=(0.6, None),
            height=60,  # большую высоту -> сильная закруглённость
            pos_hint={'center_x': 0.5, 'center_y': 0.35},
            on_press=self._on_login
        )
        self.add_widget(self.btn_login)

        # Кнопка "Назад" (обычный MDFlatButton, без закруглений)
        self.btn_back = MDFlatButton(
            text='Назад',
            pos_hint={'center_x': 0.5, 'center_y': 0.25},
            text_color='white',
            on_press=lambda x: setattr(self.manager, 'current', 'main')
        )
        self.add_widget(self.btn_back)

    def _on_login(self, instance):
        email = self.field_email.text
        password = self.field_password.text
        print(f"[DEBUG] Логин: {email}, Пароль: {password}")
