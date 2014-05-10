from kivy.app import App
from kivy.properties import ListProperty


class DaumenkivyApp(App):
    """Basic kivy app

    Edit daumenkivy.kv to get started.
    """

    flip_books = ListProperty()

    def build(self):
        return self.root
