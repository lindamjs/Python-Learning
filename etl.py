import sqlite3
import pandas as pd 
import datetime
import re
import matplotlib.pyplot as plt

#Connect to DB
conn = sqlite3.connect('process_event_log_Linda_Stanley.db')

#Read database table into a dataframe 
#query = """select * from events"""

query = """with cte as (
select id,
min(case when event = 'START_PROCESSING' then event_timestamp end) as 'event_start_tm',
max(case when event = 'FINISH_PROCESSING' then event_timestamp end) as 'event_end_tm'
from events
group by id
)
select id,
datetime(event_start_tm,'unixepoch') start_tm,
datetime(event_end_tm,'unixepoch') end_tm,
ROUND((JULIANDAY(datetime(event_end_tm,'unixepoch')) - JULIANDAY(datetime(event_start_tm,'unixepoch'))) * 86400) AS difference
FROM cte
"""

#Write resultset into dataframe
df = pd.read_sql_query(query, conn)

#Convert to datetime format
df['start_tm'] = pd.to_datetime(df['start_tm'])
df['end_tm'] = pd.to_datetime(df['end_tm'])

#Normalize to remove timestamp
df['start_tm'] = df['start_tm'].dt.normalize()
df['end_tm'] = df['end_tm'].dt.normalize()
print(df['start_tm'])
print(df['end_tm'])
print(df)

# Extract year month from dates
df['st_year'] = pd.DatetimeIndex(df['start_tm']).year
df['st_month'] = pd.DatetimeIndex(df['start_tm']).month

# Combine the original DataFrame and append the new columns
result_df = pd.concat([df,df['st_year'],df['st_month']],axis = 1)
#print(result_df.head())

#Plotting resultset
print(result_df.head())
result_df.plot(kind='line',x='start_tm',y='difference',color='blue')
plt.show()

#Result indicates spike in processing time between 2023-07 and 2023-08 time priod
