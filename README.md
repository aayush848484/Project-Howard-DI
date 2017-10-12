

# Diversity Index Project 
Basically, this is a web-application that uses Machine Learning and Data Science algorithms to predict the reliablity of available rankings by comparing different rankings and looking for anomalies in the rankings available. 

## Abstract

The aim of the Diversity Index Project is to provide a rigorous basis for the comparison of the diversity initiatives of different companies.  Currently there are many different rankings of diversity efforts from a variety of organizations. This allows companies to cherry pick the ranking on which they perform well and claim that they are doing better than their peers. The Diversity Index will combine data from all available rankings in a systematic way in order to allow a comparison of different organizations.  Furthermore this will greatly reduce the impact of bias in any individual ranking.


## Getting Started

### NOTE: This project is based on PostgreSQL database hosted locally. So, it will not work until the database is hosted remotely. 

- git clone https://github.com/aayush848484/Project-Howard-DI.git <directory-name>
- cd directory-name
(Create a virtual environment - recommended to avoid clash of different versions of same library).
- virtualenv name-of-virtual-environment
- pip install -r requirements.txt
- python manage.py makemigrations 
- python manage.py runserver

## Tests:

For automated tests, the inbuilt Django test application shall be used. 
NOTE: Need to devise test cases. Haven't done it yet. 

### Built With

- Django 
- PostgreSQL

### Authors

- Dr. Legand Burge 
- Dr. Robert Rwebangira 
- Mr. Aayush Gupta
