Omkar Account Generator
=======================

Omkar Account Generator provides a convenient solution for creating
accounts. It is particularly useful for automated tasks that require
account creation in selenium.

Getting Started
---------------

To get started with Omkar Account Generator install
``omkar-account-generator`` using the following command:

.. code:: bash

   python -m pip install omkar-account-generator

Usage
-----

1. ``generate_account(gender, country)``

Generates an account

**Arguments**

-  ``gender`` (optional): The gender of the user account to generate.
   Value can be ``Gender.MEN``, ``Gender.WOMEN``, ``Gender.BOTH``.
   Default’s to ``Gender.BOTH``
-  ``country`` (optional): The country of the user account to generate.
   It accepts a value from the ``Country`` enum. The default value is
   ``None``, which means the country can be any country.

**Example**

.. code:: python

   from omkar_account_generator import AccountGenerator, Gender, Country

   account = AccountGenerator.generate_account(gender = Gender.WOMEN, country=Country.IN)
   print(account)

**Output**

.. code:: json

   {
       "name": "Vibha Almeida",
       "username": "vibhaalmeida",
       "email": "vibha.almeida@gmail.com",
       "password": "letter16",
       "profile_picture": "https://randomuser.me/api/portraits/women/81.jpg",
       "phone": "9217029568",
       "address": "7492, Ratha Bheedi, Thanjavur, Tripura, India",
       "gender": "female",
       "country": "IN",
       "dob": {
           "date": "1992-07-29T22:51:53.073Z",
           "age": 30
       }
   }

2. ``generate_accounts(n, gender, country)``

Generates multiple user accounts.

**Arguments**

-  ``n``: The number of user accounts to generate.
-  ``gender`` (optional): The gender of the user account to generate.
   Value can be ``Gender.MEN``, ``Gender.WOMEN``, ``Gender.BOTH``.
   Default’s to ``Gender.BOTH``
-  ``country`` (optional): The country of the user account to generate.
   It accepts a value from the ``Country`` enum. The default value is
   ``None``, which means the country can be any country.

**Example**

.. code:: python

   from omkar_account_generator import AccountGenerator, Gender, Country

   accounts = AccountGenerator.generate_accounts(3, gender = Gender.WOMEN, country=Country.IN)
   print(accounts)

**Output**

.. code:: json

   [
       {
           "name": "Sahana Nayak",
           "username": "sahananayak",
           "email": "sahana.nayak@gmail.com",
           "password": "vietnam6",
           "profile_picture": "https://randomuser.me/api/portraits/women/35.jpg",
           "phone": "8679648937",
           "address": "424, Naiduthota, Khammam, Uttar Pradesh, India",
           "gender": "female",
           "country": "IN",
           "dob": {
               "date": "1997-10-03T07:38:31.090Z",
               "age": 25
           }
       },
       {
           "name": "Madhura Shroff",
           "username": "madhurashroff",
           "email": "madhura.shroff@gmail.com",
           "password": "bettina1",
           "profile_picture": "https://randomuser.me/api/portraits/women/87.jpg",
           "phone": "8738692847",
           "address": "5106, Maharanipeta, Mehsana, Maharashtra, India",
           "gender": "female",
           "country": "IN",
           "dob": {
               "date": "1989-08-15T05:10:47.967Z",
               "age": 33
           }
       },
       {
           "name": "Hetal Kavser",
           "username": "hetalkavser",
           "email": "hetal.kavser@gmail.com",
           "password": "django27",
           "profile_picture": "https://randomuser.me/api/portraits/women/94.jpg",
           "phone": "8033453360",
           "address": "5222, Colaba Causeway, Buxar, Daman and Diu, India",
           "gender": "female",
           "country": "IN",
           "dob": {
               "date": "1961-05-29T07:35:50.196Z",
               "age": 62
           }
       }
   ]

If my code helped you in creating accounts, please take a moment to `star the repository <https://github.com/omkarcloud/omkar-account-generator>`__. Your act of starring will help developers in discovering our Repository and contribute towards helping fellow developers in their account creation tasks. Dhanyawad 🙏! Vande Mataram!
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
