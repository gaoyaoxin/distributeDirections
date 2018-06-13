import random

count = 0
while count < 170:
    randomCode = random.sample(range(1, 6), 5)
    newCode = []
    for i in randomCode:
        i = str(i)
        newCode.append(i)
    print(' '.join(newCode))
    count += 1