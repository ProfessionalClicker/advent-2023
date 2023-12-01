# On each line, the calibration value can be found by combining the first digit 
# and the last digit (in that order) to form a single two-digit number

# What is the sum of all of the calibration values?

# spelled out numbers:
# one, two, three, four, five, six, seven, eight, and nine also count as valid "digits"

import re

def main():
    calibration_values = []
    number_dictionary ={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    first_alt_dict ={'oneight':'1','twone':'2','threeight':'3','fiveight':'5','sevenine':'7','eightwo':'8','nineight':'9'}
    last_alt_dict ={'oneight':'8','twone':'1','threeight':'8','fiveight':'8','sevenine':'9','eightwo':'2','nineight':'8'}
    # oneight, twone, threeight, fiveight, sevenine, eightwo, eighthree, nineight
    with open('1/input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            pattern = r'oneight|twone|threeight|fiveight|sevenine|eightwo|eighthree|nineight|\d|one|two|three|four|five|six|seven|eight|nine'
            matches = re.findall(pattern, line)
            print(line)
            print(matches)
            print()
            # get the first and last digits/words as strings
            first_digit = matches[0]
            last_digit = matches[len(matches) - 1]

            # convert any words to digits
            for number in number_dictionary:
                if first_digit == number:
                    first_digit = number_dictionary[number]
                if last_digit == number:
                    last_digit = number_dictionary[number]

            # check first number against first alt dict
            for number in first_alt_dict:
                if first_digit == number:
                    first_digit = first_alt_dict[number]
            # check last number against last alt dict
            for number in last_alt_dict:
                if last_digit == number:
                    last_digit = last_alt_dict[number]

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

# this might be simplified if using pattern matching with overlapping
# re doesn't support overlapping, but 3rd part regex module does
    # import regex as re
    # matches = re.findall(pattern, line, overlapped=True)
# this post shows how you can use lookaheads and capture groups to do something similar https://stackoverflow.com/questions/5616822/how-to-use-regex-to-find-all-overlapping-matches