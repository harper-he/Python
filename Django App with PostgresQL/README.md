This is one of the hardest aspects of data science project I have ever done. It didn't involve analysis, but trying to make the backend of data science work. 

In this project, I built a Django app with a Relational Database Management System (RDBMS), PostgresQL.

Django is a high level full-stack open-source web framework written in Python, that encourages rapid development and clean, pragmatic design.

TSG provides a complete guide to online streaming content. It combines many streaming platforms users subscribe to — Netflix, Hulu, etc. — and enables users to browse, search, and watch TV and movies from over 5 services.

This project is built using Django REST Framework to provide the backend API for TSG.

This project contains a Django Rest API. Users are able to signup and login to their account. 

Features
Products API endpoint available at /api/products/.
Custom user authentication using JSON Web Tokens. The API is available at /api/accounts/.
Simple newsletter functionality: superuser can view the list of all subscribers in Django admin panel; any visitor can subscribe. The relevant API endpoint is available at /api/newsletter/.
Stripe payments API endpoint available at /api/payments/.

Main requirements
python 3.5, 3.6, 3.7
Django 2.1.8
PostgreSQL 11.1
This project also uses other packages (see requirements.txt file for details). For instance, tag support is provided by django-taggit and image processing is thanks to Pillow.

URL chekcing
