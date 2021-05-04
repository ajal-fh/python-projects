#Day2: Tip calculator project

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

#check wether the tip percent is valid
while(tip_percent not in [10,12,15]):
    print("invalid tip percentage. Aborting")
    tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

no_of_people = int(input("How many people to split the bill? "))

#total amount the group has to pay after including the tip
bill_with_tip = total_bill + tip_percent * total_bill * 0.01

amount_per_person = round( bill_with_tip
    / no_of_people,2)

print("Each person should pay: ${}".format(amount_per_person))
