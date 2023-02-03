# added input error detection in While True: loop

options = ("a)","b)","c)")

print("Python Quiz")
score = 0
print("Welcome, player!")
print("1. What is 18.5?")
print("a) a float")
print("b) an integer")
print("c) a string")
# print("Your guess: ")
while True:
    guess = input("Your guess: ")
    if guess in options:
        while guess == "a)":
            print("Correct!")
            score = score + 1
            break
        while guess != "a)":
            print("Incorrect!")
            break
        break
    else:
        print("Invalid answer! Please try again.")

print("2. Which answer means that counter is exactly the same as 3?")
print("a) counter != 3")
print("b) counter = 3")
print("c) counter == 3")
# print("Your guess: ")
while True:
    guess = input("Your guess: ")
    if guess in options:
        while guess == "c)":
            print("Correct!")
            score = score + 1
            break
        while guess != "c)":
            print("Incorrect!")
            break
        break
    else: 
        print("Invalid answer! Please try again.")
print("3. A variable is: ")
print("a) a piece of data that cannot be changed")
print("b) a piece of data that can be changed")
print("c) a piece of information that the user inputs")
# print("Your guess: ")
while True:
    guess = input("Your guess: ")
    if guess in options:
        while guess == "b)":
            print("Correct!")
            score = score + 1
            break
        while guess != "b)":
            print("Incorrect!")
            break
        break
    else:
        print("Invalid answer! Please try again.")

print("Your score: " + str(score) + "/3")