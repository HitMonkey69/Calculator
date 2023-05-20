#Calculator by HitMonkey69

import pyfiglet

banner = pyfiglet.figlet_format('Calculator')
print(banner)

print('Press + for add')
print('Press - for sub')
print('Press / for divide')
print('Press * for multiply')
print('Press q for quit')
x = 0
while True:

    do = input('Select action:')

    if do == 'q':
        banner = pyfiglet.figlet_format('ThankYou!')
        print(banner)
        break
    
    else:
        usr1 = int(input('Enter first number:'))
        usr2 = int(input('Enter second number:'))

    if do == '+':
        print(f'{usr1} + {usr2}:')
        x = (usr1 + usr2)
        print(x)

    elif do == '-':
        print(f'{usr1} - {usr2}:')
        x = (usr1 - usr2)
        print(x)

    elif do == '/':
        print(f'{usr1} / {usr2}:')
        x = (usr1 / usr2)
        print(x)

    elif do == '*':
        print(f'{usr1} * {usr2}:')
        x = (usr1 * usr2)
        print(x)

    else:
        print('Wrong action selected')