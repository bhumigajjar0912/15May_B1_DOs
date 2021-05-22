#regitratin request
ask = input('Do you want to register?(y/n)')
if ask.lower() != 'n' and ask.lower() != 'y':
    while ask.lower() != 'n' or ask.lower() != 'y':
        print('Please provide valid input!')
        ask = input('Do you want to register?(y/n)')

#user input and password check

if ask == 'y':
    username = input('Enter your usename: ')
    while(True):
        password = input('Enter Password:')
        if len(password)<8:
            print('Length should be greate then 8, Try again!')
            continue
        elif not any(char.isdigit() for char in password):
            print('Length should have atlest one digit, Try again!')
            continue
        elif not any(char.islower() for char in password):
            print('Length should have atlest one lower case character, Try again!')
            continue
        elif not any(char.isupper() for char in password):
            print('Length should have atlest one uppercase charactor, Try again!')
            continue
        else:
            print('valid password')
            break
   
#login reqest
login = input('Do you want to login?(y/n) ')
if login.lower() != 'n' and login.lower() != 'y':
    while login.lower() != 'n' or login.lower() != 'y':
        print('Please provide valid input!')
        login = input('Do you want to login?(y/n)')
if login.lower() == 'y':
    u1 = input('Enter your usename: ')
    p1 = input('Enter password')
    if u1 != username and p1 != password:
        while u1 != username and p1 != password:
            print('Enter valid username/password')
            u1 = input('Enter your usename: ')
            p1 = input('Enter password')
    
#ask wor selecting one of the following task
    print('Task 1: Basic Calculator')
    print('Task 2: Table generator')
    print('Task 3: Pattern generator')
    print('Choose one of the following three task:')
    tasks = int(eval(input('Choose the task you want to perform ')))
    if tasks not in range(1,4):
        while tasks not in range(1,4):
            print('Please provide a valid input!')
            tasks = int(eval('Choose the task you want to perform'))

if tasks == 1:
    a = float(input('Enter 1st number:'))
    b = float(input('Enter 2nd number:'))
    print('Choose the following operations')
    print('Enter 1 for basic addition')
    print('Enter 2 for basic subtraction')
    print('Enter 3 for basic multiplication')
    print('Enter 4 for basic division')
    ops = int(eval('Enter opreation'))
    if ops == 1:
        print(a+b)
    if ops == 2:
        print(a-b)
    if ops == 3:
        print(a*b)
    if ops == 4:
        print(a/b)    
elif tasks == 2:
    n = int(input('Enter the numger: '))
    for i in range(1,11):
        print(str(n)+' x '+str(i)+' = '+str(n*i))
    
elif tasks == 3:
    n = int(input('Enter the numger: '))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')
        print('')
                

    
