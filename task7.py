class Snow:
    def __init__(self, qty):
        self.snow = qty

    def __call__(self, qty):
        self.snow = qty

    def __add__(self, n):
        self.snow += n

    def __sub__(self, n):
        self.snow -= n

    def __mul__(self, n):
        self.snow *= n

    def __truediv__(self, n):
        self.snow = round(self.snow / n)

    def make_snow(self, row):
        return '\n'.join(['*' * row] * (self.snow // row) + ['*' * (self.snow % row)])
