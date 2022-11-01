# Election 2020 Streamlit Dashboard
![App screenshot](https://i.imgur.com/sIh5zS8.png)

Exploring application creation with Streamlit and SQLite. The data is from FiveThirtyEight's [repo](https://raw.githubusercontent.com/bconnor17/2020-Presidential-Election-Data/master/presidential_poll_averages_2020.csv). Using an embedded database like SQLite makes sense with Streamlit since the entire point is speed/simplicity and it can be created in minutes. At the same time, the local database(s) can be regularly updated to support more data sets and additional visualizations without having to gather the data from disparate sources all the time.

## Requirements
- [Streamlit](https://pypi.org/project/streamlit/)
- [SQLite](https://www.sqlite.org/about.html)
- [Pandas](https://pypi.org/project/pandas/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Plotly](https://pypi.org/project/plotly/)

## How to Run
Any Streamlit app can be run locally via CLI `streamlit run app.py` or deployed via [other methods](https://discuss.streamlit.io/t/streamlit-deployment-guide-wiki/5099).
