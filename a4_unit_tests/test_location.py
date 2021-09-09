from unittest import TestCase
from game import location
import io
import unittest.mock
from unittest.mock import patch


class TestLocation(TestCase):

    def test_location_return_none(self):
        character = {"name": "John", "health": 10, 'current_coordinates': [1, 1], 'level': 1, 'exp': 0,
                     'location': 'Playground', 'class': {'level_name': "Amateur Wrestler", "MAX_HEALTH": (20, 30),
                                                         "EXP_REQ": (200, 300)}, 'inventory': []}
        board = {(x_value, y_value): ' \U0001F7EB ' for y_value in range(25) for x_value in range(25)}
        notes = ['h', 'o', 's']
        self.assertIsNone(location(character, board, notes))

    def test_location_character_dict_unchanged(self):
        character = {"name": "John", "health": 10, 'current_coordinates': [1, 1], 'level': 1, 'exp': 0,
                     'location': 'Playground', 'class': {'level_name': "Amateur Wrestler", "MAX_HEALTH": (20, 30),
                                                         "EXP_REQ": (200, 300)}, 'inventory': []}
        board = {(x_value, y_value): ' \U0001F7EB ' for y_value in range(25) for x_value in range(25)}
        notes = []
        location(character, board, notes)
        expected = {"name": "John", "health": 10, 'current_coordinates': [1, 1], 'level': 1, 'exp': 0,
                    'location': 'Playground', 'class': {'level_name': "Amateur Wrestler", "MAX_HEALTH": (20, 30),
                                                        "EXP_REQ": (200, 300)}, 'inventory': []}
        self.assertEqual(character, expected)

    @patch('random.choice', side_effect=["look around", "weird", "person"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_location_print_board(self, mock_stdout, mock_randchoice):
        character = {"name": "Jimmy", "health": 10, 'current_coordinates': [1, 1], 'level': 1, 'exp': 0,
                     'location': 'Playground', 'class': {'level_name': "Amateur Wrestler", "MAX_HEALTH": (20, 30),
                                                         "EXP_REQ": (200, 300)}, 'inventory': []}
        board = {(x_value, y_value): ' \U0001F7EB ' for y_value in range(25) for x_value in range(25)}
        notes = []
        location(character, board, notes)
        expected = '\nYou look around and see a weird person.\n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  ' \
                   '🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 \n 🟫  🤺  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 ' \
                   ' 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 ' \
                   ' 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 ' \
                   ' 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 ' \
                   ' 🟫  🟫  🟫  🟫  🟫  🟫  🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 ' \
                   ' 🟫  🟫  🟫  🟫  🟫  🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 ' \
                   ' 🟫  🟫  🟫  🟫  🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  ' \
                   '🟫  🟫  🟫  🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  ' \
                   '🟫  🟫  🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 ' \
                   ' 🟫  🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 ' \
                   ' 🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  ' \
                   '🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 ' \
                   ' 🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  ' \
                   '🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  ' \
                   '🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  ' \
                   '🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  ' \
                   '🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  ' \
                   '🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 ' \
                   ' 🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  ' \
                   '🟫  🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  ' \
                   '🟫  🟫  🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 ' \
                   ' 🟫  🟫  🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  ' \
                   '🟫  🟫  🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫 ' \
                   ' 🟫  🟫 \n 🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  🟫  ' \
                   '🟫  🟫 \nYou are in the:\x1b[33mPlayground\x1b[0m\nJimmy: The level 1 A.\n\x1b[31mHP: ' \
                   '10/20\x1b[0m\t \x1b[32mEXP: 0/200\x1b[0m\n'
        self.assertEqual(mock_stdout.getvalue(), expected)
