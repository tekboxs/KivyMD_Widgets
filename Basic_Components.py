from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

Window.size = (400, 650) # resize window like a mobile


class MainInterface(MDBoxLayout):
		# Class that will be used to build interface 
    pass


class TextAnalyserApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
				# All widgets that use main color will be Red in "normal" mode
        self.theme_cls.theme_style = "Dark"
				# By default set color "Red" to dark version


TextAnalyserApp().run()
