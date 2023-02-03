# added input error detection in While True: loop
# added functions
# import os
# added error function(red)

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
            # os.system("cls")
            print(f"\033[0;31m [INVALID] Invalid answer! \033[0;37m Please try with the listed options again.")
    return response
        

print("Python Quiz")
score = 0
name = input("What is your name? ")
# print("Welcome, " + name + "!")
print(f"Welcome, {name}!")


print(f"""1. What is 18.5?
a) a float
b) an integer
c) a string """)
# print("Your guess: 

if collectAnswer("a") == True:
    score += 1 

print(f"""2. Which answer means that counter is exactly the same as 3?
a) counter != 3
b) counter = 3
c) counter == 3 """)
# print("Your guess: 

if collectAnswer("c") == True:
    score += 1 

print(f"""3. A variable is: 
a) a piece of data that cannot be changed
b) a piece of data that can be changed
c) a piece of information that the user inputs""")
# print("Your guess: ")

if collectAnswer("b") == True:
    score += 1 


print(f"Your score:  {str(score)} /3")
#Shift down to select entire line