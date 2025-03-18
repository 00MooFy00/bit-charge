# screens/base_screen.py

from kivymd.uix.screen import MDScreen
from kivy.graphics import Rectangle, Color

class BaseScreen(MDScreen):
    """
    Базовый экран, который рисует картинку-фон на весь экран.
    Все остальные экраны будут наследоваться от этого класса.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            # Можно поставить Color(1,1,1,1) если нужна непрозрачная картинка
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(
                source='assets/background.png',  # <-- подставь свою картинку
                pos=self.pos,
                size=self.size
            )

        # Следим за размером и позицией экрана, чтобы фон растягивался
        self.bind(pos=self._update_bg, size=self._update_bg)

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
