import unittest
from day4 import Day4



class TestDay4(unittest.TestCase):
    def test_read_file(self):
        """
        test first line of file matches what we expect
        """
        input = Day4.read_file("input")

        self.assertEqual("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n", input[0])

    def test_has_two_valid_passports(self):

        """
        testing to see if there are 2 valid passports in the data

        byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
        :return:
        """
        lines = Day4.read_file("input")
        count = Day4.count_valid_passports(lines)

        self.assertEqual(2, count)

if __name__ == '__main__':
    unittest.main()