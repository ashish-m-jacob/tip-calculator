print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15\n "))
people = int(input("How many people to split the bill?\n"))

# format() allows you to format numbers to suit your need. Here, the '.2f' means that there will be 2 digits after the decimal point.
final_split = (bill/people) * (1 + tip/100)
print(f"Cost per person: ${round(final_split,2)}")