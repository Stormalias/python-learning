import string
import random
import time
import calendar
from datetime import datetime


# Classwork Day 2

# Data Types qns
# 1)	Write a program that will get the first name and last name of the user
# and return the first name in uppercase and capitalized the first letter of the last name of the user. 
# (You can also add a message).

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
fullName = firstName.upper() + ' ' + lastName.title()

message = "welcome back {}! Note that your first name is in capitals"
print(message.format(fullName))

# 2)	Write a program that will get the name of the user and 2 numerical values, 
# then return the name in uppercase and the sum of the numbers with a message.

firstName = input("Enter your first name: ")
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
answer = num1 + num2
nameCap = firstName.upper()
message = "Hello there {0}. The sum of values is {1}"
print(message.format(nameCap, answer))

# 3)	Write a program that will get the following information from the user:

# •	Full name
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
fullName = firstName.title() + ' ' + lastName.title()

# •	Date of birth
dateOfBirth = input("Enter your date of birth (DD/MM/YYYY): ")

# Return a greeting to the user, with the following information:

# •	User’s current age
# •	User’s age on their next birthday
userYear = datetime.strptime(dateOfBirth , '%d/%m/%Y').strftime("%Y") # Just the year from user birth date
nowYear = datetime.today().strftime("%Y") # current year
age = int(nowYear) - int(userYear) # Difference is age in the year

nowMonthDay = datetime.today().strftime("%m%d") #MonthDay combination provides an integer to accurately find out if birthdate has passed
userMonthDay = datetime.strptime(dateOfBirth , '%d/%m/%Y').strftime("%m%d")

if int(nowMonthDay) < int(userMonthDay): # if statement to check if birthday has passed yet
    print(f"Your current age is {age - 1}")
    print(f"Your age on your next birthday will be {age}")
else:
    print(f"Your current age is {age}")
    print(f"Your age on your next birthday will be {age + 1}")

# •	Number of days to the next birthday
userDate = datetime.strptime(dateOfBirth, "%d/%m/%Y")
nowDate = datetime.today()

delta = userDate - nowDate #timeDelta object 
daysYear = age * 365.25 # Used to remove the days counted by difference in years
deltaDay = abs(delta.days) # The absolute difference in days between birthdate and today's date
dayDiff = round(abs(deltaDay - daysYear) + 0.5) # actual number of days to next birthday, with 0.5 days added to counter rounding error

print(f"Your next birthday is in {dayDiff} days")

# •	If year of birth is a leap year
if calendar.isleap(int(userYear)) == True: # using Calender module to return boolean value
    print("Your birthyear was a leap year!")
else:
    print("Your birthyear was not a leap year =(")




# Control structures qns
# 1)	Invite user to enter a number:
num = input("Enter your number here: ")
num = int(num)
# •	If the user number is a multiple of 3:  Display  "FIZZ"
if num % 3 == 0 and num % 5 != 0:
    print("FIZZ")
# •	if it is a multiple of 5:  Display   "BUZZ"
elif num % 5 == 0 and num % 3 != 0:
    print("BUZZ")
# •	and if it is a multiple of both 3 and 5: Display   "FIZZ BUZZ“
elif num % 3 == 0 and num % 5 == 0:
    print("FIZZ BUZZ")
# •	* If none of the above, display the user number.
else:
    print(num)

# 2)	Write a program which will find all the numbers which are divisible by 7 but are not a multiple of 5, between 100 and 203 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
numList = list(range(100, 204))

divNums = []
for num in numList:
    if num % 7 == 0 and num % 5 != 0:
        divNums.append(num)

print(divNums)

# 3)	Display a randomly generated number between 1 and 13.
# •	Show the number
randomNum = random.randrange(1, 14)
print(f"The random number is {randomNum}")
# •	Invite user to guess if next card/number is higher (H) or lower (L)
userGuess = input("Guess if the next number will be higher or lower (H/L): ")
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
    uGuess = input(f"Guess again?(H/L/X): ")

    if (uGuess == 'H' and ranNum < newNum) or (uGuess == 'L' and ranNum > newNum):
        print(f"The new number is {newNum}. You guessed {uGuess} correctly! YOU WIN!")
        counter += 1 # Points because why not
    elif uGuess == 'X': # Exit option
        exitClause = 'X'
    elif newNum == ranNum: # Extra flavour to the answer
        print(f"OOF the new number was {newNum} also! Unlucky that this game doesn't have a third option")
    elif uGuess != 'H' and uGuess != 'X' and uGuess != 'L': # psuedo-error handling
        print(f"incorrect input, try again. Higher, Lower or Exit(H/L/X). Number is currently {newNum}: ")
    else:
        print(f"the new number is {newNum}. You guessed wrongly!")
    
    ranNum = newNum # Replacing number

print(f"Your final score was {counter}")

# 4)	Modify your code from 1) but instead do the following:
# •	Generate a list of every number between 1 and 100
aList = list(range(2, 100))

# •	if a number is a multiple of 3 it is replaced with "FIZZ"
# •	if it is a multiple of 5 it is replaced by "BUZZ"
# •	if it is a multiple of both 3 and 5, it is replaced by " FIZZ BUZZ "

for num in range(len(aList)):
    if aList[num] % 3 == 0 and aList[num] % 5 == 0:
        aList[num] = "FIZZ BUZZ"
    elif aList[num] % 3 == 0:
        aList[num] = "FIZZ"
    elif aList[num] % 5 == 0:
        aList[num] = "BUZZ"

# Print out the list of results with a space between each item. 

print(aList)

# Syntax and Ops qns
username = input("Enter your username: ")
password = input("Enter your password: ")

# print("Welcome back " + user + "!") 
# # qn 1 code for reference

# 2)	Update your program to ask the user to type in their Username and Password.
# Check if the Username is one of the following (display appropriate message):
allUserList = ['UK_User1', 'US_USer2', 'Africa_User3', 'Canada_User4', 'Australia_User6']

if username not in allUserList:
   print("Invalid username") 

# 3)	Update your program to ask the user to type in their Username and Password. Display error message or a welcome message if the password has:

passLen = len(password)
numericCheck = [_ for _ in password if _.isdigit()]
upperCheck = [_ for _ in password if _.isupper()]
lowerCheck = [_ for _ in password if _.islower()]
alphaNumCheck = [_ for _ in password if _.isalnum()]

if username not in allUserList: # Repeated from qn 2 to ensure one error message displayed overall
    print("Invalid username") 
# •	a number of characters greater than 8
elif passLen <= 8:
    print("password too short")
# •	at least one numerical character
elif not numericCheck:
    print("password does not contain numbers")
# •	at least one uppercase
# •	at least one lowercase
elif not upperCheck or not lowerCheck:
    print("password does not contain appropriate lower and upper case letters")
# •	at least one non alphanumerical character
elif not alphaNumCheck:
    print("password does not contain alphanumeric characters")
else:
    print(f"Welcome back {username}")