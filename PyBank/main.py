import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")


budget_data = []


with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]), "change": 0})

total_months = len(budget_data)

previous_amount = budget_data[0]["amount"]
for i in range(total_months):
    budget_data[i]["change"] = budget_data[i]["amount"] - previous_amount
    prev_amount = budget_data[i]["amount"]

total_amount = sum(row["amount"] for row in budget_data)

total_change = sum(row["change"] for row in budget_data)

average = round(total_change / (total_months-1), 2)

greatest_increase = max(budget_data, key=lambda x:x["change"])
greatest_decrease = min(budget_data, key=lambda x:x["change"])

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {greatest_increase['month']}(${greatest_increase['change']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['month']}(${greatest_decrease['change']})")




csvpath = os.path.join("analysis")
with open(csvpath, "w") as text_file:
    print("Financial Analysis", file = text_file)
    print("---------------------------", file = text_file)
    print(f"Total Months: {total_months}", file = text_file)
    print(f"Total: ${total_amount}", file = text_file)
    print(f"Average Change: ${average}", file = text_file)
    print(f"Greatest Increase in Profits: {greatest_increase['month']}(${greatest_increase['change']})", file = text_file)
    print(f"Greatest Decrease in Profits: {greatest_decrease['month']}(${greatest_decrease['change']})", file = text_file)



