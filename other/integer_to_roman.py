"""
Integer to Roman
===================
Convert Inteer numbers to Roman like 

Rules:
- Basic values: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
- Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Similarly: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900
"""

from printopia import print_return


@print_return
def int_to_roman_1(num):
    roman_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    roman = ""
    for value, symbol in roman_map:
        while num >= value:
            roman += symbol
            num -= value
    return roman


@print_return
def int_to_roman_2(num: int):
    roman_map = [
        (1000, "M"),
        (500, "D"),
        (100, "C"),
        (50, "L"),
        (10, "X"),
        (5, "V"),
        (1, "I"),
    ]
    replacements = [
        ("IIII", "IV"),
        ("VIV", "IX"),
        ("XXXX", "XL"),
        ("LXL", "XC"),
        ("CCCC", "CD"),
        ("DCD", "CM"),
    ]

    roman: str = ""
    for value, symbol in roman_map:
        count = num // value
        roman += symbol * count
        num %= value

    for old, new in replacements:
        roman = roman.replace(old, new)

    return roman


# Example Usage
int_to_roman_2(1994)  # MCMXCIV
int_to_roman_2(58)  # LVIII
int_to_roman_2(44)  # XLIV
