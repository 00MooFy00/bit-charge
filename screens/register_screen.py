# screens/register_screen.py

from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from widgets.custom_buttons import RoundGradientButton

def register_user(name, email, pwd, pwd2):
    if pwd != pwd2:
        print("[DEBUG] Пароли не совпадают!")
        return
    print(f"[DEBUG] Регистрация:\nИмя: {name}\nEmail: {email}\nПароль: {pwd}")

class RegisterScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = [0.1, 0.1, 0.1, 1]

        hints = ['Имя', 'Почта', 'Пароль', 'Повторите пароль']
        self.fields = []

        for i, hint in enumerate(hints):
            field = MDTextField(
                hint_text=hint,
                size_hint=(0.8, None),
                height=48,
                pos_hint={'center_x': 0.5, 'center_y': 0.75 - (0.12 * i)},
                password=('Пароль' in hint),
                mode='round'
            )
            self.fields.append(field)
            self.add_widget(field)

        # Кнопка "Зарегистрироваться"
        btn_register = RoundGradientButton(
            text='Зарегистрироваться',
            size_hint=(0.7, 0.07),
            pos_hint={'center_x': 0.5, 'center_y': 0.25},
            on_press=self._on_register
        )
        self.add_widget(btn_register)

        # Кнопка "Назад"
        btn_back = MDFlatButton(
            text='Назад',
            pos_hint={'center_x': 0.5, 'center_y': 0.15},
            text_color='white',
            on_press=lambda x: setattr(self.manager, 'current', 'main')
        )
        self.add_widget(btn_back)

    def _on_register(self, instance):
        name = self.fields[0].text
        email = self.fields[1].text
        pwd = self.fields[2].text
        pwd2 = self.fields[3].text
        register_user(name, email, pwd, pwd2)
