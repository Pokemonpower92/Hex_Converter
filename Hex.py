#!/usr/bin/env python
# This program takes any number of decimal or hexidecimal numbers
# and converts them to the opposite

import sys

def get_nums():
    ''' This function returns a list of numbers to convert. '''
    lst = []
    if len(sys.argv) < 2:
        return lst
    else:
        # Check that the arguments are valid
        # Either the first two characters must be
        # numbers, or '0x'
        lst = []
        
        for arg in sys.argv[1:]:
        # We need to verify that the hex value is valid,
        # but it's better to do that while we calculate
        # the decimal value of it.
            if arg[:2] == '0x' or arg.isdigit():
                lst.append(arg)

        return lst     

def calculate(nums):
    ''' If the number is a decimal number convert it to hex,
        otherwise check if the number is a valid hex value
        then convert it to decimal. '''

    valid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e',
             'E', 'f', 'F']

    output = []
    
    for num in nums:
        flag = True
        if num[:2:] == '0x':
            # Check the digits. If they're valid turn them into decimal
            for digit in num[2::]:
                if digit in valid:
                    x = True
                else:
                    flag = False

            if flag:
                output.append(int(num, 16))
            else:
                output.append("Invalid number!")
        else:
            # If the string is an int, convert it,
            # otherwise report as invalid.
            try:
                output.append(hex(int(num)))
            except ValueError:
                output.append("Invalid number!")
            

    return output

def print_ans(nums, answers):
    for i in range(len(nums)):
        print(nums[i], "converts to:", answers[i])

# Do the stuff
numbers = get_nums()
answers = calculate(numbers)
print_ans(numbers, answers)
