# import the random module
import random

# defined function to set the rules of the game
def gamewin(comp, you) :
    if comp == you:
     # if both computer and you select the same 
        return None

# if the computer chooses 'R' 
    elif comp == 'R':
        if you == 'P':
            return True
        elif you == 'S':
            return False

# if the computer chooses 'p'
    elif comp == 'P':
        if you == 'S' :
            return True
        elif you == 'R':
            return False

# if the comcputer chooses 's'
    elif comp == 'S':
        if you == 'R':
            return True  
        elif you == 'P':
            return False

print(f"computer's turn : Rock(R) Paper(P) or Scissors(S):")

# the random.radiant command gives random values between (1,3)
randm = random.randint(1,3)

if randm == 1:
    comp = 'R'
elif randm == 2:
    comp = 'P'
elif randm == 3:
    comp = 'S'

# for user to enter their choice
you = input("Your turn: Rock(R) Paper(P) or Scissor(S):\n")

print(f"computer chose {comp}")
print(f"you chose {you}")

# give the function a variable a just for simpllification
a = gamewin(comp, you)

# if comp  ==  you then its tie
if a == None:
    print("The Game is Tie!")
    # if a is true then you win!
elif a :
    print("You Win!")
    # if a is false then you loose!
else :
    print("You Loose!")