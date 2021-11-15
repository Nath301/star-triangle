def try_me():
    n = 10
    for x in range(10):
        s = ''
        for y in range(n):
            s += "*"
        n -= 1
        print(s)
