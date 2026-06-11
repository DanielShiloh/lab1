"""
UPC Validator
Daniel Shiloh
Validate UPC-A code
June 10, 2026
"""

def find_check_digit(upc):
    
    sum = 0

    #sum odd positions

    #odd sum x 3

    #add even positions

    #result modulo 10 = M

    #check digit is 0 or 10-M

    #return check digit

#ask user for upc
input_UPC: str = input("Enter UPC: ")

#validate that input is 12 char, only numbers
    #if invalid, print error and ask again

#use fxn to calculate correct check digit
find_check_digit(input_UPC[:-1])
    #compare returned check digit to actual 12th digit

#inform user if full upc is valid or invalid