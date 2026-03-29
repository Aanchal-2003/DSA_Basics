def num(n):
    if n > 5:
        return
    print(n)
    num(n+1)
num(1)


def fact(n):
    if (n == 1):
        return 1
    return n*fact(n-1)
print(fact(5))

def num(n):
    if n < 1:
        return
    print(n)
    num(n-1)
num(5)


