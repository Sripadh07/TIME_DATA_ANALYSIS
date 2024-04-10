import pandas as pd

# READING DATA FROM CSV FILE
data = pd.read_csv('SBIN_Data.csv')
# TAKING A COLUMN IN THE DATAFRAME WITH TIME
data['TIME'] = pd.to_datetime(data['Time'])

def rank_volume(data):
    # GETTING THE DATE OF THE CURRENT GROUP
    Initial_date= data['Date'].iloc[0]
    # GETTING THE DATE RANGE FOR THE LAST 5 DAYS
    Duration= pd.date_range(end=Initial_date, periods=5, freq='D')
    # FILTERING THE DATA FOR THE LAST 5 DAYS AND THE SAME TIME AS THE CURRENT DATA
    Duration_data= data[(data['Date'].isin(Duration)) & (data['TIME'].dt.time == data['TIME'].iloc[0].time())] 
    # RANKING VOLUME WITHIN THE LAST 5 DAYS DATA
    data['rank']= data['Volume'].rank(ascending=False)
    return data 


# GROUPING THE DATA ACCORDING TO THE TIME
ranked_data= data.groupby(data['TIME'].dt.time).apply(rank_volume).reset_index(drop=True)
print(ranked_data)

