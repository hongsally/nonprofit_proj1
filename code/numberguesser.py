guess = int(input("Guess a number: "))
number = 21
if guess == number:
    print("You got it")
elif guess >= 22:
    print("Guess lower")
else:
    print("Guess higher")