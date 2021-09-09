from unittest import TestCase
from game import check_level
import unittest
import io
from unittest.mock import patch


class TestCheckLevel(TestCase):
    def test_check_level_return_is_none(self):
        character = {'name': 'John', 'current_coordinates': [0, 1], 'level': 1, 'exp': 0, 'location': 'Playground',
                     'inventory': [], 'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                                               'Football Captain'),
                                                'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                                                'attack': 'You throw a football and hit the',
                                                'EXP_REQ': (150, 300, 'MAX')}, 'health': 22}
        self.assertIsNone(check_level(character))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_check_level_level_up_print(self, mock_stdout):
        character = {'name': 'John', 'current_coordinates': [0, 1], 'level': 1, 'exp': 170, 'location': 'Playground',
                     'inventory': [], 'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                                               'Football Captain'),
                                                'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                                                'attack': 'You throw a football and hit the',
                                                'EXP_REQ': (150, 300, 'MAX')}, 'health': 22}
        check_level(character)
        expected = '\nDing! Congratulations, John! You have advanced to level 2!' \
                   '\nYou are now a Basketball Lead!' \
                   '\nYour maximum health has increased to 27 and maximum damage has increased to 27.\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_check_level_character_unchanged(self):
        character = {'name': 'John', 'current_coordinates': [0, 1], 'level': 1, 'exp': 0, 'location': 'Playground',
                     'inventory': [], 'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                                               'Football Captain'),
                                                'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                                                'attack': 'You throw a football and hit the',
                                                'EXP_REQ': (150, 300, 'MAX')}, 'health': 22}
        check_level(character)
        expected = {'name': 'John', 'current_coordinates': [0, 1], 'level': 1, 'exp': 0, 'location': 'Playground',
                    'inventory': [], 'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                                              'Football Captain'),
                                               'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                                               'attack': 'You throw a football and hit the',
                                               'EXP_REQ': (150, 300, 'MAX')}, 'health': 22}
        self.assertEqual(character, expected)
