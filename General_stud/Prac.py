a = 1
b = 2
c = 3
e = 4
f = 5
g = 6

# True and-expressions return the result of the last operation:
print(b + c * f >= e and (f + g) * c)  # (17 >= 4 is True) and 33 -> 33
print((f + g) * c and b + c * f >= e)  # 33 and (17 >= 4 is True) -- > True
