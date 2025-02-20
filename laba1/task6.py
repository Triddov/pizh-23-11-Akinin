import math

class WinDoor:
    def __init__(self, w, h):
        self.square = w * h

class Room:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
        self.wd = []

    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))

    def work_surface(self):
        return 2 * self.height * (self.length + self.width) - sum(wd.square for wd in self.wd)

    def wallpapers(self, l, w):
        return math.ceil(self.work_surface() / (w * l))
