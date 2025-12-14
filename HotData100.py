import pandas as pd 
import datetime
import streamlit as st
import plotly.express as px

if st.session_state.get('frames'):
    frames = st.session_state.frames
else:
    frames = pd.read_excel('./Billboard Hot 100 Number Ones Database.xlsx', sheet_name=None)
    st.session_state.frames = frames


df = frames['Data']
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

st.title(":red[Hot] Graph App")
option = st.selectbox(
        "Which column would you prefer?",
        df.columns
)

option2 = st.multiselect(
        "Select Entries to see total weeks at no.1!",
        df[option].unique())
        
mask = df[option].apply(lambda x: x in option2)
st.write(option)
vx = df[mask].groupby('Artist')['Weeks at Number One'].sum()
vx

fig = px.bar(df[mask], 
            x='Artist',
            y='Weeks at Number One', 
            color= 'Artist',
            title='Billboard HotGraph')
st.plotly_chart(fig)
