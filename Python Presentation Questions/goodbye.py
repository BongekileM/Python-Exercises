# Python program that says goodbye to a user.

# Taking input.

name = input("Please enter your name: ")


# Creating function that takes in a name.

def goodbye(name):
    return "Goodbye, " + name + "."


# Function call.

goodbye_user = goodbye(name)
print(goodbye_user)
