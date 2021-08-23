import re

regex = re.compile(r'^[4-6][\d][-]*$')


def lenght(a):
    x = re.sub('-', '', a)
    if len(x) != 16:
        return False
    else:
        return True


def separator(a):
    x = re.findall("[_ ]", a)
    if len(x) > 0:
        return False
    else:
        return True


def repeated(a):
    j = True
    x = re.sub("-", "", a)
    if len(x) == 16:
        for i in range(13):
            if x[i] == x[i + 1] == x[i + 2] == x[i + 3] and i + 3 < 14:
                j = False
                return j
        return j


def divisor(a):
    if re.findall("-", a):
        x = re.split("-", a)
        for i in range(3):
            if len(x[i]) != 4:
                return False
    else:
        return True


def beg(a):
    x = re.split("",a)
    if x[1] == "4" or x[1] == '5' or x[1] == '6':
        return True
    else:
        return False


for _ in range(int(input())):
    ncreditc = input()
    if False in {lenght(ncreditc), separator(ncreditc), repeated(ncreditc), divisor(ncreditc), beg(ncreditc)}:
        print('Invalid')
    else:
        print('Valid')
