import pandas as pd 
import sqlite3

poll_avg = pd.read_csv('https://raw.githubusercontent.com/bconnor17/2020-Presidential-Election-Data/master/presidential_poll_averages_2020.csv')

poll_avg = poll_avg.drop('cycle', axis=1, inplace=True)
poll_avg = poll_avg[poll_avg['candidate_name'].str.contains('Convention Bounce for Joseph R. Biden Jr.') == False]
poll_avg = poll_avg[poll_avg['candidate_name'].str.contains('Convention Bounce for Donald Trump') == False]

cnxn = sqlite3.connect('election_2020.db')
c = cnxn.cursor()

c.execute('''
          CREATE TABLE state_averages (
          id INTEGER PRIMARY KEY,
          state TEXT NOT NULL,
          modeldate TEXT NOT NULL,
          candidate_name TEXT NOT NULL,
          pct_estimate REAL NOT NULL,
          pct_trend_adjusted REAL NOT NULL
          )
          ''')

poll_avg.to_sql('state_averages', cnxn, if_exists='append', index=False)

cnxn.close()
