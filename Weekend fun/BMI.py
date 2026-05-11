weigth = int(input('Enter kg: '))
height = int(input('Enter meters: '))
bmi = weight / (height * height)
if bmi < 18:
    print('Underweight')
elif bmi >= 18.5 and bmi <= 24.9:
    print('Normal')    
elif bmi >= 25 and bmi <= 29.9:
    print('Overweight')
else:
    print('Obese')
