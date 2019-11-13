def sqr(c):
    return c ** 2


def plus(a=1, b=2):
    #result = a + b
    #print(result)
    return a + sqr(b)

r = plus(1,3)
print("result: " + str(r))
print(plus(5,7) + 2)
plus()

print(plus(3, 2))

