print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12 or 15? "))
number = int(input("How many people to split the bill? "))

split = 150(total+(total*tip)/100)/number
final = "{:.2f}".format(split)
print(f"Each person should pay: ${final}")
