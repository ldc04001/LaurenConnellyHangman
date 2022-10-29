# Create fun title

# Give the user the game instructions

# Create the variable for the secret word and blank variable for the user's word
secretWord = "AMPLIFIER"
userGuesses = []
count = 0


# Create the function to get the user to enter a letter
def getLetter():
  userLetter = ""
  
  while len(userLetter) != 1:
    
    userLetter = input("Enter a letter: ")
    
  return userLetter.upper()
  

# Create the function to display the secret word
def displaySecret(secret, guesses):
  
# Go through each letter in the secret word, and determine HOW we display it
  for letter in secret:
    
   if letter in guesses:
           
    # If this letter (from the secret word) has been guessed, display the letter
    print(letter, end ="")
    
     
    # Otherwise, display an underscore ( _ )
   else: 
     print("_ ", end ="")

  

# Create a function to tell if the user has won or not
def checkGuess(answer, guesses):

  win = True
  
  # Go through each letter in the secret word
  for letter in answer:
    
    if letter not in guesses :
      
      win = False
      
  return win

  
# Design a loop for the game

while count < 6 and checkGuess(secretWord, userGuesses) != True:
  userLetter = getLetter()
  print()
  userGuesses.append(userLetter) 
  if checkGuess(secretWord, userGuesses) == True:
    print("you win")
  if userLetter in secretWord:
    print("good guess")
    displaySecret(secretWord, userGuesses)
    print()
    
  else: 
    
    count += 1
    print(f"{userLetter} is not in the word")
    print(f"you guessed wrong, you have {count} out of 6 strikes")
    if count == 6:
      print("you lose")
    print()

    
  
  
  
  
  # Create a condition that stops the loop when the user has won or they've guessed 6 letters wrong

