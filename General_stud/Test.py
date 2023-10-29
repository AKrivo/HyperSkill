mystring = "01010010010001010100100101001001101000110010101010101111010010010110100101101010100110101010101010001110011"
triads = ["000", "001", "010", "011", "100", "101", "110", "111"]
k = 0
results = dict.fromkeys(triads, [0, 0])
while k < len(triads):
    x = 0
    y = 0
    i = 0
    newstring = mystring
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
    print(results)
for i in results:
    print(str(i) + ": " + str(",".join([str(item)for item in results[i]])))
