num_One = int(input('Enter a number: '))
num_Two = int(input('Enter a number: '))
num_Three = int(input('Enter a number: '))
largest = num_One
if num_Two > largest:
    largest = num_Two
if num_Three > largest:
    largest = num_Three
print(largest)    
