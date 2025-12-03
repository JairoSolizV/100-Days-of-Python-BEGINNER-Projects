print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill?\n"))
percentage = int(input("What percentage tip would you like to give? 10, 12, o 15?\n"))
people_to_split = int(input("How many people to split the bill?\n"))

total_include_tip = total_bill + (percentage * total_bill) / 100
each_should_pay = round(total_include_tip / people_to_split, 2)

print(f"Each person should pay ${each_should_pay}")