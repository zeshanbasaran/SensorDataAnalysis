# SensorDataAnalysis
An easy to read, understand, modify, and utilize program created in python to organize data from glutamate sensors collected by the Allen Institute.

iGluSnFR4-Data_2023-01-18.csv is composed of 4441 datapoints collected from the institute.

![image](https://github.com/zeshanbasaran/SensorDataAnalysis/assets/116126778/7a61e282-c7c7-482a-8bbe-2581b6d5e89a)

The entire program is very heavily commented so that researchers unfamilar with python could mutate the program as needed.

```python
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
```

The main problem the researcher was having was that some sensors had multiple recorded datapoints with differing "1AP ∆Ffast normalized" results. When he tried to graph the data using Excel, it would treat every test as a seperate sensor ID. My responsiblity was to implement a solution that would take the median of all results of each ID, and graph the sensors in order from greatest to smallest "1AP ∆Ffast normalized". 

To explore the problem, I started with a more simple test group:

|ID|Data|
|---|---|
|A|10|
|A|10|
|A|9|
|B|1|
|B|2|
|B|1|
|C|1|
|C|10|
|C|5|
|D|1|
|D|10|
|D|5|
|E|3|
|F|6|
|...|...|

I grouped all the sensors together, found the median for each sensor, and sorted them from highest mean to lowest mean.

```python
# Grouping values together by Sensor Name - (A,8)(A,9)(A,10)(B,1)(B,6)...
df.sort_values([sensorNameColumn, data], ascending=True).groupby(sensorNameColumn).head(10)
# ...
grouped_df = df.groupby([sensorNameColumn])[data]   # All As, Bs, Cs and so forth are grouped together
grouped_df.describe()                               # Data information given about each sensor seperately
grouped_df.median()                                 # Median of each sensor. In order of sensors

dataInfo = grouped_df.median().reset_index()                    # Moves "Sensor Name" back as column title
sortedDataInfo = dataInfo.sort_values(data, ascending=False)    # Data sorted by highest mean -> lowest mean
sortedDataInfo                                                  # Display the sorted data

sortedDataInfo.head()                       # First/largest 5 in DataFrame
print(sortedDataInfo.nlargest(10,[data]) )  # N largest values
```

These are the largest 10 for demonstration:

![image](https://github.com/zeshanbasaran/SensorDataAnalysis/assets/116126778/ca82c93d-15ad-4f21-a037-dbd9422eada1)

Next, I plotted and exported the data.

```python
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
sortedDataInfo.to_csv('C:/Users/zesha/OneDrive/Desktop/TestExport.csv')
# sortedDataInfo.to_excel('C:/Users/zesha/OneDrive/Desktop/TestExport.xlsx')
```

![TestFigure](https://github.com/zeshanbasaran/SensorDataAnalysis/assets/116126778/237eae3b-6fad-4bea-90b2-06310c22ee00)

And this is how it turned out for the actual data:

![image](https://github.com/zeshanbasaran/SensorDataAnalysis/assets/116126778/a16ec1b2-4100-4d6f-84e7-d3fe215d4dc4)

![SensorMedians](https://github.com/zeshanbasaran/SensorDataAnalysis/assets/116126778/5bb0a67a-7e31-4084-a235-6c8e931cd270)

## Credits

### Dataset:
- The Allen Institute (Seattle WA)
