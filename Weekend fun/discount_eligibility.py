total_bill = int(input('Enter total bill: '))
is_member = input('Are you a member? yes/no: ')
discount = 0
if total_bill >= 1000 and is_member == 'yes':
    discount = total_bill * 0.10
    print('10% discount applied')
elif total_bill >= 1000 and is_member == 'no':
    discount = total_bill * 0.05
    print('5% discount applied')
else:
    print('No discount')
final_amount = total_bill - discount
print(final_amount)    
