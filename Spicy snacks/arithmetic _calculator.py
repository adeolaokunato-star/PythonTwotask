num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))
calculator = input('Enter how you want to calculate(+,-,*,/):')
if calculator == '+':
    print(num1 + num2)
elif calculator == '-':
    print(num1 - num2)
elif calculator == '*':
    print(num1 * num2)
elif calculator == '/':
    print(num1 / num2)
else:
    print('Invaid')            
       

