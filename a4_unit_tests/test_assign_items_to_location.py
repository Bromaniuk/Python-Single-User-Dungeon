from unittest import TestCase
from unittest.mock import patch

from game import assign_items_to_location


class TestAssignItemsToLocation(TestCase):

    @patch('random.randint', side_effect=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7])
    def test_assign_items_to_location(self, mock_randint):
        board = {(x_value, y_value): ' \U0001F7EB ' for y_value in range(25) for x_value in range(25)}
        assign_items_to_location(board)
        x, y = 1, 1
        for coord in range(7):
            self.assertEqual(board[(x, y)], ' 📄 ')
            x += 1
            y += 1

    def test_assign_items_to_location_return_is_none(self):
        board = {(x_value, y_value): ' \U0001F7EB ' for y_value in range(25) for x_value in range(25)}
        actual = assign_items_to_location(board)
        self.assertIsNone(actual)
