import unittest

from rover import Rover


class RoverTestCase(unittest.TestCase):
    def setUp(self):
        self.rover = Rover(1, 2, "N")

    def test_create_rover(self):
        self.assertEqual(self.rover.x, 1)
        self.assertEqual(self.rover.y, 2)
        self.assertEqual(self.rover.orientation.value, "N")

    def test_rotate_left(self):
        self.rover.rotate_left()
        self.assertEqual(self.rover.orientation.value, "W")
        self.rover.rotate_left()
        self.assertEqual(self.rover.orientation.value, "S")
        self.rover.rotate_left()
        self.assertEqual(self.rover.orientation.value, "E")
        self.rover.rotate_left()
        self.assertEqual(self.rover.orientation.value, "N")

    def test_rotate_right(self):
        self.rover.rotate_right()
        self.assertEqual(self.rover.orientation.value, "E")
        self.rover.rotate_right()
        self.assertEqual(self.rover.orientation.value, "S")
        self.rover.rotate_right()
        self.assertEqual(self.rover.orientation.value, "W")
        self.rover.rotate_right()
        self.assertEqual(self.rover.orientation.value, "N")

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

    def test_process(self):
        plateau = [5, 5]
        self.rover.process(plateau, "LMLMLMLMM")
        self.assertEqual(self.rover.position(), "1 3 N")
        self.rover = Rover(3, 3, "E")
        self.rover.process(plateau, "MMRMMRMRRM")
        self.assertEqual(self.rover.position(), "5 1 E")

    def test_process_with_exception(self):
        plateau = [5, 5]
        with self.assertRaises(Exception) as context:
            self.rover.process(plateau, "LMM")
        self.assertTrue("Position invalid" in str(context.exception))
        with self.assertRaises(Exception) as context:
            self.rover.process(plateau, "LMLMMM")
        self.assertTrue("Position invalid" in str(context.exception))

    def test_invalid_position(self):
        plateau = [5, 5]
        self.assertEqual(self.rover.is_invalid_position(plateau), False)
        self.rover = self.rover = Rover(-1, 2, "W")
        self.assertEqual(self.rover.is_invalid_position(plateau), True)

    def test_position(self):
        self.assertEqual(self.rover.position(), "1 2 N")
        self.rover = self.rover = Rover(3, 4, "E")
        self.assertEqual(self.rover.position(), "3 4 E")
