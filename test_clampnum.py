import unittest

from clampnum import clamp, clamp_all, outside_count, overflow, spread, within


class ClampnumTest(unittest.TestCase):
    def test_inside_and_edges(self) -> None:
        self.assertEqual(clamp(5, 0, 10), 5)
        self.assertEqual(clamp(-1, 0, 10), 0)
        self.assertEqual(clamp(11, 0, 10), 10)
        self.assertTrue(within(5, 0, 10))
        self.assertFalse(within(11, 0, 10))
        self.assertEqual(overflow(11, 0, 10), 1)
        self.assertEqual(overflow(5, 0, 10), 0)
        with self.assertRaises(ValueError):
            clamp(1, 3, 2)
        self.assertEqual(clamp_all([-1, 5, 11], 0, 10), [0, 5, 10])
        self.assertEqual(outside_count([-1, 5, 11], 0, 10), 2)
        self.assertEqual(spread(0, 10), 10)


if __name__ == "__main__":
    unittest.main()
