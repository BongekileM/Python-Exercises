# Python program that doubles numbers in an array.

def double(arr):
    return [i*2 for i in arr]


arr = [3, 5, 7, 10, 50, 200]

# Function call.

newArr = (double(arr))

# Displaying original array.

print('Original array: ' + str(arr))

# Displaying new array.
print('Doubled array: ' + str(newArr))
