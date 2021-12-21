from functools import reduce


f =lambda a: a*a

print(f(4))




nums = [3, 2, 6, 8, 10, 5, 7]

evens = list(filter(lambda n: n%2==0, nums))

doubles = list(map(lambda n: n*2, evens))

sum = reduce(lambda a, b: a+b, doubles)
print(evens)
print(doubles)
print(sum)