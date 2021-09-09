from unittest import TestCase
from game import validate_move


class TestValidateMove(TestCase):

    def test_validate_move_true(self):
        character = {"current_coordinates": [0, 3]}
        direction = "1"
        actual = validate_move(character, direction)
        self.assertEqual(actual, True)

    def test_validate_move_false(self):
        character = {"current_coordinates": [0, 3]}
        direction = "4"
        actual = validate_move(character, direction)
        self.assertEqual(actual, False)

    def test_validate_move_return_is_bool(self):
        character = {"current_coordinates": [0, 3]}
        direction = "1"
        actual = validate_move(character, direction)
        self.assertIsInstance(actual, bool)

    def test_validate_move_coordinate_unchanged(self):
        character = {"current_coordinates": [0, 3]}
        direction = "1"
        validate_move(character, direction)
        self.assertEqual(character['current_coordinates'], [0, 3])
