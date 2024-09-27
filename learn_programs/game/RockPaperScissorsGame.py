import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors = [rock, paper, scissors]

user_input = int(input("Enter your choice 0, 1 or 2 \n"))
if user_input <= int(len(rock_paper_scissors)):
    user_choice = rock_paper_scissors[user_input]
    print(f"User input :: {user_choice}")

    system_choice = random.choice(rock_paper_scissors)
    print(f"System choice :: {system_choice}")

    if user_choice == system_choice:
        print("Match is tied.")
    elif user_choice == rock and system_choice == scissors:
        print("user wins [rock wins against scissors]")
    elif user_choice == scissors and system_choice == paper:
        print("user wins [scissors wins against paper]")
    elif user_choice == paper and system_choice == rock:
        print("user wins [paper wins against rock]")
    else:
        print(f"system wins {user_choice} against {system_choice}")
else:
    print("Invalid input")
