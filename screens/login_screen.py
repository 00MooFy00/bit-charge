# screens/login_screen.py

from screens.base_screen import BaseScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from widgets.custom_buttons import RoundGradientButton
from db_utils import check_login, is_verified, get_confirm_code
from email_utils import send_confirm_code

class LoginScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.error_label = MDLabel(
            text='',
            halign='center',
            theme_text_color='Custom',
            text_color=(1,0,0,1),
            pos_hint={'center_x': 0.5, 'center_y': 0.75}
        )
        self.add_widget(self.error_label)

        self.email_field = MDTextField(
            hint_text="Email",
            mode='rectangle',
            size_hint=(0.3, None),
            height=44,
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        self.add_widget(self.email_field)

        self.pass_field = MDTextField(
            hint_text="Пароль",
            mode='rectangle',
            size_hint=(0.3, None),
            height=44,
            password=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(self.pass_field)

        # Кнопка "Войти"
        btn_login = RoundGradientButton(
            text='Войти',
            size_hint=(0.4, None),
            height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.38},
            on_press=self._on_login
        )
        self.add_widget(btn_login)

        # Кнопка "Назад"
        btn_back = RoundGradientButton(
            text='Назад',
            size_hint=(0.4, None),
            height=50,
            color_bottom=(0,0,0,1),
            color_top=(0.2,0.2,0.2,1),
            pos_hint={'center_x': 0.5, 'center_y': 0.28},
            on_press=lambda x: setattr(self.manager, 'current', 'main')
        )
        self.add_widget(btn_back)

        # Кнопка "Отправить код" (изначально прячем)
        self.btn_resend = RoundGradientButton(
            text='Отправить код повторно',
            size_hint=(0.4, None),
            height=50,
            color_bottom=(0,0,0,1),
            color_top=(0.2,0.2,0.2,1),
            pos_hint={'center_x': 0.5, 'center_y': 0.18},
            on_press=self._on_resend_code
        )
        self.btn_resend.opacity = 0
        self.btn_resend.disabled = True
        self.add_widget(self.btn_resend)

    def _on_login(self, instance):
        email = self.email_field.text.strip().lower()
        password = self.pass_field.text.strip()

        if check_login(email, password):
            # Логин и пароль верны. Проверим, verified ли
            if is_verified(email):
                self.error_label.text = ""
                # Переходим на карту
                self.manager.current = "map"
            else:
                self.error_label.text = "Подтвердите email!"
                # Показать кнопку "Отправить код повторно"
                self.btn_resend.opacity = 1
                self.btn_resend.disabled = False
        else:
            self.error_label.text = "Неверный логин или пароль!"
            self.btn_resend.opacity = 0
            self.btn_resend.disabled = True

    def _on_resend_code(self, instance):
        """
        Отправляет код снова и переводит на экран "confirm_code".
        Можно генерировать новый код, либо брать старый из БД.
        """
        email = self.email_field.text.strip().lower()
        if not email:
            return
        # Можно взять старый код
        code = get_confirm_code(email)
        if not code:
            self.error_label.text = "Пользователь не найден (резенд)."
            return

        # Отправляем код снова
        send_confirm_code(email, code)

        # Переходим к экрану ввода кода
        confirm_screen = self.manager.get_screen("confirm_code")
        confirm_screen.set_email(email)
        self.manager.current = "confirm_code"
