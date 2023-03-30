# Capstone Project #
## Edgardo Alvarez ##

The project's main objective is to build a dashboard to help data visualization. In order to do so, it was first needed to fully understand and clean the dataset, deploy a database (in this case in MySQL). Then build a back-end service for the API that fetches the data from the SQL database stored in the cloud and finally, a front-end developed in streamlit that displays KPIs, charts and tables.

This project cointains 3 main parts:
1. Database
    - Developed with Pandas in a Jupyter Notebook
    - To reduce query times KPI tables were included.
    - Uploaded the tables to a MySQL database in Google Cloud

2. API
    - Developed with Flash-RestX
    - Connected to MySQL database in Google Cloud
    - Deployed in APP Engine (Google Cloud)

3. Front-End
    - Developed using Streamlit
    - Deployed in APP Engine (Google Cloud)
    - App Engine does not recognize Streamlit 1.20.0, therefore some changes had to be done to the Front-End when deploying (pie chart was replaced by a table)

    link to frontend: https://frontend-dot-plucky-pointer-375715.ue.r.appspot.com/
    link to API: https://api-dot-plucky-pointer-375715.ue.r.appspot.com/
