# --------------------------------------------------
# Challenge 4 - Dog Years
# --------------------------------------------------

# Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named dog_years() that has two parameters named name and age.

# The function should compute the age in dog years and return the following string:

# "{name}, you are {age} years old in dog years"
# Test this function with your name and your age!

# Write your dog_years function here:

# Uncomment these function calls to test your dog_years function:
#print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
#print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"
def dog_years(name,age):
    return f"{name} you are {age*7} years in dog years"
    age = age * 7

def main():
    dogs_name = input("Enter your dog's name: ")
    dogs_age = int(Input("Enter your dogs age: "))
    print(dog_years(dogs_name, dogs_age))
main()