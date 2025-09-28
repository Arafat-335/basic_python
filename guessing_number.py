import random 

n = random.randrange(1,10) 

guess = int(input("Enter any number: ")) 

while n!= guess: 

    if guess < n: 

        print("your number is wrong, plz try agin") 

        guess = int(input("Enter number again: ")) 

    elif guess > n: 

        print("your number is wrong, plz try agin") 

        guess = int(input("Enter number again: ")) 

    else: 

      break 

print("you guessed it right!!") 

 