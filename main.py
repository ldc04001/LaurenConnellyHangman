# Create fun title

# Give the user the game instructions

# Create the variable for the secret word and blank variable for the user's word
secretWord = "AMPLIFIER"
userWord = ""
count = 0


# Create the function to get the user to enter a letter
def getLetter():
  userLetter = ""
  if len(userLetter) > 1 or len(userLetter) > 1:
    
    userLetter = input("Enter a letter: ")
    
    return userLetter.upper()
  

# Create the function to display the secret word
def diplaySecret(guess, actual):
  
  if userLetter in secretWord:
    
    print()

  
# Create a function to tell if the user has won or not
def checkGuess():
  if userWord == secretWord:
    if count < 6:
      print("You have won!")
  else:
    print("You lose")

  
# Design a loop for the game
while count < 6 and userWord != secretWord:
  userLetter = getLetter("")
  
  # Create a condition that stops the loop when the user has one or they've guessed 5 letters wrong

