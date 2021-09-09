from unittest import TestCase
import unittest.mock
import io
from game import intro_dialogue
from unittest.mock import patch

class TestIntroDialogue(TestCase):

    @patch('builtins.input', side_effect=["1"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_intro_dialogue(self, mock_stdout, mock_input):
        intro_dialogue()
        expected = "                                                                                   \n              " \
                   "                                                                  \n                             " \
                   "@@@@@@                                             \n                            ,@@@@@@@        " \
                   "                                    \n                             @@@@@@%                       " \
                   "                     \n                              @@@@@                                       " \
                   "      \n                        &@@@@@@@@@@                                             \n       " \
                   "              /@@@@@@@@@@@@@@@@@                       @                 \n                     @" \
                   "@@@@@@@@@@@@@@@@@@                  @.                    \n                   .@@@@@@@@@@@@@@@@@@" \
                   "@@             &@                         \n                  @@@@@%@@@@@@@@@@@@@@@@/  .@@@@@@@@ " \
                   "                           \n                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    " \
                   "            \n                    @@@@@@@@@@@@@@@@@@ &.                                       \n " \
                   "                     @@@@@@@@@@@@@@@@%                                         \n                " \
                   "      @@@@@@@@@@@@@@@@@                                         \n                     .@@@@@@@@@" \
                   "@@@@@@@@@                                        \n                        @@@@@@@@@@@@@@@       " \
                   "                                  \n                        @@@@@@@@@@@@@@@                     " \
                   "                    \n                        @@@@@@@@@@@@@@@                                    " \
                   "     \n                        &@@@@@@(@@@@@@@                                         \n       " \
                   "                  @@@@@@ @@@@@@@                                         \n                     " \
                   "    @@@@@   @@@@@@                                         \n                         @@@@@   @@" \
                   "@@@@                                         \n                         @@@@@   &@@@@@          " \
                   "                               \n                        %@@@@,   @@@@@@                        " \
                   "                 \n                        (@@@@@   @@@@@*                                      " \
                   "   \n                         @@@@@   @@@@@                                          \n         " \
                   "                @@@@,  .@@@@                                           \n                       " \
                   "   @@@@  &@@@@@@                                         \n                                     " \
                   "                                           \n                                                   " \
                   "                             \n\nYou are dozing in and out during Math class...\n\nMr.Thompson: ." \
                   ".ahem..\nMr.Thompson: Ahem.\nMr.Thompson: !!AHEM!!\n\nYou jolt awake!\nYou open your eyes and see" \
                   " your math teacher, and everyone else in the class, staring at you!\n\nMr.Thompson: Aha! I assume" \
                   " you are so tired because you were up all last night studying!\nMr.Thompson: In that case, please" \
                   " tell me what the 96th number in the fibonacci sequence is!\nYou: Uhhmmm... is it... \n\nRRRRRIII" \
                   "IIINNNNGGGG!\n\nMr.Thompson: Hmm... It seems like you've been saved by the bell once again.\nMr.T" \
                   "hompson: None the matter! Report to Principal Filbert's office after school for 3 hours of detent" \
                   "ion!\n\nRats! That was totally bogus, man!\nYou head outside and meet up with your group of frien" \
                   "ds...\n\nBill: Hey man, that was so not cool of Mr.Thompson!\nTed: Yeah! I wish there was somethi" \
                   "ng we could do to get back at all of the lame teachers!\nBill: I've got it! Let's execute Operati" \
                   "on Swordfish! Everyone got their walkie-talkies?\nTed: Yeah! Let's do it, dude! I'll head to the " \
                   "Cafeteria and start a food-fight! My codename will be Hawk!\nBill: I'll go to the Teacher's Loung" \
                   "e and burn popcorn in their microwave! You can call me Bullseye over the radio!\nBilly: Dude, rem" \
                   "ember the plan? You've got to take on Principal Filbert!\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('builtins.input', side_effect=["1"])
    def test_intro_dialogue_return_is_none(self, mock_input):
        self.assertIsNone(intro_dialogue())
