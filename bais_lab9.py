#asking user for input
rows = int(input("Enter your number of rows: ")) 
#intializing variables
current_number = 1  
number = 1
#starting the loop
while number <= rows:
    j = 1
    while j <= number:
        print(current_number, end=" ")
        current_number += 1  # Increment the number after printing
        j += 1
    print()
    number += 1
