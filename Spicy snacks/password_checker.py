password = input('Enter passward')
length = len(password)
if length < 1:
    print('invaild Password')
elif length < 6:
    print('Weak password')
elif length <= 10:
    print('Medium password')
else:
    print('Strong password')
