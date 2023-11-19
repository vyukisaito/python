import random
num = [1, 4, 5, 2]
num.append(9)
num[3] = 4
num.sort(reverse=True)
num.remove(4)
print(num)
print(f'A lista tem {len(num)} elementos')
