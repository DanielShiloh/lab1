"""
UPC Validator
Daniel Shiloh
Validate UPC-A code
June 10, 2026
"""

def find_check_digit(upc):
    
    sum = 0

    for position in range(11):
        if (position+1) % 2 == 0:
            sum += int(upc[position])
        else:
            sum += int(upc[position]) * 3

    sum = sum % 10 - 10

    return abs(sum)



#ask user for upc
input_UPC: str = input("Enter UPC: ")

#validate that input is 12 char, only numbers
    #if invalid, print error and ask again

#use fxn to calculate correct check digit
print(find_check_digit(input_UPC[:-1]))
    #compare returned check digit to actual 12th digit

#inform user if full upc is valid or invalid