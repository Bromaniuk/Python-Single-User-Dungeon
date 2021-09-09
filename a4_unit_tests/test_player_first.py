from unittest import TestCase
from game import player_first
import unittest
import io
from unittest.mock import patch


class TestPlayerFirst(TestCase):

    @patch('random.randint', side_effect=[5, 5])
    def test_player_first_each_take_damage(self, mock_randint):
        character = {'name': 'Jimmy', 'current_coordinates': [0, 1], 'level': 1, 'exp': 0, 'location': 'Playground',
                     'inventory': [], 'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                                               'Football Captain'),
                                                'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                                                'attack': 'You throw a football and hit the',
                                                'EXP_REQ': (150, 300, 'MAX')}, 'health': 22}
        foe = {'name': 'Class Clown', 'exp': 15, 'health': 10, 'MAX_DMG': 10,
               'attack': 'Boom! The Class Clown hits you with some bad jokes!',
               'death_message': 'The Class Clown has had his last laugh, he cowers in shame!'}
        player_first(character, foe)
        self.assertEqual(character["health"], 17)
        self.assertEqual(foe["health"], 5)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', side_effect=[5, 5])
    def test_player_first_each_take_damage_print(self, mock_randint, mock_stdout):
        character = {'name': 'John', 'current_coordinates': [0, 1], 'level': 1, 'exp': 0, 'location': 'Playground',
                     'inventory': [], 'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                                               'Football Captain'),
                                                'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                                                'attack': 'You throw a football and hit the',
                                                'EXP_REQ': (150, 300, 'MAX')}, 'health': 22}
        foe = {'name': 'Class Clown', 'exp': 15, 'health': 10, 'MAX_DMG': 10,
               'attack': 'Boom! The Class Clown hits you with some bad jokes!',
               'death_message': 'The Class Clown has had his last laugh, he cowers in shame!'}
        player_first(character, foe)
        expected = "\nYou throw a football and hit the Class Clown! Their health decreased from 10 to 5.\n" \
                   "Boom! The Class Clown hits you with some bad jokes! Your health decreased from 22 to 17.\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_player_first_return_none(self):
        character = {'name': 'John', 'current_coordinates': [0, 1], 'level': 1, 'exp': 0, 'location': 'Playground',
                     'inventory': [], 'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                                               'Football Captain'),
                                                'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                                                'attack': 'You throw a football and hit the',
                                                'EXP_REQ': (150, 300, 'MAX')}, 'health': 22}
        foe = {'name': 'Class Clown', 'exp': 15, 'health': 10, 'MAX_DMG': 10,
               'attack': 'Boom! The Class Clown hits you with some bad jokes!',
               'death_message': 'The Class Clown has had his last laugh, he cowers in shame!'}
        self.assertIsNone(player_first(character, foe))

    @patch('random.randint', side_effect=[10, 5])
    def test_player_first_opponent_doesnt_deal_damage_if_dead_first(self, mock_randint):
        character = {'name': 'John', 'current_coordinates': [0, 1], 'level': 1, 'exp': 0, 'location': 'Playground',
                     'inventory': [],
                     'class': {'name': 'Jock', 'level_name': ('Wrestling Amateur', 'Basketball Lead',
                                                              'Football Captain'),
                               'MAX_DMG': (22, 27, 32), 'MAX_HEALTH': (22, 27, 32),
                               'attack': 'You throw a football and hit the',
                               'EXP_REQ': (150, 300, 'MAX')}, 'health': 22}
        foe = {'name': 'Class Clown', 'exp': 15, 'health': 2, 'MAX_DMG': 10,
               'attack': 'Boom! The Class Clown hits you with some bad jokes!',
               'death_message': 'The Class Clown has had his last laugh, he cowers in shame!'}
        player_first(character, foe)
        self.assertEqual(character["health"], 22)
        self.assertEqual(foe["health"], -8)
