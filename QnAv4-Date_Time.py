# added input error detection in While True: loop
# added functions
# added error function(red)
# added date/time

import datetime
from colorama import Fore, Style

def collectAnswer(expectedAnswer):
    options = ("a","b","c")
    response = False
    
    while True:
        guess = input("Your guess: ")
        if guess in options:
            if guess == expectedAnswer:
                print("Correct!\n")
                response = True  
            else:
                print("Incorrect!\n")
            break
        else:
            print(f"{Fore.RED} [INVALID] Invalid answer! {Style.RESET_ALL} Please try with the listed options again.")
            

    return response
        
x = datetime.datetime.now()
print(f'Starting time: {x.strftime("%c")}')

print("Python Quiz")
score = 0
name = input("What is your name? ")
# print("Welcome, " + name + "!")
print(f"Welcome, {name}!")

print(f"""1. What is 18.5?
a) a float
b) an integer
c) a string """)
# print("Your guess:  ")

if collectAnswer("a") == True:
    score += 1 

print(f"""2. Which answer means that counter is exactly the same as 3?
a) counter != 3
b) counter = 3
c) counter == 3 """)
# print("Your guess: ")

if collectAnswer("c") == True:
    score += 1

print(f"""3. A variable is: 
a) a piece of data that cannot be changed
b) a piece of data that can be changed
c) a piece of information that the user inputs""")
# print("Your guess: ")

if collectAnswer("b") == True:
    score += 1 

print(f"""3. The creator of Python is: 
a) Guido Van Rossum
b) Mark Zuckerburg
c) Elon Musk""")
# print("Your guess: ")

if collectAnswer("a") == True:
    score += 1 

print(f"Your score:  {str(score)} /4")
x = datetime.datetime.now()
print(f'Ending time: {x.strftime("%c")}')
#Shift down to select entire line