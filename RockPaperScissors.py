import random

gameRunning = True

# create some scores
computerScore = 0
userScore = 0

while gameRunning == True:
  # we need a choice of rock, paper or scissors from the user 
  userChoice = input("Welcome to my game of rock, paper, scissors!! Please choose an option: ")
  print("You chose: "+ userChoice)

  userChoice = userChoice.lower()

  # we need a choice of rock, paper or scissors from the computer
  options = ["rock", "paper", "scissors"]
  computerChoice = random.choice(options)
  print("Computer chose: " + computerChoice)

  # compare choices to see who wins
  if userChoice == computerChoice:
    print("It's a draw!!!")

  elif userChoice == "rock" and computerChoice == "scissors":
    print("Rock beats scissors!!! You win!!")
    userScore += 1

  elif userChoice == "rock" and computerChoice == "paper":
    print("Paper beats rock!!! Computer wins!!!")
    computerScore += 1

  elif userChoice == "scissors" and computerChoice == "paper":
    print("Scissors beats paper!!! You win!!")
    userScore += 1

  elif userChoice == "scissors" and computerChoice == "rock":
    print("Rock beats scissors!!! Computer wins!!!")
    computerScore += 1

  elif userChoice == "paper" and computerChoice == "scissors":
    print("Scissors beats paper!!! Computer wins!!")
    computerScore += 1

  elif userChoice == "paper" and computerChoice == "rock":
    print("Paper beats rock!!! You win!!!")
    userScore += 1


  print("The score is: Computer ", computerScore, "-", userScore, " User")


  quitting = input("Do you want to continue, yes or no? ")
  quitting = quitting.lower()

  if quitting == "no":
    gameRunning = False

print("Thank you for playing my game of rock, paper scissors!!!!")