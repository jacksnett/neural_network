class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        if self.x > self.y:
            self.label = -1

        else:
            self.label = 1
