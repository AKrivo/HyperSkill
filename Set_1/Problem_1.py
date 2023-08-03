# Reading user input
user_input = int(input("Please inter the number from 100 to 999: "))
first_two = user_input // 10
first_one = first_two // 10
second_one = first_two % 10
last_one = user_input % 10
print(first_one + second_one + last_one)
