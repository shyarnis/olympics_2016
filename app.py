import pandas as pd
import streamlit as st
import preprocessing
import helper

# datasets
df = pd.read_csv("./athlete_events.csv")
region_df = pd.read_csv("./noc_regions.csv")

# pre-processing
df = preprocessing.preprocess(df, region_df)


st.sidebar.title("Olympics Analysis")

user_menu = st.sidebar.radio(
    "Select and Option", (
        "Medal Tally",
        "Overall Analysis",
        "Country Wise Analysis",
        "Athelete Wise Analysis"
        )
)

 
# Medal Tally
if user_menu == "Medal Tally":

    st.sidebar.header("Medal Tally")

    years, countries = helper.country_year_list(df)
    
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", countries)


    # dynamic title
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " overall performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
    
    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    # st.dataframe(medal_tally)
    st.table(medal_tally)


# Drop down menu
#   - Year
#   - Country