from kivy.uix.carousel import Carousel
from kivy.properties import StringProperty


class FlipBook(Carousel):
    """Carousel representing the timeline of the animation.
    """
    name = StringProperty()