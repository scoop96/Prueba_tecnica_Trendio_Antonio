# Prueba_tecnica_Trendio_Antonio
Technical test for Trendio job

To access to the project activate the Venv "Venv_prueba" inside the repository.

    - Django Version : Django-4.2.5
    - Python version : Python 3.8.10
    - GraphQL version: 3.1.5


To populate the database if any error you can use the file 'fill_database.json'  using 'python manage.py loaddata $path/fill_database.json'


This code only has 2 queries to retrive all the cities and all the countries with their cities. And 2 mutations to update or create a new city or country.

Testing might be added to avoid using manual Rest petitions.

In the file 'graphql.txt' there is an example of each one of them.
First run the server using the command 'python manage.py runserver'. The app works in localhost in the port 8000.