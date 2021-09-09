from unittest import TestCase
from game import heal_character
import io
import unittest.mock


class TestHealCharacter(TestCase):

    def test_heal_character_return_is_dict(self):
        character = {"name": "John", "health": 10, 'current_coordinates': [1, 1], 'level': 1, 'exp': 0,
                     'location': 'Playground', 'class': {'level_name': "Amateur Wrestler", "MAX_HEALTH": (20, 30),
                                                         "EXP_REQ": (200, 300)}, 'inventory': []}
        actual = heal_character(character)
        self.assertIsInstance(actual, dict)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_heal_character_print(self, mock_stdout):
        character = {"name": "John", "health": 10, 'current_coordinates': [1, 1], 'level': 1, 'exp': 0,
                     'location': 'Playground', 'class': {'level_name': "Amateur Wrestler", "MAX_HEALTH": (20, 30),
                                                         "EXP_REQ": (200, 300)}, 'inventory': []}
        heal_character(character)
        expected = '\nYou rest in the hallway and regain your courage!\nYour health has increased from 10 to 14.\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_heal_character_health_changed(self):
        character = {"name": "John", "health": 10, 'current_coordinates': [1, 1], 'level': 1, 'exp': 0,
                     'location': 'Playground', 'class': {'level_name': "Amateur Wrestler", "MAX_HEALTH": (20, 30),
                                                         "EXP_REQ": (200, 300)}, 'inventory': []}
        heal_character(character)
        self.assertEqual(character['health'], 14)

    def test_heal_character_max_health_unchanged(self):
        character = {"name": "John", "health": 20, 'current_coordinates': [1, 1], 'level': 1, 'exp': 0,
                     'location': 'Playground', 'class': {'level_name': "Amateur Wrestler", "MAX_HEALTH": (20, 30),
                                                         "EXP_REQ": (200, 300)}, 'inventory': []}
        heal_character(character)
        self.assertEqual(character['health'], 20)
