import random
while True:
    b=random.randint(0,10)
    a=int(input())
    if a==b: print('Exactly!')
    elif a<b: print('Greater!')
    elif a>b: print('Less!')
