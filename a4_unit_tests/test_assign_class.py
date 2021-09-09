from unittest import TestCase
from game import assign_class


class TestAssignClass(TestCase):

    def test_assign_class_dict_is_changed(self):
        character = {'health': 10, 'level': 1}
        assign_class(character, class_choice="1")
        expected = {'class': {'EXP_REQ': (50, 150, 'MAX'),
                              'MAX_DMG': (14, 18, 24),
                              'MAX_HEALTH': (14, 18, 24),
                              'attack': 'You throw a calculator and hit the',
                              'level_name': ('Math Wiz',
                                             'Computer Lab Lurker',
                                             'Chess Club President'),
                              'name': 'Nerd'},
                    'health': 14,
                    'level': 1}
        self.assertEqual(character, expected)

    def test_assign_class_is_dict(self):
        character = {'health': 10, 'level': 1}
        assign_class(character, class_choice="2")
        self.assertIsInstance(character, dict)

    def test_assign_class_health_is_int(self):
        character = {'health': 10, 'level': 1}
        assign_class(character, class_choice="2")
        self.assertIsInstance(character['health'], int)

    def test_assign_class_class_is_dict(self):
        character = {'health': 10, 'level': 1}
        assign_class(character, class_choice="3")
        self.assertIsInstance(character['class'], dict)

    def test_assign_class_returns_none(self):
        character = {'health': 10, 'level': 1}
        class_choice = "2"
        self.assertIsNone(assign_class(character, class_choice))
