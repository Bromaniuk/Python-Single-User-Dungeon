from unittest import TestCase
from game import enemy_first
import unittest
import io
from unittest.mock import patch


class TestEnemyFirst(TestCase):

    @patch('random.randint', side_effect=[5, 5])
    def test_enemy_first_each_take_damage(self, mock_randint):
        character = {'name': 'Jake', 'current_coordinates': [0, 1], 'level': 1, 'exp': 0, 'location': 'Playground',
                     'inventory': [], 'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                                               'Football Captain'),
                                                'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                                                'attack': 'You throw a football and hit the',
                                                'EXP_REQ': (150, 300, 'MAX')}, 'health': 22}
        foe = {'name': 'Class Clown', 'exp': 15, 'health': 10, 'MAX_DMG': 10,
               'attack': 'Boom! The Class Clown hits you with some bad jokes!',
               'death_message': 'The Class Clown has had his last laugh, he cowers in shame!'}
        enemy_first(character, foe)
        self.assertEqual(character["health"], 17)
        self.assertEqual(foe["health"], 5)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[5, 5])
    def test_enemy_first_each_take_damage_print(self, mock_randint, mock_stdout):
        character = {'name': 'John', 'current_coordinates': [0, 1], 'level': 1, 'exp': 0, 'location': 'Playground',
                     'inventory': [], 'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                                               'Football Captain'),
                                                'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                                                'attack': 'You throw a football and hit the',
                                                'EXP_REQ': (150, 300, 'MAX')}, 'health': 22}
        foe = {'name': 'Class Clown', 'exp': 15, 'health': 10, 'MAX_DMG': 10,
               'attack': 'Boom! The Class Clown hits you with some bad jokes!',
               'death_message': 'The Class Clown has had his last laugh, he cowers in shame!'}
        enemy_first(character, foe)
        expected = '\nBoom! The Class Clown hits you with some bad jokes! Your health decreased from 22 to 17.' \
                   '\nYou throw a football and hit the Class Clown! Their health decreased from 10 to 5.\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_enemy_first_return_none(self):
        character = {'name': 'John', 'current_coordinates': [0, 1], 'level': 1, 'exp': 0, 'location': 'Playground',
                     'inventory': [], 'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                                               'Football Captain'),
                                                'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                                                'attack': 'You throw a football and hit the',
                                                'EXP_REQ': (150, 300, 'MAX')}, 'health': 22}
        foe = {'name': 'Class Clown', 'exp': 15, 'health': 10, 'MAX_DMG': 10,
               'attack': 'Boom! The Class Clown hits you with some bad jokes!',
               'death_message': 'The Class Clown has had his last laugh, he cowers in shame!'}
        self.assertIsNone(enemy_first(character, foe))

    @patch('random.randint', side_effect=[10, 10])
    def test_enemy_first_opponent_if_player_dies(self, mock_randint):
        character = {'name': 'John', 'current_coordinates': [0, 1], 'level': 1, 'exp': 0, 'location': 'Playground',
                     'inventory': [],
                     'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                              'Football Captain'),
                               'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                               'attack': 'You throw a football and hit the',
                               'EXP_REQ': (150, 300, 'MAX')}, 'health': 5}
        foe = {'name': 'Class Clown', 'exp': 15, 'health': 20, 'MAX_DMG': 10,
               'attack': 'Boom! The Class Clown hits you with some bad jokes!',
               'death_message': 'The Class Clown has had his last laugh, he cowers in shame!'}
        enemy_first(character, foe)
        self.assertEqual(character["health"], -5)
        self.assertEqual(foe["health"], 20)
