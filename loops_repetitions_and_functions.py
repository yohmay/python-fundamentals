total_numbers = int(input("Enter the total number of values: "))
number_list = []

for _ in range(total_numbers):
    num = int(input("Enter a number: "))
    number_list.append(num)

total_sum = sum(number_list)
print(total_sum)

################################################################
min_value = int(input("Enter the minimum value: "))
total = 0

while total < min_value:
    total += int(input("Enter a value: "))

print("Minimum:", min_value)
print("Total:", total)
print("Excess:", total - min_value)

################################################################
input_str = ""

while input_str != 'CDA':
    input_str = input()
    if 'CDA' in input_str:
        print('CDA 1942')
    else:
        print(input_str)


################################################################
count = 0
sentence = ''

while 'CDA 1942' not in sentence:
    sentence = input()
    if sentence == 'CDA 1942':
        break
    count += 1

print(count)

################################################################
count = 0
sentence = ''

while 'CDA 1942' not in sentence:
    sentence = input()
    if sentence == 'CDA 1942':
        break
    if sentence:
        count += 1

print(count)

################################################################
target = int(input("Enter the target number: "))
guess = ''

while guess != target:
    guess = int(input("Enter your guess: "))
    if target > guess:
        print("Greater")
    elif guess > target:
        print("Smaller")
    else:
        print("Equal")

################################################################
total_items = int(input("Enter the total number of items: "))
value = int(input("Enter the initial value: "))
item_count = 0

balance = float(total_items)
while True:
    if (balance - value) >= 0:
        balance -= value
        item_count += 1
        if balance:
            value = int(input("Enter the next value: "))
    else:
        break

print("Number of items:", item_count)
print("Balance: {:.2f}".format(balance))

################################################################
total_items = int(input("Enter the total number of items: "))
value = int(input("Enter the initial value: "))
item_count = 0

balance = float(total_items)
while True:
    if (balance - value) >= 0:
        balance -= value
        item_count += 1
        if balance:
            value = int(input("Enter the next value: "))
    else:
        break

print("Number of items:", item_count)
print("Balance: {:.2f}".format(balance))

################################################################
initial_battery_level = int(input("Enter the initial battery level: "))
command_first = ''
command_second = ''

while initial_battery_level > 5:
    command_first = input("Enter the first command (B/L): ").upper()
    command_second = input("Enter the second command (A/P): ").upper()

    if command_first == "B" and command_second == "A":
        initial_battery_level -= 5
        print("Turn:", initial_battery_level)
    elif command_first == "L" and command_second == "P":
        initial_battery_level -= 1
        print("Move forward:", initial_battery_level)
    elif command_first == "B" and command_second == "P":
        initial_battery_level -= 5
        print("Turn:", initial_battery_level)
    elif command_first == "L" and command_second == "A":
        initial_battery_level -= 5
        print("Turn:", initial_battery_level)

print('Recharge:', initial_battery_level)

################################################################
num_candles = int(input("Enter the number of candles: "))

for candle in range(num_candles):
    candle_lit = True
    while candle_lit:
        breath_strength = input("Enter the strength of your breath: ")
        if len(breath_strength) < 3:
            print("Need much more strength in the breath!")
        elif len(breath_strength) < 8:
            print("A bit more strength in the breath!")
        elif len(breath_strength) >= 8:
            print("Good breath!")
            candle_lit = False

print("Congratulations on your", num_candles, "years birthday!")

################################################################
stop_condition = input("Enter the stop condition: ")
lines = 0
phrase = input("Enter a phrase: ")

if stop_condition != phrase:
    while stop_condition != phrase:
        phrase = input()
        lines += 1

print(lines)

################################################################
memory = int(input())
entered_value = memory
peak_value = memory

while entered_value != 0:
    if memory > peak_value:
        peak_value = memory
    entered_value = int(input())
    memory += entered_value

print(peak_value)

################################################################
grade = int(input())
total_value = grade

while grade != 0:
    grade = int(input())
    total_value += grade

print(total_value)

################################################################
word = input()
spelling = input()
letter = ''

while letter != '.':
    letter = input()
    if letter != '.':
        spelling += letter

print(word == spelling)

################################################################
still = 1
movement = 0

data = input()

while data != 'f':
    if data == 'p':
        still += 1
    elif data == 'm':
        movement += 1
    data = input()

if movement > still:
    print('active')
else:
    print('sedentary')