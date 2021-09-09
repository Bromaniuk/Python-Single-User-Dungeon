from unittest import TestCase
from game import validate_class_choice
import unittest.mock
import io


class TestValidateClassChoice(TestCase):

    def test_validate_class_choice_is_bool(self):
        expected = validate_class_choice(class_choice="1")
        self.assertIsInstance(expected, bool)

    def test_validate_class_choice_is_bool_false(self):
        expected = validate_class_choice(class_choice="6")
        self.assertEqual(expected, False)

    def test_validate_class_choice_is_bool_true(self):
        expected = validate_class_choice(class_choice="2")
        self.assertEqual(expected, True)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_class_choice_print_string(self, mock_stdout):
        validate_class_choice(class_choice="10")
        expected = "Sorry, that's not a valid choice! Please try again.\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_validate_class_choice_does_not_return_none(self):
        actual = validate_class_choice(class_choice="")
        self.assertIsNotNone(actual)
