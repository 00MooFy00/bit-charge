# screens/register_screen.py
from screens.base_screen import BaseScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from widgets.custom_buttons import RoundGradientButton
from db_utils import user_exists, create_user
from email_utils import send_confirm_code
import random

class RegisterScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = [0.1, 0.1, 0.1, 1]

        self.error_label = MDLabel(
            text='',
            halign='center',
            theme_text_color='Custom',
            text_color=(1,0,0,1),  # красный цвет
            pos_hint={'center_x': 0.5, 'center_y': 0.83}
        )
        self.add_widget(self.error_label)

        self.name_field = MDTextField(
            hint_text="Имя",
            mode='rectangle',
            size_hint=(0.3, None),
            height=44,
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        self.add_widget(self.name_field)

        self.email_field = MDTextField(
            hint_text="Email",
            mode='rectangle',
            size_hint=(0.3, None),
            height=44,
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        self.add_widget(self.email_field)

        self.pass1_field = MDTextField(
            hint_text="Пароль",
            mode='rectangle',
            size_hint=(0.3, None),
            height=44,
            password=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(self.pass1_field)

        self.pass2_field = MDTextField(
            hint_text="Повтор пароля",
            mode='rectangle',
            size_hint=(0.3, None),
            height=44,
            password=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        self.add_widget(self.pass2_field)

        self.btn_register = RoundGradientButton(
            text='Зарегистрироваться',
            size_hint=(0.4, None),
            height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.28},
            on_press=self._on_register
        )
        self.add_widget(self.btn_register)

        self.btn_back = RoundGradientButton(
            text='Назад',
            color_bottom=(0,0,0,1),
            color_top=(0.2,0.2,0.2,1),
            size_hint=(0.4, None),
            height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.18},
            on_press=lambda x: setattr(self.manager, 'current', 'main')
        )
        self.add_widget(self.btn_back)

    def _on_register(self, instance):
        name = self.name_field.text.strip()
        email = self.email_field.text.strip().lower()
        pwd1 = self.pass1_field.text.strip()
        pwd2 = self.pass2_field.text.strip()

        if not name or not email or not pwd1 or not pwd2:
            self.error_label.text = "Все поля обязательны!"
            return

        if pwd1 != pwd2:
            self.error_label.text = "Пароли не совпадают!"
            return

        # Проверим, нет ли такого email
        if user_exists(email):
            self.error_label.text = "Пользователь с таким email уже существует!"
            return

        # Генерируем код подтверждения (6 цифр)
        code = str(random.randint(100000, 999999))

        # Создаём юзера в БД (verified=0)
        create_user(name, email, pwd1, code)

        # Отправляем код (пока просто печатаем в консоль)
        send_confirm_code(email, code)

        self.error_label.text = ""
        # Переходим на экран confirm_code
        confirm_screen = self.manager.get_screen("confirm_code")
        confirm_screen.set_email(email)
        self.manager.current = "confirm_code"
