def number_to_words(number):
    if not isinstance(number, int) or number < 0:
        return "Please enter a non-negative integer."
    
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", 
            "sixty", "seventy", "eighty", "ninety"]
    
    if number == 0:
        return "zero"
    elif number < 10:
        return units[number]
    elif 10 <= number < 20:
        return teens[number - 10]
    elif 20 <= number < 100:
        tens_part = number // 10
        units_part = number % 10
        if units_part == 0:
            return tens[tens_part]
        else:
            return tens[tens_part] + "-" + units[units_part]
    elif 100 <= number < 1000:
        hundreds_part = number // 100
        remainder = number % 100
        hundreds_text = units[hundreds_part] + " hundred"
        if remainder == 0:
            return hundreds_text
        else:
            return hundreds_text + " and " + number_to_words(remainder)
    elif 1000 <= number < 1_000_000:
        thousands_part = number // 1000
        remainder = number % 1000
        thousands_text = number_to_words(thousands_part) + " thousand"
        if remainder == 0:
            return thousands_text
        else:
            connector = " " if remainder < 100 else " and "
            return thousands_text + connector + number_to_words(remainder)
    else:
        return "Number too large (max: 999,999)"

# User input
try:
    num = int(input("Enter a number (0-999,999): "))
    print(number_to_words(num))
except ValueError:
    print("Please enter a valid integer.")
