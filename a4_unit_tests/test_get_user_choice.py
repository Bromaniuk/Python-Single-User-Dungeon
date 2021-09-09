from unittest import TestCase
from game import get_user_choice
import unittest
from unittest.mock import patch
import io


class TestGetUserChoice(TestCase):

    @patch('builtins.input', side_effect=["menu", "1"])
    def test_get_user_choice_one(self, mock_input):
        character = {'name': 'John'}
        actual = get_user_choice(character)
        self.assertEqual(actual, "1")

    @patch('builtins.input', side_effect=["1"])
    def test_get_user_choice_one_no_menu(self, mock_input):
        character = {'name': 'John'}
        actual = get_user_choice(character)
        self.assertEqual(actual, "1")

    @patch('builtins.input', side_effect=["5", "3"])
    def test_get_user_choice_backpack(self, mock_input):
        character = {'name': 'John', 'inventory': ['a', 'b', 'c']}
        actual = get_user_choice(character)
        self.assertEqual(actual, "3")

    @patch('builtins.input', side_effect=["3"])
    def test_get_user_choice_return_is_string(self, mock_input):
        character = {'name': 'John'}
        actual = get_user_choice(character)
        self.assertIsInstance(actual, str)
