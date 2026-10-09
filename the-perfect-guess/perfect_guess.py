import random

n_1= random.randint(0,100)
n_2= random.randint(0,100)

user_1=input("enter your name-> ")
user_2=input("enter your friend name-> ")

print(f"{user_1}'s turn: ")
guess_user_1=1
a_user_1=-1

while (a_user_1!=n_1) :
    a_user_1=int(input("enter your number "))
    
    if a_user_1>n_1:
        print("this number is too high.")
    elif (a_user_1<n_1):
        print("this number is too low.")
    guess_user_1+=1   

if (a_user_1==n_1):
    if guess_user_1==1:
      
      print("congratulations its a record.")
    else:
      print(f"you find the number {n_1} good. ")


print(f"now, its {user_2}'s turn: ")
print(f"lets see you can guess your number in less then {user_1}'s guesses or not ")

a_user_2=-1
guess_user_2=1

while (a_user_2!=n_2) :
    a_user_2=int(input("enter your number "))
    
    if a_user_2>n_2:
        print("this number is too high.")
    elif (a_user_2<n_2):
        print("this number is too low.")
    guess_user_2+=1   

print("wow you got this too , now lets check the result,who won!!!")

print(input("are u ready? (press enter)"))

if (guess_user_1>guess_user_2):
    print(f"{user_2} won!!!, congratulationsss.")
elif(guess_user_2>guess_user_1):
    print(f"{user_1} won!!!, congratulationsss.")        
else:
    print(f"Sorry to say its a TIE, play again to see who is the real winner.")