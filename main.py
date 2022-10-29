# Create fun title
print(r"""
 __  __     ______     __   __     ______     __    __     ______     __   __    
/\ \_\ \   /\  __ \   /\ "-.\ \   /\  ___\   /\ "-./  \   /\  __ \   /\ "-.\ \   
\ \  __ \  \ \  __ \  \ \ \-.  \  \ \ \__ \  \ \ \-./\ \  \ \  __ \  \ \ \-.  \  
 \ \_\ \_\  \ \_\ \_\  \ \_\\"\_\  \ \_____\  \ \_\ \ \_\  \ \_\ \_\  \ \_\\"\_\ 
  \/_/\/_/   \/_/\/_/   \/_/ \/_/   \/_____/   \/_/  \/_/   \/_/\/_/   \/_/ \/_/ 
                                                                                 
""")
print()

# Give the user the game instructions
print("Welcome to the classic word game, Hangman!")


# Create the function to get the user to enter a letter
def getLetter():
  
  userLetter = ""

  # Force the user to enter only 1 letter
  while len(userLetter) != 1:
    
    userLetter = input("Enter a letter: ")

  # make the letter uppercase, if it is not
  return userLetter.upper()
  

# Create the function to display the secret word
def displaySecret(secret, guesses):
  
# For each letter in the secretWord
  for letter in secret:

   # if that letter is also one of their guesses 
   if letter in guesses:

    # Show them the letter in the correct place
    # If this letter (from the secret word) has been guessed, display the letter
    print(letter, end ="")
    
     
    # if the letter is not one of their guesses, then show a blank as a placeholder
   else: 
     print("_ ", end ="")

  

# Create a function to tell if the user has won or not
def checkGuess(answer, guesses):

  # set the default to True
  win = True
  
  # for each letter in the secret word
  for letter in answer:

    # If every letter in the secret word doesn't appear in the list of guesses
    if letter not in guesses :

      # the person did not win
      win = False
      
  return win

  
# Design a loop for the game:
  
# Create the variable for the secret word and blank list to hold all the user's guesses
secretWord = "AMPLIFIER"
userGuesses = []

# set the user's guess count, or 'strikes' to zero
count = 0

# while the strikes are less than 6, and the user has not guessed all the letters in the word...
while count < 6 and checkGuess(secretWord, userGuesses) != True:
  
  # Ask the user to enter a single letter
  userLetter = getLetter()
  print()
  
  # Add that letter to the userGuesses list
  userGuesses.append(userLetter) 

  # If they guessed all the letters in the secret word
  if checkGuess(secretWord, userGuesses) == True:

    # tell them they won
    print("You win")
    
  # if their letter guess is in the secret word 
  if userLetter in secretWord:
    
    # tell them good guess
    print("Good guess!")
    
    # then show them where their letter is in the secret word
    displaySecret(secretWord, userGuesses)
    print()
  
    # if their letter in not in the secret word
  else: 

    # Add a strike
    count += 1

    # Tell them their letter is not in the secret word
    print(f"{userLetter} is not in the word")

    # show them the number of strikes they have
    print(f"You guessed wrong, you have {count} out of 6 strikes")

    # when they guess wrong 6 times
    if count == 6:

      # tell them they lost
      print("Sorry, you lose!")
    print()

  