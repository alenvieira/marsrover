import unittest


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


class RoverTestCase(unittest.TestCase):
    def setUp(self):
        self.rover = Rover(1, 2, "N")

    def test_create_rover(self):
        self.assertEqual(self.rover.x, 1)
        self.assertEqual(self.rover.y, 2)
        self.assertEqual(self.rover.orientation, "N")

    def test_rotate_left(self):
        self.rover.rotate_left()
        self.assertEqual(self.rover.orientation, "W")
        self.rover.rotate_left()
        self.assertEqual(self.rover.orientation, "S")
        self.rover.rotate_left()
        self.assertEqual(self.rover.orientation, "E")
        self.rover.rotate_left()
        self.assertEqual(self.rover.orientation, "N")

    def test_rotate_right(self):
        self.rover.rotate_right()
        self.assertEqual(self.rover.orientation, "E")
        self.rover.rotate_right()
        self.assertEqual(self.rover.orientation, "S")
        self.rover.rotate_right()
        self.assertEqual(self.rover.orientation, "W")
        self.rover.rotate_right()
        self.assertEqual(self.rover.orientation, "N")
