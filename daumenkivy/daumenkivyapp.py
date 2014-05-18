from kivy.app import App
from kivy.properties import ListProperty

from daumenkivy.flipbook import FlipBook


class DaumenkivyApp(App):
    """Basic kivy app

    Edit daumenkivy.kv to get started.
    """

    flip_books = ListProperty()

    def build(self):
        return self.root

    def create_flip_book(self, name):
        fb = FlipBook(name)
        self.flip_books.append(fb)
