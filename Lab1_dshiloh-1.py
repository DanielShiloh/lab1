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



input_UPC: str = ""

while True:
    
    input_UPC = input("\nEnter a 12-digit UPC: ")

    if len(input_UPC) != 12:
        print("UPC must be 12 characters long.")
        continue
    
    if not input_UPC.isdigit():
        print("UPC may only contain numbers.")
        continue
    
    break

returned_check = find_check_digit(input_UPC)
given_check = int(input_UPC[-1])

print(f"\nThe first 11 digits are '{input_UPC[:-1]}'.")
print(f"The provided check digit is '{given_check}'.")
print("\nCalculating...")
print(f"The expected check digit is {returned_check}.")

if returned_check == given_check:
    print("\nThis is a VALID UPC.")
else:
    print("\nThis is an INVALID UPC.\n")