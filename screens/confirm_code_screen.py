# screens/confirm_code_screen.py
from screens.base_screen import BaseScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from widgets.custom_buttons import RoundGradientButton
from db_utils import get_confirm_code, verify_user

class ConfirmCodeScreen(BaseScreen):
    """
    Экран ввода кода подтверждения. Предполагаем, что при переходе
    сюда мы знаем email, который надо подтвердить.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.email_to_confirm = None  # будем задавать извне
        self.error_label = MDLabel(
            text='',
            halign='center',
            theme_text_color='Custom',
            text_color=(1,0,0,1),  # красный
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        self.add_widget(self.error_label)

        self.field_code = MDTextField(
            hint_text="Введите код",
            mode='rectangle',
            size_hint=(0.3, None),
            height=44,
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        self.add_widget(self.field_code)

        btn_confirm = RoundGradientButton(
            text="Подтвердить",
            size_hint=(0.4, None),
            height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.48},
            on_press=self._on_confirm
        )
        self.add_widget(btn_confirm)

        btn_back = RoundGradientButton(
            text="Назад",
            size_hint=(0.4, None),
            height=50,
            color_bottom=(0,0,0,1),
            color_top=(0.2,0.2,0.2,1),
            pos_hint={'center_x': 0.5, 'center_y': 0.38},
            on_press=lambda x: setattr(self.manager, 'current', 'main')
        )
        self.add_widget(btn_back)

    def set_email(self, email: str):
        """
        Вызывается при переходе на экран,
        чтобы мы знали, чей код нужно проверять.
        """
        self.email_to_confirm = email

    def _on_confirm(self, instance):
        if not self.email_to_confirm:
            self.error_label.text = "Ошибка: email неизвестен!"
            return

        code_entered = self.field_code.text.strip()
        real_code = get_confirm_code(self.email_to_confirm)

        if real_code is None:
            self.error_label.text = "Пользователь не найден!"
            return

        if code_entered == real_code:
            # Верный код
            verify_user(self.email_to_confirm)
            self.error_label.text = ""
            # Переходим на экран логина (или сразу на карту)
            self.manager.current = "login"
        else:
            self.error_label.text = "Неверный код!"
