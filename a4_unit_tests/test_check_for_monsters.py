from unittest import TestCase
from unittest.mock import patch
from game import check_for_monsters


class TestCheckForMonsters(TestCase):

    @patch('random.randint', side_effect=[10])
    def test_check_for_monsters_roll_true(self, mock_randint):
        actual = check_for_monsters()
        self.assertEqual(actual, True)

    @patch('random.randint', side_effect=[50])
    def test_check_for_monsters_roll_false(self, mock_randint):
        actual = check_for_monsters()
        self.assertEqual(actual, False)

    def test_check_for_monsters_return_is_bool(self):
        actual = check_for_monsters()
        self.assertIsInstance(actual, bool)
