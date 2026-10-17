import random
wel= ' !! Welcome to the number guessing game !!'
print(wel.center(45))
comp =random.randint(1,100)

def guess():
    count=0
    while True:    
        a =int(input('Guess the number: '))
        count+=1
        if a== comp:
            print('Congrats you guessed right')
            print('Attempts=',count)
            break
        elif a>comp:
            print('You are higher')
        elif a<comp:
            print('You are lower')
        else:
            print('Invalid Input')

guess()

while True:
    k = input('Enter yes if wanna play again otherwise enter quit\n')
    if k=='yes':
        guess()
    elif k=='quit':
        print('---Thanks for using---')
        break
    else:
        print('Invalid Input')