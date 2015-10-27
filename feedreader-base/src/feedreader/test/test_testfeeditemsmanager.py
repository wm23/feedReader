__author__ = 'wojtek'

import unittest
from feedreader.lib.logic.testfeeditemsmanager import TestFeedItemsManager

class TestFeedItemsManagerTests(unittest.TestCase):
        def testGetItems(self):
            self.assertEqual(len(TestFeedItemsManager.getItems("AAA", "AAA")), 15)

