from unittest import TestCase
from game import roll_initiative
import unittest
import io
from unittest.mock import patch


class TestRollInitiative(TestCase):
    @patch('random.randint', side_effect=[50, 20])
    def test_roll_initiative_is_bool(self, mock_randint):
        actual = roll_initiative()
        self.assertIsInstance(actual, bool)

    @patch('random.randint', side_effect=[50, 20])
    def test_roll_initiative_True(self, mock_randint):
        actual = roll_initiative()
        self.assertEqual(actual, True)

    @patch('random.randint', side_effect=[20, 50])
    def test_roll_initiative_False(self, mock_randint):
        actual = roll_initiative()
        self.assertEqual(actual, False)

    @patch('random.randint', side_effect=[10, 10])
    def test_roll_initiative_draw_return_none(self, mock_randint):
        actual = roll_initiative()
        self.assertIsNone(actual)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[10, 10])
    def test_roll_initiative_draw_print(self, mock_randint, mock_stdout):
        roll_initiative()
        expected = "You both parry each other's attack! No damage dealt!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
