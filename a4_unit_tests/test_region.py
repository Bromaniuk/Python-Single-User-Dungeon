from unittest import TestCase
from game import region


class TestRegion(TestCase):

    def test_region_playground_from_cafeteria(self):
        character = {"location": "Cafeteria", "current_coordinates": [15, 15]}
        region(character)
        self.assertEqual(character["location"], "Playground")

    def test_region_cafeteria_from_principals_office(self):
        character = {"location": "Principal's Office", "current_coordinates": [16, 15]}
        region(character)
        self.assertEqual(character["location"], "Cafeteria")

    def test_region_principals_office_from_teachers_lounge(self):
        character = {"location": "Teacher's Lounge", "current_coordinates": [16, 16]}
        region(character)
        self.assertEqual(character["location"], "Principal's Office")

    def test_region_teachers_lounge_from_playground(self):
        character = {"location": "Playground", "current_coordinates": [2, 16]}
        region(character)
        self.assertEqual(character["location"], "Teacher's Lounge")

    def test_region_return_is_none(self):
        character = {"location": "Cafeteria", "current_coordinates": [16, 12]}
        self.assertIsNone(region(character))

    def test_region_coordinates_no_change(self):
        character = {"location": "Cafeteria", "current_coordinates": [16, 12]}
        region(character)
        self.assertEqual(character["current_coordinates"], [16, 12])
