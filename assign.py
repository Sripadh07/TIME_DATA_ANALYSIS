import pandas as pd

# READING DATA FROM CSV FILE
data = pd.read_csv('SBIN_Data.csv')
# TAKING A COLUMN IN THE DATAFRAME WITH TIME
data['TIME'] = pd.to_datetime(data['Time'])

def rank_volume(data):
    # TAKING DATA ACCORDING TO THE DATES
    Duration = data.sort_values(by='Date', ascending=False).head(5)
    # RANKING THE VOLUME COLUMN
    data['Rank'] = Duration['Volume'].rank(ascending=False)
    return data
   
# GROUPING THE DATA ACCORDING TO THE TIME
ranked_data= data.groupby(data['TIME'].dt.time).apply(rank_volume).reset_index(drop=True)
print(ranked_data)

