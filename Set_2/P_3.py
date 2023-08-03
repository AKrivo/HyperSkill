# Save the input in this variable
ticket = input()

# Add up the digits for each half
half1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
half2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
print(half1, half2)
