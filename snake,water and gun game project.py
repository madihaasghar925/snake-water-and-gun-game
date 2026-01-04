# We all have played snake, water gun game in our childhood. If you haven’t, google the
# rules of this game and write a python program capable of playing this game with the user.
import random
choice=input("Enter your choice \"S\" for snake , \"W \"for water and \"G\"for Gun : ")
options=["S","G","W"]
c_choice= random.choice(options)
if(choice not in options):
    print("enter valid option and try again")

else:
    if(choice=="S" and c_choice=="W"):
     print(f"You Won Becz you choosed {choice} and other player choosed {c_choice} ")

    elif(choice=="W" and c_choice=="G"):
      print(f"You Won Becz you choosed {choice} and other player choosed {c_choice} ")

    elif(choice=="G" and c_choice=="S"):
     print(f"You Won Becz you choosed {choice} and other player choosed {c_choice} ")
    elif(choice==c_choice):
     print(f"Game is draw becz you chosed {choice} and other player also choosed {c_choice} ")    
    else:
        print(f"you lost becz you chosed {choice} and other player chosed {c_choice}")
    print(f"computer chosed {c_choice} for you")

    






