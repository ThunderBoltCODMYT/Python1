class RomanConverter:
    roman_map = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }

    def int_to_roman(self, num):
        if not (0 < num < 4000):
            raise ValueError("Number must be between 1 and 3999")
        result = ''
        for value in sorted(self.roman_map.keys(), reverse=True):
            while num >= value:
                result += self.roman_map[value]
                num -= value
        return result


# 🚀 Run the conversion
if __name__ == "__main__":
    try:
        user_input = int(input("Enter an integer between 1 and 3999: "))
        converter = RomanConverter()
        roman_numeral = converter.int_to_roman(user_input)
        print(f"Roman numeral: {roman_numeral}")
    except ValueError as ve:
        print(f"Error: {ve}")