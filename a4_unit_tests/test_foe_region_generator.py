from unittest import TestCase
from game import foe_region_generator
from unittest.mock import patch


class TestFoeRegionGenerator(TestCase):
    def test_foe_region_generator_return_is_dict(self):
        character = {"location": "Playground"}
        actual = foe_region_generator(character)
        self.assertIsInstance(actual, dict)

    @patch('random.randint', side_effect=[1])
    def test_for_region_generator_teachers_pet_foe_in_teacher_lounge(self, mock_randint):
        character = {"location": "Teacher's Lounge"}
        actual = foe_region_generator(character)
        self.assertEqual(actual, {'name': "Teacher's Pet", 'exp': 12, 'health': 8, 'MAX_DMG': 10,
                                  'attack': "Thwap! The Teacher's Pet smacks you with a booklet full of optional "
                                   "homework assignments!", 'death_message': "The Teacher's Pet runs to "
                                   "tell on you to the nearest Teacher!"})

    @patch('random.randint', side_effect=[0])
    def test_foe_region_generator_lunch_lady_in_cafeteria(self, mock_randint):
        character = {"location": "Cafeteria"}
        actual = foe_region_generator(character)
        self.assertEqual(actual, {'name': 'Lunch Lady', 'exp': 15, 'health': 10, 'MAX_DMG': 10,
                                  'attack': 'Twang! The Lunch Lady smacks you upside the head with a ladle!',
                                  'death_message': 'The Lunch Lady retreats to the cafeteria!'})

    @patch('random.randint', side_effect=[2])
    def test_foe_region_generator_mean_girl_in_playground(self, mock_randint):
        character = {"location": "Playground"}
        actual = foe_region_generator(character)
        self.assertEqual(actual, {'name': 'Mean Girl', 'exp': 15, 'health': 10, 'MAX_DMG': 10,
                                  'attack': 'Rude! The Mean Girl just made fun of your outfit!',
                                  'death_message': 'The Mean Girl runs away to cry in the bathroom!'})

    @patch('random.randint', side_effect=[0])
    def test_foe_region_generator_teacher_in_principals_office(self, mock_randint):
        character = {"location": "Principal's Office"}
        actual = foe_region_generator(character)
        self.assertEqual(actual, {'name': 'Teacher', 'exp': 22, 'health': 15, 'MAX_DMG': 10,
                                  'attack': 'Smack! The Teacher strikes you with a ruler!',
                                  'death_message': 'The Teacher retreats to the staff lounge!'})
