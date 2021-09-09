from unittest import TestCase
import unittest
import io
from unittest.mock import patch
from game import foe_flee


class TestFoeFlee(TestCase):
    @patch('random.randint', side_effect=[1])
    def test_foe_flee_return_is_bool(self, mock_randint):
        foe = {"death_message": "You have died"}
        actual = foe_flee(foe)
        self.assertIsInstance(actual, bool)

    @patch('random.randint', side_effect=[10])
    def test_foe_flee_return_is_True(self, mock_randint):
        foe = {"death_message": "You have died"}
        actual = foe_flee(foe)
        self.assertEqual(actual, True)

    @patch('random.randint', side_effect=[50])
    def test_foe_flee_return_is_none(self, mock_randint):
        foe = {"death_message": "You have died"}
        actual = foe_flee(foe)
        self.assertEqual(actual, None)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[10])
    def test_foe_flee_print(self, mock_randint, mock_stdout):
        foe = {"death_message": "You have died"}
        foe_flee(foe)
        expected = "\nYour adversary has decided to flee!\nYou have died\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
