import random

a = random.randint(1,10)
attempt = 3
while attempt>0:
    usernumber = int(input('ведите число от 1 до 10: '))
    if usernumber == a:
        print ('вы угадали')
        break
    else:
        print('вы не угадали')
        attempt -=1









