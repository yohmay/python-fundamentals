number = int(input("Enter a number: "))
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))

print("Multiplication Table for", number, "from", start_number, "to", end_number)
for i in range(start_number, end_number + 1):
    print(number, "x", i, "=", number * i)

  
################################################################
number = int(input("Enter a number: "))
for i in range(number + 1):
    print(i)


################################################################
number = int(input("Enter a number: "))

for i in range(0, number, 2):
    print(i)


################################################################
number = int(input("Enter a number: "))
total = 0

for i in range(0, number + 1, 3):
    total += i

print(total)


################################################################
code = input().lower()

if code == "v":
    print("['a', 'e', 'i', 'o', 'u']")
elif code == "p":
    print("[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]")
elif code == "n":
    print("[10.0, 9.5, 8.0, 7.5]")
elif code == "a":
    print("['Maria', 85, 9.5]")
elif code == "z":
    print("[]")


################################################################
numbers = input("Enter a sequence of numbers: ").split()

for digit in range(10):
    count = numbers.count(str(digit))
    print(digit, count)


################################################################
numbers = [int(i) for i in input("Enter a sequence of integers: ").split()]
minimum_value = min(numbers)
maximum_value = max(numbers) + 1

for value in range(minimum_value, maximum_value):
    count = numbers.count(value)
    print(value, count)

################################################################
numbers = [int(i) for i in input("Enter a sequence of integers: ").split()]
numbers.sort()
unique_numbers = []

for value in numbers:
    if value not in unique_numbers:
        count = numbers.count(value)
        print(value, count)
        unique_numbers.append(value)

print("Sum of all numbers:", sum(numbers))

################################################################

#String Concatenation:
current_day, current_month, current_year = input().split()
expiry_day, expiry_month, expiry_year = input().split()

current_date = int(current_year + current_month + current_day)
expiry_date = int(expiry_year + expiry_month + expiry_day)

if current_date <= expiry_date:
    if current_month == expiry_month and current_year == expiry_year:
        print("Expires this month")
    elif current_year == expiry_year:
        print("Expires this year")
    else:
        print("Valid")
else:
    print("Expired!")

#List Indexing:
current_list = input().split()
current_day = current_list[0]
current_month = current_list[1]
current_year = current_list[2]

expiry_list = input().split()
expiry_day = expiry_list[0]
expiry_month = expiry_list[1]
expiry_year = expiry_list[2]

current_date = int(current_year + current_month + current_day)
expiry_date = int(expiry_year + expiry_month + expiry_day)

if current_date <= expiry_date:
    if current_month == expiry_month and current_year == expiry_year:
        print("Expires this month")
    elif current_year == expiry_year:
        print("Expires this year")
    else:
        print("Valid")
else:
    print("Expired!")

#Datetime Module:
import datetime

current_date_values = [int(x) for x in input().split()]
expiry_date_values = [int(x) for x in input().split()]

today = datetime.datetime(current_date_values[2], current_date_values[1], current_date_values[0])
expiry_date = datetime.datetime(expiry_date_values[2], expiry_date_values[1], expiry_date_values[0])

if today <= expiry_date:
    if today.month == expiry_date.month and today.year == expiry_date.year:
        print("Expires this month")
    elif today.year == expiry_date.year:
        print("Expires this year")
    else:
        print("Valid")
else:
    print("Expired!")

################################################################
grades = [float(x) for x in input("Enter grades separated by space: ").split()]

grades.sort()
grades.reverse()
print(grades)

################################################################
word = input("Enter a word: ")
word_list = input("Enter a list of words separated by space: ").split()

if word in word_list:
    print(word, word_list.index(word))
else:
    print("Missing:", word)

################################################################
word_list = input("Enter a list of words separated by space: ").split()
to_search = input("Enter words to search for separated by space: ").split()

total_to_search = len(to_search)

for word in to_search:
    if word in word_list:
        print(word, word_list.index(word))

################################################################
words_to_search = input("Enter words to search for separated by space: ").split()
list_of_lists = []
num_lines = int(input("Enter the number of lines: "))

for _ in range(num_lines):
    list_of_lists.append(input("Enter a line of words separated by space: ").split())

total_words_to_search = len(words_to_search)

for word in words_to_search:
    for line_index in range(num_lines):
        if word in list_of_lists[line_index]:
            word_index = list_of_lists[line_index].index(word)
            print(word, line_index, word_index)