print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
people = input("How many people to split the bill? ")
tip_p = input("What percentage tip would you like to give? 10, 12 or 15? ")

total = (float(bill) + (float(tip_p) * float(bill) / 100)) / int(people)
print(f"Each person should pay: ${total:.1f}")