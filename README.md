## Pyramid-REST-API

**UPDATE: This is a fairly old project, and this doesn't reflect how i would make an api now. You can look at it, but just know it's not exactly a good example.**

This is a simple REST-API to manage users in a database.

## Getting Started

These instructions should get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* [A Postgres database](https://www.postgresql.org/download/) - To store users

Installation:
* Download Postgres and install it, remember the password you entered during installation.
* Create a server and connect to it.
* Create the database, with the desired name.
* For the table, [this script can be used](https://drive.google.com/file/d/1UA5GlL0j_CTlhi5HV7ZVjSf_aqsLc6Ef/view?usp=sharing).

Filling the database with dummy data in advance is optional.
### Installing

* Clone the project from this repository into your desired directory.
* Create a filled called "config.txt" in the same directory. This will be used to connect to your database. Fill in the content inside the {}:
```
[configuration]
password = postgresql://postgres:{postgres password}@localhost:{port number}/{database name}
```
Install the required packages if asked for. A requirement.txt file has been provided, but in case this doesn't work, install these packages via pip:
* pyramid
* SQLAlchemy
* psycopg2

If you can't get this to work either, [here's the full project with packages installed](https://drive.google.com/file/d/1v77p2Mi1Swzhvldsh86mwkQCBHg47ndX/view?usp=sharing).

## Running

Simply run main.py to start up the server. You can now send requests as you like.

## Endpoints

**Request method = GET**
```
/
```
You'll end up here by default if no endpoint is specified. This will simply return a welcome message.

```
/users
```
This returns all the users currently in your database, in JSON format.

```
/user/{email}
```
This returns a specific user, Fill in the email in the {} to enter an user.

**Request method = POST**
```
/user
```
This way you can create a new user. Valid JSON is required in the request body. Here's an example of how it should look like.
```
{
  "email": "henk@hotmail.nl",
  "name": "Henk"
}
```

**Request method = DELETE**
```
/user/{email}
```
This way you can delete an user from the database. Fill in the email in the {} to enter an user.

**Request method = PATCH**
```
/user/{email}
```
This way you can edit the name and e-mail of an user. Fill in the email in the {} to enter an user. TValid JSON is required in the request body. Here's an example of how it could look like:
```
{
  "name": "Henk"
}
```

## Built With

* [Pyramid](https://trypyramid.com/) - Python web framework
* [SQLAlchemy](https://www.sqlalchemy.org/) - SQL Toolkit
* [Psycopg2](http://initd.org/psycopg/) - Postgres database adapter
