import random

# to generate random numbers between 1 and 100
randNumber = random.randint(1,100)

# keep guesses at zero so as the loop will run each rime it will raise by 1 and set you as None to define you variable
you = None
guesses = 0

#create the rules and format of the game using the while loop
while(randNumber != you):
    you = int(input("enter your guess:\n"))
    if randNumber == you: 
        print("your guess is correct!")

    else:
        print("your guess is wrong")
        if you<randNumber:
            print("the number is bigger than your guess")
        else :
            print("the number is less than your guess")
    guesses += 1

#print the result of the number of guesses of the player
print(f"You guessed the number in {guesses} guesses")

#with open("hiscore.txt",'r') as f:
 #   hiscore  = int(f.read())

#if(guesses<hiscore):
 #   print("Congratulations! You have just broken the high score.")
  #  with open("hiscore.txt",'w') as f:
   #     f.write(str(guesses))