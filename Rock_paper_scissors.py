import random
my_computer = ['rock','paper','scissors']
print("***Rock Paper Scissors***")
i = int(input("Enter number of turns:  "))
j = 0
k = 0
while i>0:
        computer = random.choice(my_computer)
        player = input("Player turn... ").lower()
        print("computer selected " + computer)
        if computer == player:
                j = j + 0
                k = k + 0
        elif player == "rock":
                if computer == "scissors":
                        k += 1
                elif computer == "paper":
                        j += 1
        elif player == "paper":
                if computer == "rock":
                        k += 1
                elif computer == "scissors":
                        j += 1
        elif player == "scissors":
                if computer == "paper":
                        k += 1
                elif computer == "rock":
                        j += 1	
        else:
            print("Something went wrong...\n")
        i -= 1

print("Computer Score: " + str(j) + "\nPlayer Score: " + str(k))
if j<k:
        print("Player Wins!!")
elif j>k:
        print("Computer Wins!!")
else:
        print("It's a tie")



