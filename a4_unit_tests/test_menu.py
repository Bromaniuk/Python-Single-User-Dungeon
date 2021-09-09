from unittest import TestCase
from game import menu
from unittest.mock import patch
import unittest
import io


class TestMenu(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_menu_print(self, mock_stdout):
        menu()
        expected = 'Enter the number corresponding to your desired choice:\n0 - Quit\n1 - Up/North\n2 - ' \
                   'Right/East\n3 - South/Down\n4 - Left/West\n5 - Backpack\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_menu_return_none(self):
        self.assertIsNone(menu())
