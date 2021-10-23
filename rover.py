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

    def process(self, plateau, instructions):
        for instruction in instructions:
            if instruction == "M":
                self.move()
                if self.is_invalid_position(plateau):
                    raise Exception("Position invalid")
            elif instruction == "L":
                self.rotate_left()
            elif instruction == "R":
                self.rotate_right()

    def is_invalid_position(self, plateau):
        return self.x < 0 or self.x > plateau[0] or self.y < 0 or self.y > plateau[1]

    def position(self):
        return "{} {} {}".format(self.x, self.y, self.orientation)
