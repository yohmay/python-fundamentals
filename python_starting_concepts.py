digit1 = input("Enter the first digit: ")
digit2 = input("Enter the second digit: ")
digit3 = input("Enter the third digit: ")
digit4 = input("Enter the fourth digit: ")

number = int(digit1 + digit2 + digit3 + digit4)
result = number * 2
print(result)

################################################################
power_of_3 = int(input("Enter the value for 2^3: "))
power_of_2 = int(input("Enter the value for 2^2: "))
power_of_1 = int(input("Enter the value for 2^1: "))
power_of_0 = int(input("Enter the value for 2^0: "))

total_value = 0

if power_of_0 == 1:
    total_value += 1 
if power_of_1 == 1:
    total_value += 2
if power_of_2 == 1:
    total_value += 4 
if power_of_3 == 1:
    total_value += 8 

print(total_value)

################################################################
first_year = int(input("Enter the first year: "))
second_year = int(input("Enter the second year: "))

result_sum = first_year + second_year
print(result_sum)

################################################################
document_name = input("Enter the document name: ")
confirmation_first = input("Confirm selection (type 'ok'): ")
confirmation_second = input("Confirm selection (type 'ok'): ")

if document_name and confirmation_first == "ok" and confirmation_second == "ok":
    print(f"{document_name} selected")
else:
    print(f"{document_name} not selected")

################################################################
hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))

result_minutes = hours * 60
total_minutes = (hours * 60) + minutes
print(total_minutes)

################################################################
animal_type = input("Enter the type of animal: ")
attribute = input("Enter an attribute: ")
action = input("Enter an action: ")

print("A", animal_type, "has", attribute, "and can", action)

################################################################
score_team1 = int(input("Enter the score for Team 1: "))
score_team2 = int(input("Enter the score for Team 2: "))

if score_team1 >= 25 or score_team2 >= 25:
    if (score_team1 - 1 > score_team2) or (score_team2 - 1 > score_team1):
        print("Yes")
    else:
        print("No")
else:
    print("No")

################################################################
player_name = input("Enter player's name: ")
cards = input("Enter the cards: ")

if "mico" in cards:
    print(player_name, "got caught!")
else:
    print(player_name, "is okay.")

################################################################
candidate = input("Enter the candidate's name: ")
item_list = input("Enter the list of items: ")

for item in item_list:
    candidate = candidate.replace(item, "*")

print(candidate)

################################################################
character = input("Enter the character to replace: ")
replacement = input("Enter the replacement character: ")
message = input("Enter the message: ")

message = message.replace(character, replacement)
print(message)

################################################################
message = input("Enter a message: ")

new_message = ""
for char in message:
    if char.lower() == "a":
        new_message += "@"
    elif char.lower() == "o":
        new_message += "*"
    else:
        new_message += char.lower()

print(new_message)

################################################################
card_first = input("Enter the first card: ")
card_second = input("Enter the second card: ")
card_third = input("Enter the third card: ")

manilha_count = 0

manilha_cards = ["4Clubs", "7Hearts", "ASpades", "7Diamonds"]

if card_first in manilha_cards:
    manilha_count += 1
if card_second in manilha_cards:
    manilha_count += 1
if card_third in manilha_cards:
    manilha_count += 1

print(manilha_count)

################################################################
number = int(input("Enter a number: "))

for multiplier in range(1, 12):
    print(number * multiplier)

################################################################
number = int(input("Enter a number: "))

print("Multiplication Table for", number)
for multiplier in range(1, 12):
    print(number, "x", multiplier, "=", number * multiplier)

################################################################
double_cripto = int(input("Enter 0 for encryption, 1 for decryption: "))
message = input("Enter the message: ")

new_message = ""

if double_cripto == 0:
    for char in message:
        if char.lower() == "a":
            new_message += "@"
        elif char.lower() == "o":
            new_message += "*"
        elif char.lower() == "e":
            new_message += "&"
        else:
            new_message += char.lower()
else:
    for char in message:
        if char == "@":
            new_message += "a"
        elif char == "*":
            new_message += "o"
        elif char == "&":
            new_message += "e"
        else:
            new_message += char.lower()

print(new_message)

################################################################
################################################################

name = input()
age = int(input())
pi_value = float(input())

print(name, 'is', age, 'years old and likes the number', pi_value)

name = input()
size = 0
for letter in name:
    print(letter)
    size += 1
length = len(name)
print(size, '=', length)

name = input()
size = 0
adjusted_name = ''
for letter in name:
    if letter == ' ':
        letter = '_'
    adjusted_name += letter  
    size += 1
length = len(name)
print(size, '=', length)
print(adjusted_name)

