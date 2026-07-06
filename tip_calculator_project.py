print("Welcome to the Tip Calculator!")

#Get the total bill amount
total_bill = float(input("What was the total bill? $"))

#Get the tip percentage
tip_percentage = float(input("How much tip would you like to give? 10, 12, 0r 15? "))

#Get the number of people to split the bill
number_of_people = int(input("How  many people to split the bill? "))

#Calculate the tip amount
tip_amount = (total_bill * (tip_percentage / 100))

# calculate the total bill including tip
bill_for_each = (total_bill + tip_amount) / number_of_people

print(f"Each person pay: ${bill_for_each:.2f}")
