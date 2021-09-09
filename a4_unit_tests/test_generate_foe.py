from unittest import TestCase
from game import generate_foe


class TestGenerateFoe(TestCase):

    def test_generate_foe_return_is_list(self):
        actual = generate_foe()
        self.assertIsInstance(actual, list)

    def test_generate_foe_list_in_lists(self):
        actual = generate_foe()
        self.assertIsInstance(actual[0], list)

    def test_generate_foe_list_in_list_is_dict(self):
        actual = generate_foe()
        self.assertIsInstance(actual[0][0], dict)

    def test_generate_foe_list_length(self):
        actual = generate_foe()
        self.assertEqual(len(actual), 4)
