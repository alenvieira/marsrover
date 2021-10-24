import sys
from enum import Enum


class Orientation(Enum):
    NORTH = ("N", "W", "E")
    SOUTH = ("S", "E", "W")
    EAST = ("E", "N", "S")
    WEST = ("W", "S", "N")

    def __new__(cls, abbreviation, direction_left, direction_right):
        obj = object.__new__(cls)
        obj.abbreviation = obj._value_ = abbreviation
        obj.direction_left = direction_left
        obj.direction_right = direction_right
        return obj


class Movement(Enum):
    NORTH = ("N", "y", 1)
    SOUTH = ("S", "y", -1)
    EAST = ("E", "x", 1)
    WEST = ("W", "x", -1)

    def __new__(cls, abbreviation, axe, value_movement):
        obj = object.__new__(cls)
        obj.abbreviation = obj._value_ = abbreviation
        obj.axe = axe
        obj.value_movement = value_movement
        return obj


class Rover:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = Orientation(orientation)
        self.actions = {"M": self.move, "L": self.rotate_left, "R": self.rotate_right}

    def rotate_left(self):
        self.orientation = Orientation(self.orientation.direction_left)

    def rotate_right(self):
        self.orientation = Orientation(self.orientation.direction_right)

    def move(self):
        movement = Movement(self.orientation.value)
        if movement.axe == "x":
            self.x += movement.value_movement
        elif movement.axe == "y":
            self.y += movement.value_movement

    def process(self, plateau, instructions):
        for instruction in instructions:
            action = self.actions.get(instruction)
            action()
            if self.is_invalid_position(plateau):
                raise Exception("Position invalid")

    def is_invalid_position(self, plateau):
        return self.x < 0 or self.x > plateau[0] or self.y < 0 or self.y > plateau[1]

    def position(self):
        return "{} {} {}".format(self.x, self.y, self.orientation.value)


if __name__ == "__main__":
    test_input = sys.stdin.read()
    lines = [line.strip() for line in test_input.splitlines()]
    plateau = [int(i) for i in lines[0].split(" ")]
    expected_output = []
    lines = iter(lines[1:])
    for line in lines:
        line1 = line.strip()
        line2 = next(lines).strip()
        x, y, orientation = line1.split(" ")
        rover = Rover(int(x), int(y), orientation)
        rover.process(plateau, line2)
        expected_output.append(rover.position())
    for output in expected_output:
        print(output)
