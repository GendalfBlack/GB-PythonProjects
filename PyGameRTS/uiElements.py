from components import *


class Icon(UI):
    def __init__(self, pos=(0,0)):
        super().__init__()
        self.pos = pos


class TextUI(UI):
    def __init__(self, pos=(0,0)):
        super().__init__()
        self.pos = pos