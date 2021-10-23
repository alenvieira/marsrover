import unittest


class Rover:
    def __init__(self, x=0, y=0, orientation="S"):
        self.x = x
        self.y = y
        self.orientation = orientation


class RoverTestCase(unittest.TestCase):
    def setUp(self):
        self.rover = Rover(1, 2, "N")

    def test_create_rover(self):
        self.assertEqual(self.rover.x, 1)
        self.assertEqual(self.rover.y, 2)
        self.assertEqual(self.rover.orientation, "N")
