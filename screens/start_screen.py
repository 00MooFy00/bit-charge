# screens/start_screen.py

from screens.base_screen import BaseScreen
from kivymd.uix.label import MDLabel
from widgets.custom_buttons import RoundGradientButton
from kivy.clock import Clock
from kivy.graphics import PushMatrix, PopMatrix, Rotate, RoundedRectangle, Color

class GearWidget(BaseScreen):
    """Пример вращающейся шестерёнки."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            PushMatrix()
            self.rotation = Rotate(angle=0, origin=self.center)
            self.rect = RoundedRectangle(
                source='assets/gear.png',
                pos=self.pos,
                size=(50, 50)
            )
            PopMatrix()

        self.bind(pos=self._update_gear, size=self._update_gear)
        Clock.schedule_interval(self._rotate_gear, 1 / 60.)

    def _rotate_gear(self, dt):
        self.rotation.angle += 1
        self.rotation.origin = self.center

    def _update_gear(self, *args):
        self.rect.pos = (self.center_x - 25, self.center_y - 25)
        self.rotation.origin = self.center


class StartScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Заголовок
        title = MDLabel(
            text='bit-charge',
            halign='center',
            font_style='H3',
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            text_color=(1, 0.5, 0, 1),
        )
        self.add_widget(title)

        # Шестерёнка
        gear = GearWidget(
            pos_hint={'center_x': 0.9, 'center_y': 0.9},
            size_hint=(None, None),
            size=(50, 50)
        )
        self.add_widget(gear)

        # Кнопка "Регистрация"
        btn_reg = RoundGradientButton(
            text='Регистрация',
            size_hint=(0.8, 0.08),
            pos_hint={'center_x': 0.5, 'center_y': 0.58},
            on_press=lambda x: setattr(self.manager, 'current', 'register')
        )
        self.add_widget(btn_reg)

        # Кнопка "Вход"
        btn_login = RoundGradientButton(
            text='Вход',
            size_hint=(0.8, 0.08),
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            color_bottom=(0.7, 0.7, 0.7, 1),
            color_top=(0.9, 0.9, 0.9, 1),
            on_press=lambda x: setattr(self.manager, 'current', 'login')
        )
        self.add_widget(btn_login)
