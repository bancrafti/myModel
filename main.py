import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "/home/waribu/workspace/myModel/CovidDeaths.csv"
covid_data = pd.read_csv(file_path)

# Convert date column to datetime format for easier time-based analysis
covid_data["date"] = pd.to_datetime(covid_data["date"])

# Aggregate data by date and continent to analyze trends
daily_trends = (
    covid_data.groupby(["date", "continent"])
    .agg({"new_cases": "sum", "new_deaths": "sum"})
    .reset_index()
)

# Plot daily new cases and deaths by continent
fig, ax = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Plot new cases
for continent in daily_trends["continent"].dropna().unique():
    continent_data = daily_trends[daily_trends["continent"] == continent]
    ax[0].plot(continent_data["date"], continent_data["new_cases"], label=continent)

ax[0].set_title("Daily New COVID-19 Cases by Continent")
ax[0].set_ylabel("New Cases")
ax[0].legend()

# Plot new deaths
for continent in daily_trends["continent"].dropna().unique():
    continent_data = daily_trends[daily_trends["continent"] == continent]
    ax[1].plot(continent_data["date"], continent_data["new_deaths"], label=continent)

ax[1].set_title("Daily New COVID-19 Deaths by Continent")
ax[1].set_ylabel("New Deaths")
ax[1].set_xlabel("Date")
ax[1].legend()

# Save the plot as a .png file
# Save the plot as a .png file in the current directory
plt.tight_layout()
plt.savefig("covid_trends_by_continent.png")
