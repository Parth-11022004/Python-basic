import random
rock = """
    _______
---'   ____ )
      (_____)
      (_____)
      (____)
---.__(___)

"""
paper = """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

choice = int(input("choose: rock paper or scissors\n rock: 1\n paper: 2\n scissors: 3"))

if choice == 1:
    print(rock)
elif choice == 2:
    print(paper)  
elif choice == 3:
    print(scissors)    
else:
    print("enter valid choice")        

choice1 = random.randint(1,3)
if choice1 == 1:
    print(rock)
elif choice1 == 2:
    print(paper)  
else:
    print(scissors)

if (choice == 1 and choice1 == 3) or (choice == 2 and choice1 == 1) or (choice == 3 and choice1 == 2):
    print("You win!!")
elif choice == choice1:
    print("Its a draw!")
else:
    print("You lose!")    



