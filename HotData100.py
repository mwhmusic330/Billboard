import pandas as pd 
import streamlit as st
import plotly.express as px

if st.session_state.get('frames'):
    frames = st.session_state.frames
else:
    frames = pd.read_excel('./Billboard Hot 100 Number Ones Database.xlsx', sheet_name=None)
    st.session_state.frames = frames

##### frames = pd.read_excel('./Billboard Hot 100 Number Ones Database.xlsx', sheet_name=None)
df = frames['Data']
maska = df['Weeks at Number One'] == 13
maskb = df['Weeks at Number One'] > 5 
maskc = df['Artist'] == 'Michael Jackson'
maskd = df['Song'] == 'Not Like Us'
mask = maska | maskb
#### print(frames['Data Dictionary']['Category'].value_counts())
#### print(df['Weeks at Number One'].value_counts())

st.title(":red[Hot] Graph App")
option = st.selectbox(
        "Which column would you prefer?",
        df.columns
)

option2 = st.multiselect(
        "Select Entries to see total weeks at no.1!",
        df[option])
        
mask = df[option].apply(lambda x: x in option2)
st.write(option)
st.write(option2)
mask
df[mask]
#### vx = df[option].value_counts().reset_index()
#### fig = px.bar(vx, 
             #### x=option,
             #### y='count', 
             #### title='Billboard HotGraph')
#### st.plotly_chart(fig)
