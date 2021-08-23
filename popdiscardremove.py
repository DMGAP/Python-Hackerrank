n = int(input())
s = set(map(int, input().split()))
N = int(input())
for x in range(N):
    eval('s.{0}({1})'.format(*input().split() + ['']))
print(sum(s))