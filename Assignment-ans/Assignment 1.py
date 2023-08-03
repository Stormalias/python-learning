import string

# Q1-2  
# Convert  symbol(s)  from flowchart into Python code.

# Set Variables and input data

allowedToPlay = 0 # Easy to use numerical values assigned to different print outputs
userAge = int(input("Enter your age here: "))
userGender = input("Enter your gender (M/F): ")

# Gender and age decisions

if userGender == 'M':
    if userAge >= 18:
        allowedToPlay = 1
    elif userAge < 0:
        allowedToPlay = 2
    elif userAge < 18:
        allowedToPlay = 0
    
elif userGender == 'F':
    if userAge >= 21:
        allowedToPlay = 1
    elif userAge < 0:
        allowedToPlay = 2
    elif userAge < 21:
        allowedToPlay = 0
    
else:
    allowedToPlay = 2

# Processing and output
if allowedToPlay == 1:
    print("You can play!")
elif allowedToPlay == 0:
    print("You cannot play!")
else:
    print("Invalid input!")


'''
Write a Python program that read words from the user until the user enters a blank line.  
After the user enters a blank line your program should display each word entered by the user exactly once. 
'''
inputList = []
userInput = 0 #Initial value to enter loop. Inconsequential

while userInput != '':
    userInput = input("Word reader active. Enter your word here: ")
    if userInput == '':
        break
    else:
        inputList.append(userInput)

editedList = list(dict.fromkeys(inputList)) # Convert compiled list to dictionary to remove duplicates, and make it a list again

for word in editedList:
    print(word)

'''
Q3-1
Write a Python program to ask user to enter the NRIC ID card number and apply the following rules to check whether it has a valid format. Report any invalid format to user.
a.	Has a length of 9. 
b.	Starts with a “S” and ends with a letter.
c.	Contains 7 numbers between the two letters.
The valid format is SNNNNNNNL where N represents a number and L represents a letter.

Q3-2
Write a function in the Python program from Q3-1 to apply the following calculations in sequence to validate the last letter of the NRIC ID card number. 
Report any invalid last letter to user.
1.	Multiply each of the 7 numbers with 2, 7, 6, 5, 4, 3, 2 in sequence. 
2.	Sum up the multiplication results.
3.	Divide the sum result by 11 and get the reminder.  
4.	Match the remainder with the letter in the table.
5.	The NRIC number must have the corresponding letter in the table.
For example, “S7654321” produces a remainder 5, so it should end with a “F”.
'''


def validateLetter(ic): # Declaring function first to be able to run function in if/else block
    numerics = [_ for _ in ic if _.isdigit()]
    multiplyList = [2, 7, 6, 5, 4, 3, 2]
    validLetters = ['J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

    i = 0
    total = 0

    while i < 7:
        multiples = int(numerics[i]) * int(multiplyList[i])
        total = int(total) + multiples
        i += 1

    Rem = total % 11
    if validLetters[Rem] != icList[-1]:
        print("Invalid last letter in IC number")
    else:
        print("NRIC seems correct")

userIC = input("Enter your NRIC here: ")
icList = list(userIC)

if len(userIC) != 9:
    print("Invalid input: Not 9 characters total")
elif icList[0] != 'S' or not icList[-1].isalpha():
    print("Invalid input: First or last character incorrect")
elif not userIC[1:7].isdigit():
    print("Invalid input: Not enough numbers in the middle")
else:
    validateLetter(userIC)

'''
A departmental store has some mystery gifts to be given away to the first 10 lucky customer every day.
giftList = ['$10 vouchers', 'Keychain', 'Umbrella', 'Tote Bag','$50 vouchers', '25% rebate for all purchases', 
'DKNY perfume 25ml', '$20 vouchers', 'Kose Mask White 50ml', 'Pearl Necklace']

•	Lucky customers could not see the gifts in the list, but get to choose the gift based on the position of the gift in the list.
•	Write a Python program to remove the gift in the position customer has chosen from the list and show the customer what is the mystery gift. 
•	The program would do this for 10 times, removing 1 gift from the list each time, until all the gifts has been given out.  
•	In addition, it must display the position of the remaining gifts in the list after each draw.
'''

giftList = ['$10 vouchers', 'Keychain', 'Umbrella', 'Tote Bag','$50 vouchers', '25% rebate for all purchases', 'DKNY perfume 25ml', '$20 vouchers', 'Kose Mask White 50ml', 'Pearl Necklace']


while len(giftList) != 0:

    userChoice = int(input(f"Pick a number between 1 and {len(giftList)}: "))
    userGift = giftList[userChoice - 1]
    print(f"you picked {userChoice} and your prize is {userGift}")
    
    del giftList[userChoice - 1]

