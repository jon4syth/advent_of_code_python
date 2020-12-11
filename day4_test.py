import unittest
from day4 import Day4

class TestDay4(unittest.TestCase):
    def test_read_file(self):
        """
        test first line of file matches what we expect
        """
        input = Day4.read_file("input")

        self.assertEqual("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n", input[0])


if __name__ == '__main__':
    unittest.main()