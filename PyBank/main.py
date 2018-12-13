# Import packages.
import csv

# Open dataset (csv).
with open("Resources/budget_data.csv", 'r') as f:
    reader = csv.reader(f)
    next(reader)
    
    # Initialize variables needed in loop.
    counter = 0  # This allows me to skip the first row when summing differences.
    total = 0 # This is for summing all profits/losses.
    month_count = 0 # For counting months. 
    diff = 0 # For array of changes in profits/losses.
    previous_amount = 0 # For calculating values to go in diff array.
    max_diff = 0
    min_diff = 0
    max_month = ''
    min_month = ''
    newline = '\n'
    
    for row in reader:
        # Skip the first row, then start calculating the MoM change in profit/losses.
        if counter != 0:
            diff += int(row[1]) - int(previous_amount)
        # If the calculated change is greater than the current max change, store it as the max change.
        if int(row[1]) - int(previous_amount) > max_diff:
            max_diff = int(row[1]) - int(previous_amount)
            max_month = row[0]
        # If the calculated change is less than the current min change, store it as the min change.
        if int(row[1]) - int(previous_amount) < min_diff:
            min_diff = int(row[1]) - int(previous_amount)
            min_month = row[0]
        # Set the current row's profit/losses as the value to compare the next row's profit/losses to.
        previous_amount = row[1]
        # Sum all profit/losses as we loop through each row.
        total += int(row[1])
        # Count how many rows there are so we know the month count.
        month_count += 1
        # This is used in the first line in order to skip calculating a difference in profit/losses for the first row.
        counter += 1
        
    avg_change = "$%.2f" % float(diff /(month_count-1))
        
    text = f'Financial Analysis{newline}----------------------------{newline}Total Months: {month_count}{newline}Total: ${total}{newline}Average Change: {avg_change}{newline}Greatest Increase in Profits: {max_month} (${max_diff}){newline}Greatest Decrease in Profits: {min_month} (${min_diff})'
    
    f = open('output.txt', 'w')
    f.write(text)
    f.close()
    print(text)