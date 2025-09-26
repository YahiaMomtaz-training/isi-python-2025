personName = input('Enter your name : ')
personAge = input('Enter your age : ')
personAge = int(personAge)

if personAge > 16:
    print('You are a man')
elif personAge >= 11:
    print('You are a boy')
else:
    print('You are a child')
