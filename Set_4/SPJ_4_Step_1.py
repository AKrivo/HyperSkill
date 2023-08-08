# write your code here
store = ''
minlen = 100

while len(store) < minlen:
    print("Print a random string containing 0 or 1:")
    userin = input()
    for i in userin:
        if i.isnumeric():
            if int(i) == 1 or int(i) == 0:
                store += i
    if len(store) < minlen:
        print("Current data length is " + str(len(store)) + ", " + str(minlen - len(store)) + " symbols left")
print("Final data string:")
print(store)
