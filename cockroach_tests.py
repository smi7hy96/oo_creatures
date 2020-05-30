import unittest
from cockroach_class import *


class CockroachTest(unittest.TestCase):
    def setUp(self):
        self.cockroach = Cockroach(5, 'black', True, 'american', 'alive')

    def test_fly(self):
        self.assertEqual(self.cockroach.fly(), 'RUN AWAY FROM IT!')
        self.cockroach.size = 1
        self.assertEqual(self.cockroach.fly(), 'SOMEONE SWAT IT!')

    def test_squish(self):
        self.assertEqual(self.cockroach.squish(0), "how did it not die")
        self.cockroach.size = 1
        self.assertEqual(self.cockroach.squish(0), "quick little bugger")
        self.assertEqual(self.cockroach.squish(1), 'WE GOT IT')

if __name__ == '__main__':
    unittest.main()
