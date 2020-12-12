# input = open("input", "r")

class Day4():
    def read_file(file_name):
        f = open(file_name, "r")
        lines = f.readlines()
        return lines

    def count_valid_passports(lines):
        """
        byr (Birth Year)
        iyr (Issue Year)
        eyr (Expiration Year)
        hgt (Height)
        hcl (Hair Color)
        ecl (Eye Color)
        pid (Passport ID)
        cid (Country ID)
        """
        valid_passport_count = 0
        required_item_count = 0

        for line in lines:
            # if the entire line is just a newline, then we finished processing a
            # passport so reset the counter and `continue` on to the next.
            if line == "\n":
                required_item_count = 0
                continue

            for key_value_pair in line.split():
                if key_value_pair.startswith("byr"):
                    required_item_count = required_item_count + 1
                elif key_value_pair.startswith("iyr"):
                    required_item_count = required_item_count + 1
                elif key_value_pair.startswith("eyr"):
                    required_item_count = required_item_count + 1
                elif key_value_pair.startswith("hgt"):
                    required_item_count = required_item_count + 1
                elif key_value_pair.startswith("hcl"):
                    required_item_count = required_item_count + 1
                elif key_value_pair.startswith("ecl"):
                    required_item_count = required_item_count + 1
                elif key_value_pair.startswith("pid"):
                    required_item_count = required_item_count + 1

                if required_item_count > 6:
                    valid_passport_count = valid_passport_count + 1

        return valid_passport_count
