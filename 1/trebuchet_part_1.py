# On each line, the calibration value can be found by combining the first digit 
# and the last digit (in that order) to form a single two-digit number

# What is the sum of all of the calibration values?

import re

def main():
    calibration_values = []
    with open('input.txt', 'r') as file:
        for line in file:
            pattern = r'\d'
            matches = re.findall(pattern, line)
            # get the first and last digits as strings
            first_digit = matches[0]
            last_digit = matches[len(matches) - 1]
            # concatenate them
            value = first_digit + last_digit
            # convert to integer, add to list
            calibration_values.append(int(value))
    # add all values in the list
    sum = 0
    for value in calibration_values:
        sum += value
    print(f"Sum of calibration values: {sum}")
if __name__ == "__main__":
    main()