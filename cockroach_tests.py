import unittest
from cockroach_class import *


class CockroachTest(unittest.TestCase):
    def setUp(self):
        self.cockroach = Cockroach(5, 'black', True, 'american', 'Alive')

    def test_fly(self):
        self.assertEqual(self.cockroach.fly(), 'RUN AWAY FROM IT!')
        self.cockroach.size = 1
        self.assertEqual(self.cockroach.fly(), 'SOMEONE SWAT IT!')

    def test_squish(self):
        self.assertEqual(self.cockroach.squish(0), "how did it not die")
        self.cockroach.size = 1
        self.assertEqual(self.cockroach.squish(0), "quick little bugger")
        self.assertEqual(self.cockroach.squish(1), 'WE GOT IT')

    def test_jump(self):
        self.assertEqual(self.cockroach.jump(1), '*boing*')
        self.assertEqual(self.cockroach.jump(3), '*boing* *boing* *boing*')

    def test_reproduce(self):
        assert isinstance(self.cockroach.reproduce(), Cockroach)


if __name__ == '__main__':
    unittest.main()
