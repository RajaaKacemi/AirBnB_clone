AirBnB clone - The console
Welcome to the AirBnB clone project
Description of the project :

The hbnb project  is a complete web application, integrating database storage, a back-end API, and front-end interfacing in a clone of AirBnB. The primary objective of this endeavor is to replicate the functionality of the Airbnb website using a server of my own. Upon completion, the project will encompass the following components:

1. A command interpreter designed for data manipulation, The console is a command line interpreter that permits management of the backend of hBnB. It can be used to handle and manipulate all classes utilized by the application.
2. A website featuring both static and dynamic functionalities on the front-end (HTML, CSS).
3. A robust database infrastructure facilitating the management of backend operations.
4. An API serving as a communication bridge between the front-end and backend systems, ensuring seamless interaction and functionality integration.

General concepts in review : 

How to create a Python package.

How to create a command interpreter in Python using the cmd module.

What is Unit testing and how to implement it in a large project.

How to serialize and deserialize a Class.

How to write and read a JSON file.

How to manage datetime.

What is an UUID.

What is *args and how to use it.

What is **kwargs and how to use it.

How to handle named arguments in a function.

Files and Directories:

models: directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
tests: directory will contain all unit tests.
console.py: file is the entry point of our command interpreter.
models/base_model.py: file is the base class of all our models. It contains common elements:
attributes: id, created_at and updated_at
methods: save() and to_json()
models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.




