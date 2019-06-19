import random


def generatorp():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    psslen = 8
    return "".join(random.sample(s, psslen))

for i in range(0, 100):

    r =  generatorp()

    print(r)