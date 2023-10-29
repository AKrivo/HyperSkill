# write your code here
import random
store = ''
minlen = 100
print("Please provide AI some data to learn...")
print("The current data length is " + str(len(store)) + ", " + str(minlen - len(store)) + " symbols left")
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
triads = ["000", "001", "010", "011", "100", "101", "110", "111"]
k = 0
results = dict.fromkeys(triads, [0, 0])
while k < len(triads):
    x = 0
    y = 0
    i = 0
    newstring = store
    t = len(newstring)
    while i < t - 3:
        if newstring[0:3] == triads[k]:
            if newstring[3] == "0":
                x += 1
                results[triads[k]] = [x, y]
            if newstring[3] == "1":
                y += 1
                results[triads[k]] = [x, y]
        newstring = newstring[1:]
        i += 1
    k += 1
# for i in results:
#     print(str(i) + ": " + str(",".join([str(item)for item in results[i]])))
prob = dict.fromkeys(triads, [0, 0])
for key in results:
    values = results[key]
    prob1 = values[0] / (values[0] + values[1])
    prob2 = values[1] / (values[0] + values[1])
    prob[key] = [prob1, prob2]

money = 1000
print("You have $" + str(money) + ". Every time the system successfully predicts your next press, you lose $1.")
print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')
stop = 0
while money > 0 and stop != 1:
    #Playng the game
    game_userin = ""
    passed = 0
    while passed == 0:
        print("Print a random string containing 0 or 1:")
        game_userin = input()
        if game_userin == "enough":
            stop = 1
            break
        game_string = ""
        for s in game_userin:
            if s.isnumeric():
                if int(s) == 1 or int(s) == 0:
                    game_string += s
        if len(game_string) >= 4:
            passed = 1
    if stop == 1:
        break
    firtsthree = ""
    while len(firtsthree) != 3:
        t = str(random.randrange(2))
        firtsthree += t
    finalstring = firtsthree
    test = game_string[3:]
    for s in test:
        if len(test) > 3:
            for key in prob:
                add = ""
                if test[0:3] == key:
                    q = prob[key]
                    if q[0] > q[1]:
                        add = str(0)
                    elif q[1] > q[0]:
                        add = str(1)
                    else:
                        add = str(random.randrange(2))
                    finalstring += add
                    test = test[1:]
                    break
    count = 0
    nice = 0
    for s in game_string[3:]:
        if game_string[count+3] == finalstring[count]:
            nice += 1
        count += 1
    totall = len(finalstring)
    x = totall - nice
    y = nice - x
    money = money - y
    print("predictions:")
    print(finalstring)
    print("Computer guessed " + str(nice) + " out of " + str(len(finalstring))
          + " symbols right " + "(" + str(round((nice/(len(finalstring)) * 100), 2)) + "%)")
    print("Your balance is now $" + str(money))
print("Game over!")
