s = set()
n = int(input())
al = ()
for i in range(1, n):
    s(i)= (input(), end = '')

N = int(input())

for x in range(1, N):
    a, b = input().split()
    if a == 'pop':
        s.pop()
    if a == 'remove':
        s.remove(b)
    if a == 'discard':
        s.discard(b)

print(len(s))