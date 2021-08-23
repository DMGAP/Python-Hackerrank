


n, m = input().split()
_ = input().split()
like = set(input().split())
dislike = set(input().split())
print(sum([(i in like)-(i in dislike) for i in _]))