#by sama aljwhari
num1 = float(input('Enter the first number: '))
oper = input('Choose an operation (+, -, *, /, %): ')
num2 = float(input('Enter the second number: '))

if oper == '+':
    result = num1 + num2
    print(num1, '+', num2, '=', result)

elif oper == '-':
    result = num1 - num2
    print(num1, '-', num2, '=', result)

elif oper == '*':
    result = num1 * num2
    print(num1, '*', num2, '=', result)

elif oper == '/':
    if num2 != 0:
        result = num1 / num2
        print(num1, '/', num2, '=', result)
    else:
        print('cant division by zero')

elif oper == '%':
    result = num1 % num2
    print(num1, '%', num2, '=', result)

else:
    print('Invalid operation', oper)