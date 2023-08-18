#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_num = 0
    for n in range(len(roman_string)):
        if n > 0 and roman_digits[roman_string[n]] > roman_digits[roman_string[n - 1]]:
            roman_num += roman_digits[roman_string[n]] - 2 * \
                        roman_digits[roman_string[n - 1]]
        else:
            roman_num += roman_digits[roman_string[n]]
    return roman_num
