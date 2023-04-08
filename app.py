import pandas as pd
import streamlit as st
import preprocessing
import helper
import plotly.express as px

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
        st.title(str(selected_country) + " overall performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(str(selected_country) + " performance in " + str(selected_year) + " Olympics")
    
    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    # st.dataframe(medal_tally)
    st.table(medal_tally)

# Overall Analysis
if user_menu == "Overall Analysis":
    editions = df['Year'].unique().shape[0] - 1
    cities = df['Year'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title("Top Statistics")
    # col1, col2, col3 = st.beta_columns(3)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)

    with col2:
        st.header("Hosts")
        st.title(cities)

    with col3:
        st.header("Sports")
        st.title(sports)


    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)

    with col2:
        st.header("Nations")
        st.title(nations)
    
    with col3:
        st.header("Atheletes")
        st.title(athletes)

    # participating nations over time
    nations_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nations_over_time, x='Edition', y='region')
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)
    
    # events over time
    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x='Edition', y='Event')
    st.title("Events over the years")
    st.plotly_chart(fig)
    
    # athletes over time
    athletes_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athletes_over_time, x='Edition', y='Name')
    st.title("Athletes over the years")
    st.plotly_chart(fig)

    
