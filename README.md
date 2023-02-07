# AirBnB Clone

The goal of this project is to deploy on your server a simple copy of the [AirBnB](https://www.airbnb.com/).

## Objectives
By the end of this project, we are expected to understand the following concepts:
- Unittest
- Python Packages
- Serialization/Deserialization
- cmd module
- * args and ** kwargs

## Description of the project
This project is divided into the following sections:
1. The Console
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

2. Web Static
- learn HTML/CSS
- create the HTML of your application
- create template of each object

3. MySQL Storage
- replace the file storage by a Database storage
- map your models to a table in database by using an O.R.M.

4. Web Framework - templating
- create your first web server in Python
- make your static HTML file dynamic by using objects stored in a file or database

5. RESTful API
- expose all your objects stored via a JSON web interface
- manipulate your objects via a RESTful API

6. Web Dynamic
- learn JQuery
- load objects from the client side by using your own RESTful API

## The Console
### How to start the command interpreter
### How to use it
### Examples
