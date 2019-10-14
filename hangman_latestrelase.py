import random
import sys

print("\n"*2) 
print("88")                                        
print("88")
print("88")
print("88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,")
print("88P\'    \"8a \"\"     `Y8 88P\'   `\"8a a8\"    `Y88 88P\'   \"88\"    \"8a \"\"     `Y8 88P\'   `\"8a")
print("88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 88       88")
print("88       88 88,    ,88 88       88 \"8a,   ,d88 88      88      88 88,    ,88 88       88")
print("88       88 `\"8bbdP\"Y8 88       88  `\"YbbdP\"Y8 88      88      88 `\"8bbdP\"Y8 88       88")
print("                                    aa,    ,88                              ")
print("                                     \"Y8bbdP\"                               ") 
print("\n")                   

# lets set some variables

wordList = []
with open("words.txt") as f:
    wordList = f.read().splitlines()
    
HANGMANPICS = ['''
        |
        |
        |
        |
________|_''', '''
      ===
        |
        |
        |
        |
________|_''', '''
    =====
        |
        |
        |
        |
________|_''', '''
   |=====
        |
        |
        |
        |
________|_''', '''
   |=====
   O    |
        |
        |
        |
________|_''', '''
   |=====
   O    |
   |    |
        |
        |
________|_''', '''
   |=====
   O    |
  /|    |
        |
        |
________|_''', '''
   |=====
   O    |
  /|\   |
        |
        |
________|_''', '''
   |=====
   O    |
  /|\   |
  /     |
        |
________|_''', '''
   |=====
   O    |
  /|\   |
  / \   |
        |
________|_''']


guess_word = []

secretWord = random.choice(wordList) # randomize a single word from the list
 
length_word = len(secretWord)

alphabet = "abcdefghijklmnopqrstuvwxyz"
 
letter_storage=[]


def change():
    guess_word.clear()
    letter_storage.clear()
    for character in secretWord: # printing blanks for each letter in secret word
        guess_word.append("-")

    print("Welcome! The word You need to guess has", length_word, "characters\n")

    print(" ".join(guess_word))


def guessing(word):
        
    guess_taken = 1
    lives = len(word) + 1 #UPGRADE new variable
    
    while guess_taken < 10 and lives > 0:

        guess = input("\nPick a letter\n").lower()

        if not guess in alphabet: #checking input
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage: #checking if letter has been already used
            print("You have already guessed that letter!")
            print(" ".join(guess_word))  #UPGRADE
        else: 

            letter_storage.append(guess)
            if guess in word:
                print("You guessed correctly!\n")
                print("You have", lives, "chances left.")
                for x in range(0, length_word): #
                    if word[x] == guess:
                        guess_word[x] = guess
                        print(" ".join(guess_word)) #
                
                if not '-' in guess_word:
                    print("You won!")
                    break
            else:
                lives = lives - 1
                print("The letter is not in the word. Try Again!")
                print("You have", lives, "chances left.") ###
                print(" ".join(guess_word))
                print("\n")
                print(HANGMANPICS[guess_taken-1])  #UPGRADE 
                guess_taken += 1
                if lives == 0:
                    print("Sorry Mate, You lost :<! The secret word was",         word)
                    print(HANGMANPICS[-1])
                

    print("Game Over!" ) 
    x = input("Do you want to play again? y or n?\n") #UPGRADE
    if x == "y":
        return True

    else:
        print("Thank you for playing!")
        return False

change()  #UPGRADE
while(guessing(secretWord) == True):
    secretWord = random.choice(wordList) # lets randomize single word from the list
    length_word = len(secretWord)
    change()
