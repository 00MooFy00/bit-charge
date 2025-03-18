# widgets/custom_buttons.py

from kivymd.uix.button import MDRaisedButton
from kivy.graphics import Color, RoundedRectangle

class RoundGradientButton(MDRaisedButton):
    """
    Кнопка с овальным "градиентом" (двухцветная заливка),
    обходя передачу новых свойств в super().__init__().
    """

    def __init__(self, **kwargs):
        # "Вырезаем" наши цвета из kwargs,
        # чтобы KivyMD не пытался их интерпретировать как Property.
        self._color_bottom = kwargs.pop('color_bottom', (1, 0.3, 0, 1))
        self._color_top = kwargs.pop('color_top', (1, 0.6, 0, 1))

        # Теперь вызываем конструктор MDRaisedButton без лишних аргументов
        super().__init__(**kwargs)

        # Настраиваем canvas.before для "псевдо-градиента"
        with self.canvas.before:
            # Нижний цвет
            self._color_bottom_instr = Color(rgba=self._color_bottom)
            self._rect_bottom = RoundedRectangle(
                pos=self.pos, size=self.size, radius=[30]
            )
            # Верхний цвет
            self._color_top_instr = Color(rgba=self._color_top)
            self._rect_top = RoundedRectangle(
                pos=self.pos, size=self.size, radius=[30]
            )

        # Следим за изменением pos и size, чтобы перерисовывать
        self.bind(pos=self._update_canvas, size=self._update_canvas)

    def _update_canvas(self, *args):
        # Нижняя часть
        self._rect_bottom.pos = self.pos
        self._rect_bottom.size = self.size

        # Верхняя часть (делим кнопку напополам по высоте)
        self._rect_top.pos = (self.x, self.y + self.height / 2)
        self._rect_top.size = (self.width, self.height / 2)

        # Чтобы кнопка была максимально "овальной", radius = половине высоты
        r = self.height / 2
        self._rect_bottom.radius = [r]
        self._rect_top.radius = [r]
