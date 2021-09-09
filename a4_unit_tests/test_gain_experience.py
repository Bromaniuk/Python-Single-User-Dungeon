from unittest import TestCase
import io
import unittest.mock
from game import gain_experience


class TestGainExperience(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_experience_print(self, mock_stdout):
        character = {'name': 'John', 'current_coordinates': [0, 1], 'level': 1, 'exp': 0, 'location': 'Playground',
                     'inventory': [], 'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                                               'Football Captain'),
                                                'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                                                'attack': 'You throw a football and hit the',
                                                'EXP_REQ': (150, 300, 'MAX')}, 'health': 22}
        foe = {'exp': 20}
        gain_experience(character, foe)
        expected = '\nYou gained 20 experience points for defeating that enemy!\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_gain_experience_character_exp_added(self):
        character = {'name': 'John', 'current_coordinates': [0, 1], 'level': 1, 'exp': 100, 'location': 'Playground',
                     'inventory': [], 'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                                               'Football Captain'),
                                                'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                                                'attack': 'You throw a football and hit the',
                                                'EXP_REQ': (150, 300, 'MAX')}, 'health': 22}
        foe = {'exp': 20}
        gain_experience(character, foe)
        self.assertEqual(character['exp'], 120)

    def test_gain_experience_return_is_none(self):
        character = {'name': 'John', 'current_coordinates': [0, 1], 'level': 1, 'exp': 100, 'location': 'Playground',
                     'inventory': [], 'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                                               'Football Captain'),
                                                'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                                                'attack': 'You throw a football and hit the',
                                                'EXP_REQ': (150, 300, 'MAX')}, 'health': 22}
        foe = {'exp': 20}
        self.assertIsNone(gain_experience(character, foe))
