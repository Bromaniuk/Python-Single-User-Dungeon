from unittest import TestCase
from unittest.mock import patch
import unittest
import io

from game import get_item


class TestGetItem(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_get_item_inventory_empty(self, mock_stdout):
        character = {'inventory': []}
        notes = ["a", "b", "c"]
        get_item(character, notes)
        expected = "You notice a scrap of paper on the ground with the letter 'a' written on it... Hmm... " \
                   "You might need this later.\nYou put it in your backpack!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_get_item_added_to_inventory(self):
        character = {'inventory': []}
        notes = ["a", "b", "c"]
        get_item(character, notes)
        expected = {'inventory': ["a"]}
        self.assertEqual(character, expected)

    def test_get_item_notes_subtracted(self):
        character = {'inventory': []}
        notes = ["a", "b", "c"]
        get_item(character, notes)
        expected = ["b", "c"]
        self.assertEqual(notes, expected)

    def test_get_item_return_none(self):
        character = {'inventory': []}
        notes = ["a", "b", "c"]
        self.assertIsNone(get_item(character, notes))

    def test_get_item_note_is_string(self):
        character = {'inventory': []}
        notes = ["a", "b", "c"]
        get_item(character, notes)
        self.assertIsInstance(notes[0], str)
        self.assertIsInstance(character['inventory'][0], str)
