import unittest
from phonelist import generate_phone_numbers

class TestPhoneList(unittest.TestCase):
    def test_phone_numbers_length(self):
        phones = generate_phone_numbers(10000)
        self.assertEqual(len(phones), 10000)

    def test_phone_number_length(self):
        phones = generate_phone_numbers(1)
        self.assertEqual(len(phones[0]), 10)

    def test_phone_number_digits(self):
        phones = generate_phone_numbers(1)
        self.assertTrue(phones[0].isdigit())
        
    def test_phone_number_unique(self):
        phones = generate_phone_numbers(10000)
        self.assertEqual(len(phones), len(set(phones)))

    def test_phone_number_range(self):
        phones = generate_phone_numbers(1)
        for digit in phones[0]:
            self.assertTrue(0 <= int(digit) <= 9)

if __name__ == '__main__':
    unittest.main()