from unittest import TestCase
from game import check_status
import io
import unittest.mock


class TestCheckStatus(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_status_print(self, mock_stdout):
        character = {"name": "John", "health": 10, 'current_coordinates': [1, 1], 'level': 1, 'exp': 0,
                     'location': 'Playground', 'class': {'level_name': "Amateur Wrestler", "MAX_HEALTH": (20, 30),
                                                         "EXP_REQ": (200, 300)}, 'inventory': []}
        check_status(character)
        expected = 'You are in the:\x1b[33mPlayground\x1b[0m\nJohn: The level 1 A.\n\x1b[31mHP: 10/20\x1b[0m\t \x1b[32mEXP: 0/200\x1b[0m\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_check_status_return_is_none(self):
        character = {"name": "John", "health": 10, 'current_coordinates': [1, 1], 'level': 1, 'exp': 0,
                     'location': 'Playground', 'class': {'level_name': "Amateur Wrestler", "MAX_HEALTH": (20, 30),
                                                         "EXP_REQ": (200, 300)}, 'inventory': []}
        self.assertIsNone(check_status(character))

    def test_check_status_character_dict_unchanged(self):
        character = {"name": "John", "health": 10, 'current_coordinates': [1, 1], 'level': 1, 'exp': 0,
                     'location': 'Playground', 'class': {'level_name': "Amateur Wrestler", "MAX_HEALTH": (20, 30),
                                                         "EXP_REQ": (200, 300)}, 'inventory': []}
        check_status(character)
        expected = {"name": "John", "health": 10, 'current_coordinates': [1, 1], 'level': 1, 'exp': 0,
                    'location': 'Playground', 'class': {'level_name': "Amateur Wrestler", "MAX_HEALTH": (20, 30),
                                                        "EXP_REQ": (200, 300)}, 'inventory': []}
        self.assertEqual(character, expected)
