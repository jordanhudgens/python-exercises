import unittest
import infinite_lineup as il

class InfiniteLineupTest(unittest.TestCase):
    def test_infinite_lineup_lineup(self):
        astros = [
          'Springer',
          'Bregman',
          'Altuve',
          'Correa',
          'Reddick',
          'Gonzalez',
          'McCann',
          'Davis',
          'Tucker'
        ]

        full_lineup = il.InfiniteLineup(astros)
        astros_lineup = full_lineup.lineup()
        self.assertEqual('Springer', next(astros_lineup))
        self.assertEqual('Bregman', next(astros_lineup))
        self.assertEqual('Altuve', next(astros_lineup))
        self.assertEqual('Correa', next(astros_lineup))
        self.assertEqual('Reddick', next(astros_lineup))
        self.assertEqual('Gonzalez', next(astros_lineup))
        self.assertEqual('McCann', next(astros_lineup))
        self.assertEqual('Davis', next(astros_lineup))
        self.assertEqual('Tucker', next(astros_lineup))
        self.assertEqual('Springer', next(astros_lineup))
        self.assertEqual('Bregman', next(astros_lineup))


if __name__ == '__main__':
    unittest.main()
