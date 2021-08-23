for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a // b)

    except ValueError as k:
        print("Error Code:", k)

    except ZeroDivisionError as e:
        print("Error Code:", e)
