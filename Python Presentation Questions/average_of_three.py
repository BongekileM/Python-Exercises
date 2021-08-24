# Python program to find average of three numbers.

# Creating function that takes in three numbers.
def average_of_three(num1, num2, num3):
    average = (num1 + num2 + num3)/3  # Formula for calculating average.
    return average


# Taking inputs.
num1 = int(input('Please enter first number: '))
num2 = int(input('Please enter second number: '))
num3 = int(input('Please enter third number: '))

# Function call.
average_of_numbers = average_of_three(num1, num2, num3)

print('The average is = ', average_of_numbers)
