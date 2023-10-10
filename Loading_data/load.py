import pandas as pd
import matplotlib.pyplot as plt

# ==========Loading data from csv file=============
my_data = pd.read_excel('medal.xlsx')
df = pd.DataFrame(my_data)
df.head(20)
print("===============Excel file=========")
print(df)
print()
print("+=============Csv file =============+")
df.to_csv('new_medal.csv')
print(df)

# ------------Visualizing using pie chart--------------
"""country = df["Conutry"]
medals = df["Gold_meadls"]
colors = ["red", "green", "cyan", "yellow", "orange"]
explode = (0.1, 0, 0, 0, 0)
plt.pie(medals, labels=country, explode=explode, autopct="%1.1f%%", shadow=True, startangle=140, colors=colors)
plt.title("Gold medal achievement")
plt.show()"""

# ---------------Visualizing using bar chart----------
"""country = df["Conutry"]
medals = df["Gold_meadls"]
plt.bar(country, medals, label="Award", color="c")
plt.plot()
plt.xlabel("country")
plt.ylabel("medals")
plt.title("Gold medals achievement winners")
plt.legend()
plt.show()"""

# ------------------visualizing using a line graph----------
country = df["Conutry"]
medals = df["Gold_meadls"]
plt.plot(country, medals, label="AWARDS", color="g")
plt.plot()
plt.xlabel("Country")
plt.ylabel("Gold_medals")
plt.title("Gold medal achievements winner")
plt.legend()
plt.show()