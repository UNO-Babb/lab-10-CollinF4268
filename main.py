# MapPlot.py
# Name: Collin Frederick
# Date: 2025-04-20
# Assignment: Lab 10 - Matplotlib Visualization

import matplotlib.pyplot as plt
import pandas as pd
import billionaires  # Make sure this file is uploaded in the same folder

# Step 1 – Load the data
data = billionaires.get_billionaire()

# Step 2 – Clean the data
clean_data = [
    person for person in data
    if person["demographics"].get("age") is not None and person["wealth"].get("worth in billions", 0) > 0
]

# Step 3 – Bar Chart: Number of Billionaires by Industry
industry_counts = {}
for person in clean_data:
    industry = person["wealth"]["how"]["industry"]
    industry_counts[industry] = industry_counts.get(industry, 0) + 1

# Convert to DataFrame
df = pd.DataFrame(list(industry_counts.items()), columns=["Industry", "Count"])
df.sort_values(by="Count", ascending=False, inplace=True)

# Plot Bar Chart
plt.figure(figsize=(12, 6))
plt.bar(df["Industry"], df["Count"])
plt.xticks(rotation=45, ha="right")
plt.title("Number of Billionaires by Industry")
plt.xlabel("Industry")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("billionaire_industries.png")
print("Bar chart saved as 'billionaire_industries.png'")

# Step 4 – Scatter Plot: Age vs Net Worth (Filtered)
ages = []
net_worths = []

for person in clean_data:
    age = person["demographics"].get("age")
    worth = person["wealth"].get("worth in billions")
    if age is not None and worth is not None and age >= 25:
        ages.append(age)
        net_worths.append(worth)

# Plot Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(ages, net_worths, alpha=0.6)
plt.xlim(25, 100)  # Focus on realistic age range
plt.title("Billionaire Age vs Net Worth (Ages 25+)")
plt.xlabel("Age")
plt.ylabel("Net Worth (Billions)")
plt.tight_layout()
plt.savefig("age_vs_wealth.png")
print("Scatter plot saved as 'age_vs_wealth.png'")

# Step 5 – Explanation
# ---
# This bar chart shows the number of billionaires across different industries.
# It helps visualize which sectors have produced the most wealth among billionaires.
# From the chart, we see that technology and finance lead in billionaire count.

# The scatter plot shows the relationship between a billionaire’s age and their net worth.
# Filtering out entries under age 25 makes the data more realistic and removes noise.
# The plot shows a wide spread of net worths among ages 30–80, with no clear trend,
# but a noticeable cluster around ages 50–70.
