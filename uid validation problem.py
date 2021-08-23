import re



def VLENGHT(uid):
    if len(uid) == 10:
        return True
    else:
        return False


def vup(uid):
    x = re.findall('[A-Z]', uid)
    if len(x) > 1:
        return True
    else:
        return False


def vdig(uid):
    x = re.findall("\d", uid)
    if len(x) > 2:
        return True
    else:
        return False


def valfa(uid):
    x = re.findall('\w', uid)
    if len(x) > 0:
        l = 0
    else:
        l = 1
    x = re.findall('_', uid)
    if len(x) > 0:
        l = 0
    else:
        l = 1
    if l == 1:
        return True
    else:
        return False


def vrep(uid):
    x = re.findall('\w', uid)
    for _ in range(10):
        y = re.findall(x[_], uid)
        if len(y) > 1:
            _=10
            return False
    return True


for _ in range(int(input())):
    uid = input()
    x = VLENGHT(uid)
    if not x:
        print('Invalid')
        continue
    x = vup(uid)
    if not x:
        print('Invalid')
        continue
    x = vdig(uid)
    if not x:
        print('Invalid')
        continue
    x = valfa(uid)
    if not x:
        print('Invalid')
        continue
    x = vrep(uid)
    if not x:
        print('Invalid')
        continue
    print('Valid')
