from unittest import TestCase

__author__ = 'oier'

import playsound


class TestPlaysound(TestCase):
    def test_playsound(self):
        playsound.playsound("./sounds/omen.wav")


