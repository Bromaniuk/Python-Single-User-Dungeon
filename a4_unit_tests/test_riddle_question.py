from unittest import TestCase
from game import riddle_question
import io
import unittest.mock
from unittest.mock import patch


class TestRiddleQuestion(TestCase):

    @patch('builtins.input', side_effect=["story"])
    def test_riddle_question_return_is_bool(self, mock_input):
        character = {"name": "Jimmy", "inventory": ['s', 't', 'o']}

        actual = riddle_question(character)
        self.assertIsInstance(actual, bool)

    @patch('builtins.input', side_effect=["history"])
    def test_riddle_question_return_true(self, mock_input):
        character = {"name": "Jimmy", "inventory": ['s', 't', 'o']}
        actual = riddle_question(character)
        self.assertEqual(actual, True)

    @patch('builtins.input', side_effect=["shark"])
    def test_riddle_question_return_false(self, mock_input):
        character = {"name": "Jimmy", "inventory": ['s', 't', 'o']}
        actual = riddle_question(character)
        self.assertEqual(actual, False)

