# File:             Data Analysis for Sensors
# Author:           Zeshan Basaran
# Date Created:     2-1-2023

import pandas as pd
import matplotlib.pyplot as plt

# Setting up variables so they're easier to change later (if needed).
fileName = "iGluSnFR4-Data_2023-01-18.csv"   # Only .cvs works with this program.
sensorNameColumn = "ID"
data = "1AP ∆Ffast normalized"
factor = "median"                                       # Ex. mean, median, std, min, max, etc.                                    

# Reading the .csv file, convert to DataFrame
df = pd.read_csv(fileName)

df          # Whole DataFrame
df.head()   # First 5 in DataFrame

df.nlargest(2,[data])     # N largest values
df.nsmallest(2,[data])    # N smallest values

# Grouping values together by Sensor Name - (A,8)(A,9)(A,10)(B,1)(B,6)...
df.sort_values([sensorNameColumn, data], ascending=True).groupby(sensorNameColumn).head(10)

# Provides information about data
# Count, mean, std, min, max, etc.
df[data].describe()
df[data].median()

grouped_df = df.groupby([sensorNameColumn])[data]   # All As, Bs, Cs and so forth are grouped together
grouped_df.describe()                               # Data information given about each sensor seperately
grouped_df.median()                                 # Median of each sensor. In order of sensors

dataInfo = grouped_df.median().reset_index()                    # Moves "Sensor Name" back as column title
sortedDataInfo = dataInfo.sort_values(data, ascending=False)    # Data sorted by highest mean -> lowest mean
sortedDataInfo                                                  # Display the sorted data

sortedDataInfo.head()                       # First/largest 5 in DataFrame
print(sortedDataInfo.nlargest(10,[data]) )  # N largest values

# Graphing Data
# sortedDataInfo is sorted by highest mean -> lowest mean
# Use dataInfo for alphabetical graph A -> Z
sensorNameColumn = [str(ID) for ID in sortedDataInfo[sensorNameColumn]]     # Convert to string for graph
plt.bar(sensorNameColumn, sortedDataInfo.sort_values(data, ascending=True)[data])
 
# Title to the plot
plt.title("Sensors and their Median Value")
 
# Adding axis labels
plt.xlabel("Sensors")
plt.ylabel("Median 1AP ∆Ffast normalized")

# Adding the legends
plt.legend(["Sensors"])
plt.show()

# Exporting data
# sortedDataInfo.to_csv('C:/Users/zesha/OneDrive/Desktop/TestExport.csv')
# sortedDataInfo.to_excel('C:/Users/zesha/OneDrive/Desktop/TestExport.xlsx')
