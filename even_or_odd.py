user = int(input('please enter an number: '))
check = int(input('please enter another number for divide by: '))
mod = user % 2
four = user % 4


if mod == 1:
    print('the number you have entered is odd')
else:
    print('the number you have entered is even')

if four == 0:
    print('this number also a multiple of four')

if user % check == 0:
    print('this number also divides evenly by')
else:
    print('this number cannot divide evenly by')
