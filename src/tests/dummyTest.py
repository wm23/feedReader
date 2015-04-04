__author__ = 'wojtek'

import unittest

class FooTests(unittest.TestCase):

    def testFoo(self):
        self.failUnless(True)

def main():
    unittest.main()

if __name__ == '__main__':
    main()