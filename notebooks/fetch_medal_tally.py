def fetch_medal_tally(year, country):
    
    if year == "Overall" and country == "Overall":
        medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    
    if year == "Overall" and country != "Overall":
        pass
    
    if year != "Overall" and coutnry == "Overall":
        pass
    
    if year != "Overall" and coutnry != "Overall":
        pass
