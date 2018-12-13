import csv

# Open dataset (csv).
with open("Resources/election_data.csv", 'r') as f:
    reader = csv.reader(f)
    next(reader)

    counter = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    error_votes = 0
    winner = ''
    newline = '\n'
    
    for row in reader:
        # Counts total votes. Assumes no duplicates. (?)
        counter += 1
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        elif row[2] == "O'Tooley":
            otooley += 1
        # Confirmed there are no error votes so can delete this.
        else: 
            error_votes += 1
        
        if khan > correy:
            winner = "Khan"
        elif correy > li:
            winner = "Correy"
        elif li > otooley:
            winner = "Li"
        else:
            winner = "O'Tooley"
            
    khan_pct = '{:.3%}'.format(float(khan/counter))
    correy_pct = '{:.3%}'.format(float(correy/counter))
    li_pct = '{:.3%}'.format(float(li/counter))
    otooley_pct ='{:.3%}'.format(float(otooley/counter))

    text = f'Election Results{newline}-------------------------{newline}Total Votes: {counter}{newline}-------------------------{newline}Khan: {khan_pct} ({khan}){newline}Correy: {correy_pct} ({correy}){newline}Li: {li_pct} ({li}){newline}O\'Tooley: {otooley_pct} ({otooley}){newline}-------------------------{newline}Winner: {winner}{newline}-------------------------'
    f = open('output.txt', 'w')
    f.write(text)
    f.close()
    
    print(text)