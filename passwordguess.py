from random import choice
import time  
password = input("Password: ")
guess = [""] * len(password)  

characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


while "".join(guess) != password:
    
    for i in range(len(password)):
        if guess[i] != password[i]:  
            guess[i] = choice(characters)
    
    print("".join(guess), end="\r")
    time.sleep(0.05)  

print("\nPassword guessed successfully!")
input("Press Enter to exit...")