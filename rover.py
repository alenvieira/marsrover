class Rover:
    def __init__(self, x=0, y=0, orientation="S"):
        self.x = x
        self.y = y
        self.orientation = orientation

    def rotate_left(self):
        if self.orientation == "N":
            self.orientation = "W"
        elif self.orientation == "W":
            self.orientation = "S"
        elif self.orientation == "S":
            self.orientation = "E"
        elif self.orientation == "E":
            self.orientation = "N"

    def rotate_right(self):
        if self.orientation == "N":
            self.orientation = "E"
        elif self.orientation == "E":
            self.orientation = "S"
        elif self.orientation == "S":
            self.orientation = "W"
        elif self.orientation == "W":
            self.orientation = "N"

    def move(self):
        if self.orientation == "N":
            self.y += 1
        elif self.orientation == "E":
            self.x += 1
        elif self.orientation == "S":
            self.y -= 1
        elif self.orientation == "W":
            self.x -= 1
