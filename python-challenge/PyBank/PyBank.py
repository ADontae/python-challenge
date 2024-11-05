import os
import csv

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = None  # Track changes
max_increase = float('-inf')  
min_decrease = float('inf')  
max_increase_date = None
min_decrease_date = None
previous_profit_loss = 0
changes = []
dates = []

# Define the relative directory path
script_dir = os.path.dirname(__file__)

# Join the current directory with the relative directory
budget_csv = os.path.join(script_dir, 'Resources/budget_data.csv')

# Open the CSV file in read mode
with open(budget_csv, 'r') as csvfile:
    
# Create a CSV reader object
    csv_reader = csv.reader(csvfile)

# Skip the header row (if present)
    next(csv_reader)

# Process each row after skipping the header
    for row in csv_reader:
        current_profit_loss = float(row[1])
        
        # Calculate total months and profit/loss by counting each line item to get total months
        # and getting the sum of profit/loss in row[1] index
        total_months += 1
        total_profit_loss += current_profit_loss
        
        # Calculate changes in profits/losses   
        if previous_profit_loss != 0:
            change = int(row[1]) - previous_profit_loss
            changes.append(change)
            dates.append(row[0])
        previous_profit_loss = int(row[1])

# Find the greatest increase in profits 
max_increase = max(changes)

# Find the date corresponding to the greatest increase value
max_increase_date = dates[changes.index(max_increase)]

# Find the greatest decrease in profits
min_decrease = min(changes)

# Find the date corresponding to the greatest decrease value
min_decrease_date = dates[changes.index(min_decrease)]

# Calculate average change
average_change = sum(changes) / len(changes)

# set the output variable
output =(
    f"\n Financial Analysis \n"
    f"---------------------------------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss:,.2f}\n"
    f"Average Change: ${average_change:,.2f}\n"
    f"Greatest Increase in Profits: {max_increase_date} (${max_increase:,.2f})\n"
    f"Greatest Decrease in Profits: {min_decrease_date} (${min_decrease:,.2f})\n"
    )
    

# Print out the results

print(output)
# Define the relative directory path
outputfile = os.path.join("Analysis.txt")

# Join the current directory with the relative directory
analysis = os.path.join("analysis.txt")

# Write the results into the PyBank Financial Analysis.txt file
with open(analysis, "w") as txtfile:
    txtfile.write(output)