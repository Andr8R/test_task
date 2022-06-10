"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""


# TODO Import the necessary libraries
import pandas as pd
import numpy as np

# TODO Import the dataset 
path = r'./data/weather_dataset.data'
pd.read_csv(path, sep='\s+')

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index
data = pd.read_csv(path, sep='\s+')
data["Date"] = pd.to_datetime(data[["Yr","Mo","Dy"]].astype(str).agg('-'.join, axis=1))
data = data.drop(columns=["Yr","Mo","Dy"])
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(data["Date"])

# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them
data = data.replace(',','.', regex=True)
data.loc[:, data.columns!='Date'] = data.loc[:, data.columns!='Date'].apply(pd.to_numeric, errors='coerce')
def filter_false(row):
    # filter out enormal huge values or negative ones
    return row.where(row.between(0.001,100))
data.loc[:, data.columns!='Date'] = data.loc[:, data.columns!='Date'].apply(filter_false)

# TODO Write a function in order to fix date (this relate only to the year info) and apply it
data["Date"] = np.where( pd.DatetimeIndex(data["Date"]).year < 2000, data.Date, data.Date - pd.offsets.DateOffset(years=100) )

# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]
data = data.set_index("Date")
data.index.astype("datetime64[ns]")
print("Displaying fixed data...")
print(data.head(10))

# TODO Compute how many values are missing for each location over the entire record
print(f"\nTotal number of missing values:")
print(data.isna().sum().sum())

# TODO Compute how many non-missing values there are in total
print(f"\nTotal number of non-missing values:")
print(data.count().sum())

# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times
print(f"\nMean windspeeds:")
print(data.mean().mean())

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
def calculate_stats(loc):
    stats = [loc.min(), loc.max(), loc.mean(), loc.std()]
    return pd.Series(stats, index=["min","max","mean","std"])
loc_stats = data.apply(calculate_stats)
print(f"\nDisplaying stats for each location:")
print(loc_stats)

# TODO Find the average windspeed in January for each location
print(f"\nMean windspeed in January for each location:")
print(data[data.index.month == 1].mean())

# TODO Downsample the record to a yearly frequency for each location
print(f"\nDownsampled to a yearly frequency:")
print(data.resample('A').mean().head(10))

# TODO Downsample the record to a monthly frequency for each location
print(f"\nDownsampled to a monthly frequency:")
print(data.resample('M').mean().head(10))

# TODO Downsample the record to a weekly frequency for each location
print(f"\nDownsampled to a weekly frequency:")
print(data.resample('W').mean().head(10))

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks
first_weeks = data[data.index.year == 1961].resample('W').mean()[1:22]
weekly_stats = first_weeks.apply(calculate_stats, axis = 1)
print(f"\nDisplaying stats for the first 21 weeks:")
print(weekly_stats)
