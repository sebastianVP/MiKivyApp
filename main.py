from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MiInterfaz(BoxLayout):

    def cambiar_imagen(self):
        if self.ids.img.source == "imagen1.png":
            self.ids.img.source = "imagen2.png"
        else:
            self.ids.img.source = "imagen1.png"


class HolaApp(App):
    def build(self):
        return MiInterfaz()


if __name__ == "__main__":
    HolaApp().run()
