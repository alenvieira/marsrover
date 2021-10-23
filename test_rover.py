import unittest

from rover import Rover


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

    def test_move(self):
        self.rover.move()
        self.assertEqual(self.rover.y, 3)
        self.rover.rotate_right()
        self.rover.move()
        self.assertEqual(self.rover.x, 2)
        self.rover.rotate_right()
        self.rover.move()
        self.assertEqual(self.rover.y, 2)
        self.rover.rotate_right()
        self.rover.move()
        self.assertEqual(self.rover.x, 1)
