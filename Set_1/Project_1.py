# # Write your code here
# Cleaner = 850
# Vendor = 1120
# Manager = 1300
# Loader = 900
# stuff_salary = Cleaner + Vendor + Manager + Loader
# #Expenses
# Electricity = 100
# Municipal_service = 90
# Security = 30
# total_exp = Electricity + Municipal_service + Security

ear_bubblegum = 202
ear_toffee = 118
ear_ice_cream = 2250
ear_milk_choco = 1680
ear_doughnut = 1075
ear_pancake = 80
currency = "$"
ear_total = float(ear_bubblegum + ear_toffee + ear_ice_cream + ear_milk_choco + ear_doughnut + ear_pancake)
print("Earned amount:",
        "\nBubblegum: ", currency, ear_bubblegum,
        "\nToffee: ", currency, ear_toffee,
        "\nIce cream: ", currency, ear_ice_cream,
        "\nMilk chocolate: ", currency, ear_milk_choco,
        "\nDoughnut: ", currency, ear_doughnut,
        "\nPancake: ", currency, ear_pancake,
        "\n"
        "Income: ", currency, ear_total)
Staff_exp = float(input("Staff expenses: "))
Other_exp = float(input("Other expenses: "))
print("Net income: $", ear_total - Staff_exp - Other_exp, sep="")


