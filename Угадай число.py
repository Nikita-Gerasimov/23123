
import random



##def func():
##    guessesTaken = 0
##
##    print('Как тебя зовут?')
##    myName = input()
##
##    number = random.randint(1,20)
##    print(myName+', я загадал число от одного до 20, у тебя есть 5 попыток')
##
##    while guessesTaken < 5:
##        print('Как ты думаешь, какое?')
##        guess = int(input())
##
##        guessesTaken += 1
##
##        if guess < number:
##            print('Моё число больше твоего')
##
##        if guess > number:
##            print('Моё число меньше твоего')
##
##        if guess == number:
##            break
##
##    if guess == number:
##        guessesTaken = str(guessesTaken)
##        print('Превосходно '+myName+'! Ты угадал число с '+guessesTaken+' попытки.')
##
##    if guess != number:
##        number = str(number)
##        print('Жаль, но у тебя не осталось попыток. Я загадал число '+number+'. Ты проиграл...')

guessesTaken = 0
print('Как тебя зовут?')
myName = input()

number = random.randint(1,20)
print(myName+', я загадал число от одного до 20, у тебя есть 5 попыток')

while guessesTaken < 5:
    print('Как ты думаешь, какое?')
    guess = int(input())

    guessesTaken += 1

    if guess < number:
        print('Моё число больше твоего')

    if guess > number:
        print('Моё число меньше твоего')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Превосходно '+myName+'! Ты угадал число с '+guessesTaken+' попытки.')

if guess != number:
    number = str(number)
    print('Жаль, но у тебя не осталось попыток. Я загадал число '+number+'. Ты проиграл...')
