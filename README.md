# Capstone Project #
## Edgardo Alvarez ##

This capstone project focuses on building a data visualization dashboard for H&M. It comprises three main components: a database, an API, and a Streamlit web application. The aim is to create an efficient and user-friendly platform to display KPIs, charts, and tables.

### Main Components ### 

1. Database

    - Developed using Pandas in a Jupyter Notebook.
    - KPI tables were included to reduce query times.
    - The tables were uploaded to a MySQL database hosted on Google Cloud.

2. API

    - Developed using Flask-RESTx.
    - Connected to the MySQL database on Google Cloud.
    - Deployed on App Engine (Google Cloud).

3. Front-End

    - Developed with Streamlit.
    - Deployed on App Engine (Google Cloud).
    - Due to compatibility issues with App Engine, Streamlit version 1.20.0 required some adjustments (the pie chart was replaced by a table).

### Links: ###

- Frontend: https://frontend-dot-plucky-pointer-375715.ue.r.appspot.com/
- API: https://api-dot-plucky-pointer-375715.ue.r.appspot.com/
