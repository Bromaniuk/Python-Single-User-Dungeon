from unittest import TestCase
from game import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_south(self):
        character = {"current_coordinates": [0, 0]}
        direction = "3"
        actual = move_character(character, direction)
        self.assertEqual(actual, {"current_coordinates": [0, 1]})

    def test_move_character_north(self):
        character = {"current_coordinates": [5, 5]}
        direction = "1"
        actual = move_character(character, direction)
        self.assertEqual(actual, {"current_coordinates": [5, 4]})

    def test_move_character_east(self):
        character = {"current_coordinates": [5, 5]}
        direction = "2"
        actual = move_character(character, direction)
        self.assertEqual(actual, {"current_coordinates": [6, 5]})

    def test_move_character_west(self):
        character = {"current_coordinates": [5, 5]}
        direction = "4"
        actual = move_character(character, direction)
        self.assertEqual(actual, {"current_coordinates": [4, 5]})

    def test_move_character_return_is_dict(self):
        character = {"current_coordinates": [0, 0]}
        direction = "3"
        actual = move_character(character, direction)
        self.assertIsInstance(actual, dict)

    def test_move_character_coordinate_is_list(self):
        character = {"current_coordinates": [0, 0]}
        direction = "3"
        actual = move_character(character, direction)
        self.assertIsInstance(actual["current_coordinates"], list)
