#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    roman = 'IVXLCDM'
    count = 0
    for i, num in enumerate(roman_string):
        if i != (len(roman_string) - 1):
            if (roman_string[i + 1] in roman[roman.index(num) + 1:] and
                    roman_string[i] != roman_string[i + 1]):
                count += roman_val[num] * -1
            else:
                count += roman_val[num]
        else:
            count += roman_val[num]
    return count
