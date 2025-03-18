# screens/register_screen.py

from screens.base_screen import BaseScreen
from kivymd.uix.textfield import MDTextField
from widgets.custom_buttons import RoundGradientButton

def register_user(name, email, pwd, pwd2):
    # Заглушка
    print("[DEBUG] регистрация:", name, email, pwd, pwd2)

class RegisterScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Три поля (или четыре) - 30% ширины
        self.name_field = MDTextField(
            hint_text="Имя",
            mode='rectangle',
            size_hint=(0.3, None),
            height=44,
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        self.add_widget(self.name_field)

        self.email_field = MDTextField(
            hint_text="Почта",
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
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            password=True
        )
        self.add_widget(self.pass1_field)

        self.pass2_field = MDTextField(
            hint_text="Повтор пароля",
            mode='rectangle',
            size_hint=(0.3, None),
            height=44,
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            password=True
        )
        self.add_widget(self.pass2_field)

        # Кнопка "Зарегистрироваться" (оранжевая, 0.4 ширины, 50 высота)
        self.btn_register = RoundGradientButton(
            text='Зарегистрироваться',
            size_hint=(0.4, None),
            height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.28},
            on_press=self._on_register
        )
        self.add_widget(self.btn_register)

        # Кнопка "Назад" (чёрная)
        self.btn_back = RoundGradientButton(
            text='Назад',
            size_hint=(0.4, None),
            height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.18},
            color_bottom=(0, 0, 0, 1),
            color_top=(0.2, 0.2, 0.2, 1),
            on_press=lambda x: setattr(self.manager, 'current', 'main')
        )
        self.add_widget(self.btn_back)

    def _on_register(self, instance):
        name = self.name_field.text
        email = self.email_field.text
        pwd = self.pass1_field.text
        pwd2 = self.pass2_field.text
        register_user(name, email, pwd, pwd2)
