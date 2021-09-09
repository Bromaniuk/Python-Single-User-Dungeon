from unittest import TestCase
from game import keep_fighting
import unittest
from unittest.mock import patch
import io


class TestKeepFighting(TestCase):

    @patch('builtins.input', side_effect=["1"])
    def test_keep_fighting_decision_fight_return_is_True(self, mock_input):
        actual = keep_fighting()
        self.assertEqual(actual, True)

    @patch('builtins.input', side_effect=["2"])
    def test_keep_fighting_decision_fight_return_is_False(self, mock_input):
        actual = keep_fighting()
        self.assertEqual(actual, False)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["1"])
    def test_keep_fighting_decision_print(self, mock_input, mock_stdout):
        keep_fighting()
        expected = "\nIt's your turn! Would you like to keep fighting or retreat?!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('builtins.input', side_effect=["hello", "6", "1"])
    def test_keep_fighting_invalid_inputs_then_valid_input(self, mock_input):
        actual = keep_fighting()
        self.assertEqual(actual, True)

    @patch('builtins.input', side_effect=["1"])
    def test_keep_fighting_decision_fight_return_is_boolean(self, mock_input):
        actual = keep_fighting()
        self.assertIsInstance(actual, bool)
