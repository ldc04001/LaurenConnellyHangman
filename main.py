# Create fun title

# Give the user the game instructions

# Create the variable for the secret word and blank variable for the user's word
secretWord = "AMPLIFIER"
userWord = []
count = 0


# Create the function to get the user to enter a letter
def getLetter(userGuess):
  userLetter = ""
  
  while len(userLetter) != 1:
    
    userLetter = input("Enter a letter: ")
    
  return userLetter.upper()
  

# Create the function to display the secret word
def displaySecret():
  
# Go through each letter in the secret word, and determine HOW we display it
  for letter in secretWord:
  
   if letter == userLetter:
   
  # If this letter (from the secret word) has been guessed, display the letter
     print("userLetter", end ="")
   
    # Otherwise, display an underscore ( _ )
  else: 
    print("_", end ="")
  
  
# Create a function to tell if the user has won or not
def checkGuess(letter, isLetterInWord = True):
 # Go through each letter in the secret word
  for letter in secretWord:
    if letter == userLetter and

    
    if count < 6:
      print("You have won!")
  else:
    print("You lose")

  
# Design a loop for the game
while count < 6 and userWord != secretWord:
  userLetter = getLetter("")
  
  
  # Create a condition that stops the loop when the user has one or they've guessed 5 letters wrong

