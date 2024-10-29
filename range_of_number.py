# Initialize the quantity per range
range_1_10 = 0
range_11_20 = 0
range_21_30 = 0
range_31_40 = 0
range_41_50 = 0
# Loop to ask user for an input between 1 to 50
while True:
    try:     
        # Ask user for input
        number = int(input("Please input a number ranging 1-50: "))  
# Check if the input is out of range, error message and break the loop if out of range

# Set the condition for the range and update quantity of the inputted numbers in range

# Error message and break the loop if the input is not integer
    except ValueError:
        print("Invalid input")
        break
# Display the quantity of inputted numbers per range
