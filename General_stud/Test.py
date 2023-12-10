number = 70e9

# Determine the exponent in the scientific notation
exponent = int(str(number).split("e")[1])

# Convert the number to a string in the desired format
formatted_number = "{:.0f} * 10^{}".format(number / 10**exponent, exponent)

print(formatted_number)