__author__ = 'wojtek'

from feedreader.lib.dummy import dummy
import unittest

class FooTests(unittest.TestCase):
        def testFoo(self):
            self.assertEqual(dummy(),"CCCCC");
