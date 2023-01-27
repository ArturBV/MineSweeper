# import enum

# class Modes(enum.Enum):
#     Easy = 1
#     Medium = 2
#     Hard = 3

class Generator():
    def __init__(self):
        self.size = 10
        self.raw_field = self.make_field()

    def make_field(self):
        return [[0 for i in range(  self.size)] for j in range(    self.size)]

    def get_top_pos(self, widgets_n):
        positions = list()

        try:
            for i in range(widgets_n):
                positions.append((0, (i + 1) * self.size // widgets_n - 1))
        except IndexError as e:
            print("Error: number of widgets is above field size!")
            positions = [(0, i) for i in range(self.size)]

        return positions

class Game():
    def __init__(self, mode):
        self.mode = mode
        # self.raw_field = list()

    def start(self):
        pass

if __name__ == "__main__":
    print("Hallo")
    g = Generator()
    print(g.get_top_pos(1));