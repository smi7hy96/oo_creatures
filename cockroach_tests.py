import unittest
from cockroach_class import *


class CockroachTest(unittest.TestCase):
    def setUp(self):
        self.cockroach = Cockroach(5, 'black', True, 'american')


if __name__ == '__main__':
    unittest.main()
