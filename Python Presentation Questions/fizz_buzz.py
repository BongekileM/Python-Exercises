# Python program that takes in a number max, and returns an array containing all numbers divisible by either 4 or 6, but not both.

# Taking input.
max = int(input("Please enter a number: "))


def fizz_buzz(max):  # Creating a function that takes in a number max.
    result = []  # Creating empty array.
    for i in range(1, max):  # Numbers greater than 0 and less than max.
        # Numbers divisible by either 4 or 6, but not both.
        if (i % 4 == 0 or i % 6 == 0) and (i % 4 != i % 6):
            result.append(i)  # Appending the values of i to empty array.
    return result


# Funcion call.

arr = fizz_buzz(max)
print(arr)
