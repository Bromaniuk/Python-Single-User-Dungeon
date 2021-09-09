from unittest import TestCase
import unittest
from unittest.mock import patch
import io
from game import cowardice_penalty


class TestCowardicePenalty(TestCase):
    @patch('random.randint', side_effect=[10, 2])
    def test_cowardice_penalty_lose_health(self, mock_randint):
        character = {"health": 20}
        cowardice_penalty(character)
        expected = {"health": 18}
        self.assertEqual(character, expected)

    @patch('random.randint', side_effect=[50])
    def test_cowardice_penalty_no_damage(self, mock_randint):
        character = {"health": 20}
        cowardice_penalty(character)
        expected = {"health": 20}
        self.assertEqual(character, expected)

    def test_cowardice_penalty_is_dict(self):
        character = {"health": 20}
        actual = cowardice_penalty(character)
        self.assertIsInstance(actual, dict)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[50])
    def test_cowardice_penalty_print_if_escape(self, mock_randint, mock_stdout):
        character = {"health": 20}
        cowardice_penalty(character)
        expected = '\nYou have evaded the foes attempt to teach you a lesson! Good work!\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[10, 4])
    def test_cowardice_penalty_print_if_hit(self, mock_randint, mock_stdout):
        character = {"health": 20}
        cowardice_penalty(character)
        expected = '\nDrats! You got hit in the back as you fled like a coward! ' \
                   'Your health has decreased from 20 to 16.\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('random.randint', side_effect=[10, 4])
    def test_cowardice_penalty_character_negative_hp(self, mock_randint):
        character = {"health": 1}
        actual = cowardice_penalty(character)
        expected = {"health": -3}
        self.assertEqual(actual, expected)
