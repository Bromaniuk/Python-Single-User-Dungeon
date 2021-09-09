from unittest import TestCase
from game import riddle_answer_letter_check


class TestRiddleAnswerLetterCheck(TestCase):

    def test_riddle_answer_letter_check_true(self):
        guess = "h"
        actual = riddle_answer_letter_check(guess)
        self.assertEqual(actual, True)

    def test_riddle_answer_letter_check_false(self):
        guess = "a"
        actual = riddle_answer_letter_check(guess)
        self.assertEqual(actual, False)

    def test_riddle_answer_letter_check_return_is_bool(self):
        guess = ""
        self.assertIsInstance(riddle_answer_letter_check(guess), bool)
