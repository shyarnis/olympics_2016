import numpy as np


def medal_tally(df):
    
    # drop duplicates subset
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    
    # groupby region and sort by Gold medal
    medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()

    # new column Total
    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']
   
    return medal_tally


def country_year_list(df):
    # Year
    years_played = df['Year'].unique().tolist()
    years_played.sort()
    years_played.insert(0, "Overall")

    # Country
    countries = np.unique(df['region'].dropna().values).tolist()
    countries.sort()
    countries.insert(0, "Overall")

    return years_played, countries


def fetch_medal_tally(df, year, country):
    # drop duplicates subset
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    temp_df = medal_df 
    if year == "Overall" and country == "Overall":
        temp_df = medal_df
    
    if year == "Overall" and country != "Overall":
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    
    if year != "Overall" and country == "Overall":
        temp_df = medal_df[medal_df['Year'] == int(year)]
    
    if year != "Overall" and country != "Overall":
        temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'] == country)]
        
    if flag == 1:
        # x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
        x = temp_df.groupby('region').sum(numeric_only=True)[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum(numeric_only=True)[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()
    
    x['Total'] = x['Gold'] + x['Silver'] + x['Bronze']

    return x


def participating_nations_over_time(df):
    
    # nations ko values
    # nations_over_time = df.drop_duplicates(['Year', 'region'])['Year'].value_counts().reset_index().sort_values('Year')
    
    # renaming columns name
    # nations_over_time.rename(columns={'Year': 'Edition', 'count': 'No of Countries'}, inplace=True)
    # return nations_over_time
    # ValueError: Value of 'y' is not the name of a column in 'data_frame'. Expected one of ['index', 'Edition'] but received: No of Countries

    # from video
    nations_over_time = df.drop_duplicates(['Year', 'region'])['Year'].value_counts().reset_index().sort_values('index')
    nations_over_time.rename(columns={'index': 'Edition', 'Year': 'No of Countries'}, inplace=True)
    return nations_over_time

