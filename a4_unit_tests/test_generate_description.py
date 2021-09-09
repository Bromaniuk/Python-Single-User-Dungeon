from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io

from game import generate_description


class TestGenerateDescription(TestCase):

    @patch('random.choice', side_effect=["look around", "weird", "person"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_random_description(self, mock_stdout, mock_choice):
        character = {'location': 'Playground'}
        generate_description(character)
        expected = '\nYou look around and see a weird person.\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_generate_random_description_return_is_none(self):
        character = {'location': 'Playground'}
        self.assertIsNone(generate_description(character))

    def test_generate_random_description_dict_unchanged(self):
        character = {'location': 'Playground'}
        generate_description(character)
        expected = {'location': 'Playground'}
        self.assertEqual(character, expected)

