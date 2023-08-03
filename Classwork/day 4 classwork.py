import random

# Classwork day 4
# 5)	Modify the code created for 3) to use exception handling to validate the user inputs.
# If invalid responses are given the code should:
# •	display error message to the user 
# •	not crash the program
# •	repeat the prompt till a valid response is received

# Display a randomly generated number between 1 and 13.
# •	Show the number
randomNum = random.randrange(1, 14)
print(f"The random number is {randomNum}")
# •	Invite user to guess if next card/number is higher (H) or lower (L)
while True:
    try:
        userGuess = input("Guess if the next number will be higher or lower (H/L): ")
        if userGuess == 'H' or userGuess == 'L':
            break
        else:
            raise TypeError
    except:
        print("Invalid input. Try again")

counter = 0
# •	Then generated another random number between 1 - 13
randomNumTemp = random.randrange(1, 14)

# •	Player loses if they guess wrong. Player wins if they guess right
# •	Show the number and the appropriate message
if (userGuess == 'H' and randomNumTemp > randomNum) or (userGuess == 'L' and randomNumTemp < randomNum):
    print(f"The new number is {randomNumTemp}. You guessed {userGuess} correctly! YOU WIN!")
    counter += 1
else:
    print(f"the new number is {randomNumTemp}. You guessed wrongly!")
# •	Loop: the game should default to replay but also offer an exit condition

exitClause = 'Q'
ranNum = randomNumTemp # 

while exitClause != 'X':
    newNum = random.randrange(1, 14)
    print("X to exit")
    while True: #Loop to ensure user input is correct
        try:
            uGuess = input(f"Guess again?(H/L/X): ")
            if uGuess == 'H' or uGuess == 'L' or uGuess == 'X':
                break # Leaves loop if correct input is detected
            else:
                raise TypeError
        except:
            print("Invalid input. Try again")

    if (uGuess == 'H' and ranNum < newNum) or (uGuess == 'L' and ranNum > newNum):
        print(f"The new number is {newNum}. You guessed {uGuess} correctly! YOU WIN!")
        counter += 1 # Points because why not
    elif uGuess == 'X': # Exit option
        exitClause = 'X'
    elif newNum == ranNum: # Extra flavour to the answer
        print(f"OOF the new number was {newNum} also! Unlucky that this game doesn't have a third option")
    else:
        print(f"the new number is {newNum}. You guessed wrongly!")
    
    ranNum = newNum # Replacing number

print(f"Your final score was {counter}")



# String n Functions
# Q1 
# Given the code below:

word = "python programming"

# Write the codes to do the following:
# Extract the word ‘python’ and store its value in variable a.
wordS = word.split()
a = wordS[0]

# Extract the word ‘programming’ and store its value in variable b.
b = wordS[1]
# Print out the number of letters (exclude spaces) in the variable word.
print(len(word) - word.count(" "))

# Print out the number of letters (include spaces) in the variable word.
print(len(word))

# Q2
sentence = "Dell profit surges on revived business spending in 2014"
words = sentence.split()

# Suppose the above codes are at the start of a python program. Write the code that follows to achieve the following:
# Print “Dell revived business in 2014” using the words variable in the codes in your answer. 
print(words[0], words[4], words[5], words[-2], words[-1])

# Print the number of words in the string sentence. 
print(len(words))

# Q3
# Complete the program below to print the following output from the nameList (each name on it's own line in caps). 
# You must use a for loop in your answer.

nameList = ["tom", "jack", "mark", "alice", "john"]
for name in nameList:
    print(name.upper())


# Q4
# A name is in the format of 
# <first name> <second name> <third name>
# For example, a valid name would be something like Lim Shi Yip.

# luckyNumber = (2 * F + S)%10 + T
# Where F = Length of first name
# Where S = Length of second name
# Where T = Length of third name

# Write a function calculateLuckyNumber(name) that takes in name to calculate & Return the lucky number using the formula given. 
# E.g. calculateLuckyNumber("Lim Shi Yip") will return the lucky number for the name “Lim Shi Yip”

def calculateLuckyNumber(name):
    splitName = name.split()
    F = len(splitName[0])
    S = len(splitName[1])
    T = len(splitName[2])

    luckNum = (2 * F + S)%10 + T
    print(luckNum)

calculateLuckyNumber("Lim Shi Yip")

# Q5
# Write a function calculateAverage that take in a list of 5 numbers as argument 
# and return the average of this 5 numbers using for or while loop. A sample out of the shell is as follow:
# sample shows function taking in list and printing avg in float

def calculateAverage(numList):
    total = 0
    numb = len(numList)
    
    for i in numList:
        total = total + i
    
    averg = total / numb
    return(averg)

testList = [9, 13, 15, 10, 7]
print(calculateAverage(testList))

# Write a python program to ask user to enter 5 numbers using for or while loop and store the numbers into a list variable numberList.  
# User the function calculateAverage to calculate the average of the numbers entered. The first line of the code is given below:

numberList = []

i = 1
while i <= 5:
    num = int(input(f"Enter number {i}: "))
    numberList.append(num)
    i += 1

print(f"The List of numbers entered is {numberList}")
print(f"the average score is {calculateAverage(numberList)}")

# Q6
# Write a function “link_points” to calculate the total number of link points customer earns based on their purchase amount and return the result

# For every 5 dollars spent award 1 link point
# Only award link points if purchase amount is more than $20

# Ask the cashier to enter the purchase amount
# Call the function and display the number of link points the customer earns

def link_points(amount):
    if amount > 20:
        points = amount // 5
    else:
        points = 0
    print(f"Total link points earned: {points}")

amount = int(input("Enter the total purchase amount: "))
link_points(amount)