'''
1. Change the number (range from 1 to 1000000)
2. Game should ask us to guess a Number
3. Give a clue of the number (if it is higher ot lower)
4. Inform the player if he won
'''

from random import randint

start = 1
end = 1000
value = randint(start, end)

print("Choose a number between ", start, " and ", end)

guess = None

while guess != value:
    text = input("Guess the number: ")
    guess = int(text)
    
    if guess < value:
        print("The number is Higher")
    elif guess > value:
        print("The number is Lower")

print("Congratulations!!! You guessed the number. You Won!")
