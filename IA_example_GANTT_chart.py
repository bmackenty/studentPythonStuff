import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime, timedelta

# Define the tasks and their start/end dates
tasks = {
    "Task": [
        "Study Perlin noise theory and procedural generation techniques",
        "Explore Python libraries for noise generation and visualization",
        "Design the custom Perlin noise algorithm",
        "Implement the algorithm in Python",
        "Develop smooth transitions between terrain features",
        "Research visualization methods for 2D and 3D terrain maps",
        "Implement heatmap visualization using matplotlib",
        "Implement 3D plot visualization using plotly",
        "Optimize the algorithm for performance",
        "Conduct performance benchmarks and profile the code",
        "Test the algorithm for accuracy, variety, and reproducibility",
        "Validate the visual representation of the terrain",
        "Compile and analyze results",
        "Write the IA report"
    ],

    "Start": [
        "2023-07-01", "2023-07-05", "2023-07-12", "2023-07-18", "2023-07-25", 
        "2023-07-29", "2023-08-03", "2023-08-10", "2023-08-14", "2023-08-19",
        "2023-08-23", "2023-08-30", "2023-09-04", "2023-09-12"
    ],
    "End": [
        "2023-07-10", "2023-07-14", "2023-07-21", "2023-07-28", "2023-08-04", 
        "2023-08-11", "2023-08-15", "2023-08-22", "2023-08-26", "2023-09-01",
        "2023-09-08", "2023-09-15", "2023-09-29", "2023-10-16"
    ]





}

# Create a DataFrame
df = pd.DataFrame(tasks)

# Convert start and end dates to datetime
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])

# Plotting the Gantt chart
fig, ax = plt.subplots(figsize=(10, 8))

for idx, row in df.iterrows():
    ax.barh(row['Task'], (row['End'] - row['Start']).days, left=date2num(row['Start']))

ax.set_xlabel('Dates')
ax.set_ylabel('Tasks')
ax.set_title('Gantt Chart for Custom Perlin Noise Algorithm Project')
ax.xaxis_date()

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()
