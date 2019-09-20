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
        othersize check if the number is a valid hex value
        then convert it to decimal. '''

    valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
             'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e',
             'E', 'f', 'F']
    output = []
    flag = True
    
    for num in nums:
        if num[:2:] == '0x':
            # Check the digits. If they're valid turn them into decimal
            for digit in num[2::]:
                if digit in valid:
                    flag = True
                else:
                    flag = False

            if flag:
                output.append(int(num, 16))
            else:
                output.append("Invalid number!")
        #else:
            # Do the conversion to hex
            

    return output
    

# Do the stuff
numbers = get_nums()
answers = calculate(numbers)
print(answers)
