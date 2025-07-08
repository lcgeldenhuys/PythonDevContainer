
def count_leap_years(year1, year2):
    """
    This function calculates the number of leap years between two given years.

    A year is a leap year if it is divisible by 4 and not divisible by 100,
    or it is divisible by 400.

    Args:
        year1 (int): The start year. This should be a non-negative integer representing 
        the start year. The function does not check for validity of input year.
        
        year2 (int): The end year. This should be a non-negative integer representing the 
        end year and it should be greater than or equal to the start year. 
        The function does not check for validity of input year.

    Returns:
        int: The number of leap years between year1 and year2, inclusive. 

    Examples:
        >>> count_leap_years(2000, 2020)
        6
        >>> count_leap_years(1900, 2000)
        25

    Edge Cases:
        - The function does not check if the years are valid (e.g., positive integers).
        - The function does not check if year2 >= year1. If year2 < year1, it will return 0.
        - The function correctly handles years that are divisible by 100 but not by 400
        (these are not leap years).
        - The function correctly handles years that are divisible by 400 (these are leap years).
    """

    # initialize counter for leap years
    leap_years = 0

    # iterate over each year in the range
    for year in range(year1, year2 + 1):
        # check if the year is a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1 

    return leap_years


import unittest

class TestCountLeapYears(unittest.TestCase):

    def test_basic_functionality(self):
        self.assertEqual(count_leap_years(2000, 2020), 6)
        self.assertEqual(count_leap_years(1900, 2000), 25)

    def test_edge_cases(self):
        # Test for years divisible by 100 but not 400
        self.assertEqual(count_leap_years(1700, 1700), 0)
        # Test for years divisible by 400
        self.assertEqual(count_leap_years(2000, 2000), 1)
        # Test when year2 < year1
        self.assertEqual(count_leap_years(2020, 2000), 0)        

    def test_error_cases(self):
        # Test with negative years
        self.assertEqual(count_leap_years(-400, 200), 147)
        # Test with start and end year being the same, and not a leap year
        self.assertEqual(count_leap_years(1900, 1900), 0)
        # Test with start and end year being the same, and a leap year
        self.assertEqual(count_leap_years(2000, 2000), 1)

    def test_various_input_scenarios(self):
        self.assertEqual(count_leap_years(0, 2000), 489)
        self.assertEqual(count_leap_years(123, 456), 82)
        self.assertEqual(count_leap_years(789, 101112), 24379)

if __name__ == '__main__':
    unittest.main()