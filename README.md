# Election 2020 Streamlit Dashboard
![App screenshot](https://i.imgur.com/sIh5zS8.png)

Exploring application creation with Streamlit and SQLite. The data is from FiveThirtyEight's [repo](https://raw.githubusercontent.com/bconnor17/2020-Presidential-Election-Data/master/presidential_poll_averages_2020.csv). Using an embedded database like SQLite makes sense with Streamlit since the entire point is speed/simplicity (current iteration took about less than an hour to make from scratch). At the same time, the local database file(s) can be regularly updated to support more data sets which power additional visualizations in a multi-page application without the app having to pre-process the data constantly.

## Requirements
- [Streamlit](https://pypi.org/project/streamlit/)
- [SQLite](https://www.sqlite.org/about.html)
- [Pandas](https://pypi.org/project/pandas/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Plotly](https://pypi.org/project/plotly/)
