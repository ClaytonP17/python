import getpass

P1 = getpass.getpass("Player 1, pick rock, paper, or scissors: ")
P2 = getpass.getpass("Player 2, pick rock, paper, or scissors: ")

if P1 not in ['rock', 'paper', 'scissors'] or P2 not in ['rock', 'paper', 'scissors']:
    print("Invalid choice. Please run the game again and choose rock, paper, or scissors.")

if P1==P2 :
    print("It's a tie!")

if (P1 == 'rock' and P2 == 'scissors') or \
   (P1 == 'scissors' and P2 == 'paper') or \
   (P1 == 'paper' and P2 == 'rock') :
    print("Player 1 Wins!")

if (P2 == 'rock' and P1 == 'scissors') or \
   (P2 == 'scissors' and P1 == 'paper') or \
   (P2 == 'paper' and P1 == 'rock') :
    print("Player 2 Wins!")