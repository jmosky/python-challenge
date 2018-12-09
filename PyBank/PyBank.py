
# coding: utf-8

# # PyBank homework.
# 
# This notebook pertains to the PyBank directory in the python-challenge repo.
# 
# 
# My questions for you all start with `# TUTOR:`. Here they are in summary form:
# 
# * How do I format the output of `df.describe()` to suppress scientific notation while also not changing the settings for all columns of each type?
# 
# * How do I format the output of `.sum()` as currency? And why is the code I've written to conver to currency not working? See code below for more detail.

# In[184]:


# Import packages.

import pandas as pd

# Import csv as dataframe.
df = pd.read_csv("Resources/budget_data.csv")
df["MoM Change"] = df["Profit/Losses"].diff()


# In[185]:


df.head()


# In[186]:


# TUTOR: How to suppress scientific notation?

df.describe()


# In[182]:


# TUTOR: How to format as currency? 
#df["Profit/Losses"].sum()

# This is what I've tried and it fails:
df["Profit/Losses"] = df['Profit/Losses'].astype("float").map('${:,.2f}'.format)


# In[187]:


# TUTOR: And why does this show no output at all if the the line above fails?
# It only shows errors if I actually run the code in the preceding box.

for i, item in enumerate(df['Profit/Losses']):
   try:
      df['Profit/Losses'].astype("float").map('${:,.2f}'.format)
   except ValueError:
      print('ERROR at index {}: {!r}'.format(i, item))


# In[167]:


import pandas as pd
df = pd.read_csv("Resources/budget_data.csv")

df["MoM Change"] = df["Profit/Losses"].diff()

# The greatest decrease in losses (date and amount) over the entire period

# TUTOR: How to select entire row corresponding to the min value shown using the methods below?
# Tried: df[df["Profit/Losses"].diff().min()]
# df["Profit/Losses"].diff().min()

df.loc[df["MoM Change"].idxmin()]


# In[188]:


# Now put it all together and output the following to CSV (assuming first two rows are not to be in the output):

# Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)

import pandas as pd
df = pd.read_csv("Resources/budget_data.csv")

df["MoM Change"] = df["Profit/Losses"].diff()

total_months = df["Date"].nunique()
total = df["Profit/Losses"].sum()
avg_change = df["MoM Change"].mean()
inc_profits = df.loc[df["MoM Change"].idxmax()]
dec_profits = df.loc[df["MoM Change"].idxmin()]

calcs = {
    'Metric': ["Total Months:", "Total:", "Average  Change:", "Greatest Increase in Profits:", "Greatest Decrease in Profits:"],
    'Month (where applicable)': ['','','',inc_profits["Date"], dec_profits["Date"]],
    'Values': [total_months, total, avg_change, inc_profits["MoM Change"], dec_profits["MoM Change"]]
}
output = pd.DataFrame(data=calcs)
output.to_csv('pybank_output.csv', index = False, header=None)


# In[189]:


print(output)

# How would I go about putting the month-year and value in the same column?
# I tried .concat() and it did not work.

