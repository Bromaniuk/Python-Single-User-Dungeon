from unittest import TestCase
import unittest.mock
import io
from game import check_inventory


class TestCheckInventory(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_inventory_3_notes_print(self, mock_stdout):
        character = {'inventory': ['a', 'b', 'c']}
        check_inventory(character)
        expected = "You reach into your back pack and pull out a few scraps of paper. " \
                   "All put together, you have the letters abc.\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_inventory_empty_print(self, mock_stdout):
        character = {'inventory': []}
        check_inventory(character)
        expected = "You do not have anything interesting in your backpack.\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_check_inventory_dict_unchanged(self):
        character = {'inventory': ['a', 'b', 'c']}
        check_inventory(character)
        expected = {'inventory': ['a', 'b', 'c']}
        self.assertEqual(character, expected)

    def test_check_inventory_is_list(self):
        character = {'inventory': ['a', 'b', 'c']}
        check_inventory(character)
        self.assertIsInstance(character['inventory'], list)

    def test_check_inventory_note_is_string(self):
        character = {'inventory': ['a', 'b', 'c']}
        check_inventory(character)
        self.assertIsInstance(character['inventory'][0], str)

    def test_check_inventory_return_is_none(self):
        character = {'inventory': ['a', 'b', 'c']}
        self.assertIsNone(check_inventory(character))
