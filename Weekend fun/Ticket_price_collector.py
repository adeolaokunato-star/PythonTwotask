age = int(input('Enter age: '))
if age < 5:
    print('Free')
elif age >= 5:
    print('$5')
elif age <= 12:
    print('$5')
elif age >= 13:
    print('$12')
elif age <= 64:
    print('$12')        
else:
    print('$8')    
