# This program takes any number of decimal or hexidecimal numbers
# and converts them to the opposite

import sys

def get_nums() -> List[str]:
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
            if arg[:2] == '0x' or arg[:2].isdigit():
                lst.append(arg)

        return lst     

def calculate(nums: List[str]) -> List[str]:



def print_ans(nums: List[str], ans: List[str]):
    
