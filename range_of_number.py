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
        if number < 1 or number > 50:
            print("Integer is out of range")
            break
        # Set the condition for the range and update quantity of the inputted numbers in range
        if 1 <= number <= 10:
            range_1_10 += 1
        elif 11 <= number <= 20:
            range_11_20 += 1
        elif 21 <= number <= 30:
            range_21_30 += 1
        elif 31 <= number <= 40:
            range_31_40 += 1            
    # Error message and break the loop if the input is not integer
    except ValueError:
        print("Invalid input")
        break
# Display the quantity of inputted numbers per range
print("Range 1-10:", range_1_10)
print("Range 11-20:", range_11_20)
print("Range 21-30:", range_21_30)
print("Range 31-40:", range_31_40)
