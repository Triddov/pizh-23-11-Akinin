import unittest
from task1_roman_nums import Roman


class TestRoman(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(Roman("X").value, 10)
        self.assertEqual(Roman(10).roman, "X")
        self.assertEqual(Roman("IX").value, 9)
        self.assertEqual(Roman(9).roman, "IX")

    def test_addition(self):
        self.assertEqual(str(Roman("X") + Roman("V")), "XV")

    def test_subtraction(self):
        self.assertEqual(str(Roman("X") - Roman("I")), "IX")
        with self.assertRaises(ValueError):
            Roman("I") - Roman("X")

    def test_multiplication(self):
        self.assertEqual(str(Roman("X") * Roman("II")), "XX")

    def test_division(self):
        self.assertEqual(str(Roman("X") / Roman("II")), "V")
        with self.assertRaises(ValueError):
            Roman("I") / Roman("X")


if __name__ == "__main__":
    unittest.main()
