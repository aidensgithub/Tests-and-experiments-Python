import random


def randomlis():
    return list(set([random.randint(0, 255) for i in range(random.randint(3, 12))]))


h = randomlis()


x = [h[0], h[-1]]
print(h, "\n", x)

