print("Welcome to the tip calculator!")
bill = float(input("What was your total bill? $"))
tip = int(input("What percentage tip would you like to give? 5, 10, 12 or 15 "))
people = int(input("How many people to split the bill? "))

bill_with_tip = bill * (1 + tip / 100)
per_person = round(bill_with_tip / people, 2)
print(f"Each person should pay: ${per_person}")
