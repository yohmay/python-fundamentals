#Initial Concepts

variable = input()

print(variable)
print(variable, variable)
print(variable, variable, variable)
print(variable, variable, variable, variable)
print(variable, variable, variable, variable, variable)

################################################################
name = input()
last_name = input()
print(name, last_name)

################################################################
name = input()
age = int(input())

print(age - 2)
print(name)

################################################################
value = int(input())

print(value + 1)
print(value - 1)
print(value * 2)
print(value ** 2)

################################################################
value1 = int(input())
value2 = int(input())

print(value1 + value2)
print(value1 - value2)
print(value1 * value2)
print(value1 ** value2)

#################################################################
num1 = int(input())
num2 = int(input())
num3 = int(input())

sum_result = num1 + num2 + num3
product_result = num1 * num2 * num3

print(sum_result)
print(product_result)

#################################################################
value1 = int(input())
value2 = int(input())

result_div = value1 // value2
result_mod = value1 % value2

print(result_div)
print(result_mod)

#################################################################
size_list = int(input("Enter the size of the first list: "))
min_value = int(input("Enter the minimum value of the first list: "))
another_list = int(input("Enter another list: "))

new_min_value = (min_value * another_list) / size_list

print("The new minimum value for the second list is:", new_min_value)

#################################################################
num1 = float(input())
num2 = float(input())

print(num1 + num2)
print(num1 * num2)
print(num1 / num2)

#################################################################
value = float(input())

print('%.0f' % value)
print('%.1f' % value)
print('%.2f' % value)
print('%.3f' % value)
print('%.4f' % value)

#################################################################
product_value = float(input("Enter the product value: "))
discount_percentage = float(input("Enter the discount percentage: "))

discounted_value = (product_value * discount_percentage) / 100
final_value = product_value - discounted_value

print('%.2f' % product_value)
print('%.2f' % final_value)
print('%.2f' % discounted_value)

#################################################################
students = int(input("Enter the number of students: "))
days = int(input("Enter the number of days: "))
monitors = int(input("Enter the number of monitors: "))
extra_students = int(input("Enter the number of extra students: "))
extra_days = int(input("Enter the number of extra days: "))

total_students_days = students * days
extra_students_days = extra_students * extra_days

extra_monitors = int((extra_students_days * monitors) / total_students_days)

print(extra_monitors)

#################################################################
letters = input("Enter a letter: ")

if letters.lower() == "a":
    print("LEFT")
elif letters.lower() == "s":
    print("DOWN")
elif letters.lower() == "w":
    print("UP")
elif letters.lower() == "d":
    print("RIGHT")
else:
    print("?")

#################################################################
age = int(input("Enter age: "))

if age >= 60:
    print(age, "Golden age!")
    
print("End")

#################################################################
age = int(input("Enter age: "))

if age >= 60:
    print("Free")
else:
    print("Paid")

#################################################################
age = int(input("Enter age: "))

if age >= 60:
    print("Free")
elif age < 6:
    print("Free on lap")
else:
    print("Paid")

#################################################################
value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))
operator = input("Enter the operator: ")

if operator == "+":
    result = value1 + value2
elif operator == "-":
    result = value1 - value2
elif operator == "*":
    result = value1 * value2
elif operator == "/":
    result = value1 / value2
elif operator == "//":
    result = value1 // value2
elif operator == "%":
    result = value1 % value2
elif operator == "**":
    result = value1 ** value2

if result % 1 == 0:
    print(result)
else:
    print('%.1f' % result)

#################################################################
#################################################################

battery = int(input("Enter the battery level: "))

while battery > 0:
    print(battery)
    battery -= 1
else:
    print('End')
