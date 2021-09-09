from unittest import TestCase
from game import create_boss


class TestCreateBoss(TestCase):

    def test_create_boss_return_is_dict(self):
        self.assertIsInstance(create_boss(), dict)
