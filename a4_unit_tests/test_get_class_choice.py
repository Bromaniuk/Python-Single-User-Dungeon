from unittest import TestCase
from unittest.mock import patch

from game import get_class_choice


class TestGetClassChoice(TestCase):

    @patch('builtins.input', side_effect=["1"])
    def test_get_class_choice_input(self, mock_input):
        character = {'class': {}, 'level': 1}
        get_class_choice(character)
        actual = character['class']
        expected = {'name': 'Nerd', 'level_name': ('Math Wiz', 'Computer Lab Lurker', 'Chess Club President'), 'MAX_DMG': (14, 18, 24), 'MAX_HEALTH': (14, 18, 24), 'attack': 'You throw a calculator and hit the', 'EXP_REQ': (50, 150, 'MAX')}
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["1"])
    def test_get_class_choice_return_none(self, mock_input):
        character = {'class': {}, 'level': 1}
        self.assertIsNone(get_class_choice(character))
