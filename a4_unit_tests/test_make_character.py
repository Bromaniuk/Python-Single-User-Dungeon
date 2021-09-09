from unittest import TestCase
from unittest.mock import patch
import unittest.mock
from game import make_character
import io


class TestMakeCharacter(TestCase):


    @patch('builtins.input', side_effect=["", "Alexander", "1"])
    def test_make_character_input_name(self, mock_input):
        actual = make_character()
        expected = "Alexander"
        self.assertEqual(actual['name'], expected)

    @patch('builtins.input', side_effect=["", "John", "2"])
    def test_make_character_input_is_string(self, mock_input):
        actual = make_character()
        self.assertIsInstance(actual['name'], str)

    @patch('builtins.input', side_effect=["", "Erica", "3"])
    def test_make_character_dict_key(self, mock_input):
        actual = make_character()
        expected = "Erica"
        self.assertIn(expected, actual.values())

    @patch('builtins.input', side_effect=["1", "Jeff", "4"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_make_character_print_intro_dialogue(self, mock_stdout, mock_input):
        make_character()
        expected = "Another boring day at Riverside High School...\n                                                " \
                   "                                   \n                                                            " \
                   "                    \n                             @@@@@@                                       " \
                   "      \n                            ,@@@@@@@                                            \n      " \
                   "                       @@@@@@%                                            \n                    " \
                   "          @@@@@                                             \n                        &@@@@@@@@@@" \
                   "                                             \n                     /@@@@@@@@@@@@@@@@@           " \
                   "            @                 \n                     @@@@@@@@@@@@@@@@@@@                  @.    " \
                   "                \n                   .@@@@@@@@@@@@@@@@@@@@             &@                       " \
                   "  \n                  @@@@@%@@@@@@@@@@@@@@@@/  .@@@@@@@@                            \n           " \
                   "       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                \n                    @@@@@@" \
                   "@@@@@@@@@@@@ &.                                       \n                      @@@@@@@@@@@@@@@@%  " \
                   "                                       \n                      @@@@@@@@@@@@@@@@@                 " \
                   "                        \n                     .@@@@@@@@@@@@@@@@@@                               " \
                   "         \n                        @@@@@@@@@@@@@@@                                         \n    " \
                   "                    @@@@@@@@@@@@@@@                                         \n                  " \
                   "      @@@@@@@@@@@@@@@                                         \n                        &@@@@@@(" \
                   "@@@@@@@                                         \n                         @@@@@@ @@@@@@@       " \
                   "                                  \n                         @@@@@   @@@@@@                     " \
                   "                    \n                         @@@@@   @@@@@@                                   " \
                   "      \n                         @@@@@   &@@@@@                                         \n      " \
                   "                  %@@@@,   @@@@@@                                         \n                    " \
                   "    (@@@@@   @@@@@*                                         \n                         @@@@@   " \
                   "@@@@@                                          \n                         @@@@,  .@@@@         " \
                   "                                  \n                          @@@@  &@@@@@@                    " \
                   "                     \n                                                                        " \
                   "        \n                                                                                \n\nY" \
                   "ou are dozing in and out during Math class...\n\nMr.Thompson: ..ahem..\nMr.Thompson: Ahem.\nMr." \
                   "Thompson: !!AHEM!!\n\nYou jolt awake!\nYou open your eyes and see your math teacher, and everyo" \
                   "ne else in the class, staring at you!\n\nMr.Thompson: Aha! I assume you are so tired because yo" \
                   "u were up all last night studying!\nMr.Thompson: In that case, please tell me what the 96th numb" \
                   "er in the fibonacci sequence is!\nYou: Uhhmmm... is it... \n\nRRRRRIIIIIINNNNGGGG!\n\nMr.Thompso" \
                   "n: Hmm... It seems like you've been saved by the bell once again.\nMr.Thompson: None the matter!" \
                   " Report to Principal Filbert's office after school for 3 hours of detention!\n\nRats! That was " \
                   "totally bogus, man!\nYou head outside and meet up with your group of friends...\n\nBill: Hey man" \
                   ", that was so not cool of Mr.Thompson!\nTed: Yeah! I wish there was something we could do to get" \
                   " back at all of the lame teachers!\nBill: I've got it! Let's execute Operation Swordfish! Everyo" \
                   "ne got their walkie-talkies?\nTed: Yeah! Let's do it, dude! I'll head to the Cafeteria and start" \
                   " a food-fight! My codename will be Hawk!\nBill: I'll go to the Teacher's Lounge and burn popcor" \
                   "n in their microwave! You can call me Bullseye over the radio!\nBilly: Dude, remember the plan?" \
                   " You've got to take on Principal Filbert!\n\nCool Cool... So are you a...\n\n1 - \x1b[32m\x1b[1" \
                   "mNerd\x1b[0m - You're a Nerd. That's right. I said it. You spend most nights staying up late to" \
                   " study and play with rubik's cubes.\nYou are proud to be a Nerd. However, teachers have been as" \
                   "signing you homework that you think is beneath you and you are SICK of it!\nThis is your chance" \
                   " to fight back against the teachers you loathe! (EASY: Fast leveling, weak start)\n\n2 - \x1b[" \
                   "34m\x1b[1mJock\x1b[0m - Is your name Chad? It probably is. You have been playing every sport o" \
                   "ut there since you were old enough to throw a ball.\nIt's kind of all you know. Like, really, " \
                   "you're failing most of your courses besides gym class. You are more than ready to fight back\na" \
                   "gainst the administration and this is your chance! (EASY)\n\n3 - \x1b[33m\x1b[1mPretty Girl\x1b" \
                   "[0m - You put more effort into your captions on Instagram than you have for this entire school " \
                   "year. It's time to give up.\nYou barely classify as a micro-influencer. You've been able to get" \
                   " decent grades so far since all you do is ask the nearest nerd\nif they would like to do your h" \
                   "omework for you. However, your teachers are beginning to realize that you are cheating and are" \
                   " getting your parents involved.\nI think it's about time you gave the administration a piece o" \
                   "f your mind! No matter how small it is! (MEDIUM)\n\n4 - \x1b[31m\x1b[1mGoth Kid\x1b[0m - They " \
                   "just don't get you. We understand. But, maybe the tri-color mohawk is a bit much? No? Okay, tha" \
                   "t's fine.\nJust put your headphones back on, resume your Linkin Park playlist, and let's go to " \
                   "war! (HARD: Slow leveling but high gains)\nBill: Alright! So Jeff the Goth Kid, eh? Lets get cr" \
                   "ackin'!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('builtins.input', side_effect=["", "Alexander", "1"])
    def test_make_character_returns_dict(self, mock_input):
        actual = make_character()
        self.assertIsInstance(actual, dict)
