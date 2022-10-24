import pandas as pd
import streamlit as st
import plotly.express as px
import sqlite3
from PIL import Image

st.set_page_config(layout='wide')

cnxn = sqlite3.connect('election_2020.db')

@st.cache(allow_output_mutation=True)
def query_to_dataframe():
    query = pd.read_sql('SELECT * FROM state_averages ORDER BY state', cnxn)
    return query

averages = query_to_dataframe()
averages['modeldate'] = pd.to_datetime(averages['modeldate'])

st.title('2020 Presidential Election Polling Averages')

col1, col2 = st.columns(2)

with col1:
    img1 = Image.open('imgs/i_voted1.jpg')
    st.image(img1)

with col2:
    img2 = Image.open('imgs/i_voted2.jpg')
    st.image(img2)

st.header('Time series visualization of polling averages from the 2020 Presidential Election via 538')

state_list = averages['state'].unique()
state = st.selectbox('Select a State:', state_list)

fig = px.line(averages[averages['state'] == state],
              x='modeldate',
              y='pct_estimate',
              color='candidate_name',
              height=800)

fig.update_layout(xaxis_title='Date',
                  yaxis_title='Percent Estimated',
                  legend_title='Candidate')

st.plotly_chart(fig, use_container_width=True)
