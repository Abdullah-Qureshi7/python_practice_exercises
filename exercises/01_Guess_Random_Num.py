# Question 01: We are going to write a program that generates a random number and asks the user to 
# guess it. 

# Explanation: If the player’s guess is higher than the actual number, the program displays “Lower 
# number please”. Similarly, if the user’s guess is too low, the program prints “higher 
# number please” When the user guesses the correct number, the program displays the 
# number of guesses the player used to arrive at the number. 
# Hint: Use the random module. 

import random

n = random.randint(1, 100)
guess = 0
a = -1

while(a != n):
    a = int(input("Guess the Number: "))
    guess +=1
    
    if( a> n):
        print("Lower number please")
    elif(a < n):
        print("Higher number please")
    print(f" Congratulations! You guessed the number {n} in {guess} Attempts")