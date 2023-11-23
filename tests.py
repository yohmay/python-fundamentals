weight = float(input())
height = float(input())

imc = weight / (height * height)

if imc < 17:
    print('{:.2f} Very below weight'.format(imc))
elif 17 <= imc <= 18.49:
    print('{:.2f} Below weight'.format(imc))
elif 18.50 <= imc <= 24.99:
    print('{:.2f} Normal weight'.format(imc))
elif 25 <= imc <= 29.99:
    print('{:.2f} Above weight'.format(imc))
elif 30 <= imc <= 34.99:
    print('{:.2f} Obesity I'.format(imc))
elif 35 <= imc <= 39.99:
    print('{:.2f} Obesity II (severe)'.format(imc))
elif imc >= 40:
    print('{:.2f} Obesity III (morbid)'.format(imc))

################################################################
bill = float(input())
percentage = int(input())

total = bill + (bill * percentage) / 100
print('%.2f' % total)

################################################################
number = input()

for digit in number:
    if digit == '0':
        print('')
    else:
        print("*" * int(digit))

################################################################
number = int(input())
total = number

while total >= 0:
    number = int(input())
    total += number
    if number == 0:
        print(">8)")
        break

if total < 0:
    print(">8(")
