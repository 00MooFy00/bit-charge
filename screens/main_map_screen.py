# screens/main_map_screen.py

from screens.base_screen import BaseScreen
from kivy_garden.mapview import MapView, MapMarkerPopup
from widgets.custom_buttons import RoundGradientButton

class MainMapScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mapview = MapView(
            lat=55.75,
            lon=37.62,
            zoom=10,
            size_hint=(1, 1)
        )
        self.add_widget(self.mapview)

        # Пример кнопки "Назад"
        self.btn_back = RoundGradientButton(
            text="Назад",
            size_hint=(0.2, None),
            height=40,
            color_bottom=(0,0,0,1),
            color_top=(0.2,0.2,0.2,1),
            pos_hint={'x': 0, 'y': 0.95},
            on_press=lambda x: setattr(self.manager, 'current', 'main')
        )
        self.add_widget(self.btn_back)

        # Пример маркера
        marker = MapMarkerPopup(lat=55.76, lon=37.64)
        self.mapview.add_widget(marker)
