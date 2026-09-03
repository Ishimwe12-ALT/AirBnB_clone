# AirBnB clone - The console

## Description

This project is the first step toward building a full clone of the
AirBnB web application. It lays the groundwork for everything that
comes later: a data model, a storage/persistence system, and a command
interpreter used to create, update, and manage that data from the
command line.

At this stage, the project implements:

* BaseModel, the parent class every future model (User, State, City,
  Amenity, Place, Review) will inherit from. It handles a unique id,
  created_at / updated_at timestamps, and conversion to/from a
  dictionary representation.
* FileStorage, a simple JSON-based persistence engine that keeps every
  object in memory and serializes/deserializes them to file.json so
  data survives between runs of the program.
* A full unittest suite covering both of the above.

Later parts of this project will add the remaining model classes and the
interactive command interpreter (console) used to manipulate them.

## The Command Interpreter

### How to start it

Make the console executable and run it directly, or invoke it with
Python:

$ ./console.py

or

$ python3 console.py

Either command drops you into an interactive prompt:

(hbnb)

### How to use it

The console works like a simple shell built on Python's cmd module.
Type a command and press Enter. To leave the console, type quit,
EOF using Ctrl+D, or use the built-in help command to see everything
that's available.

### Examples

$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
help  quit

(hbnb) quit
$

## Requirements / Environment

* Ubuntu 20.04 LTS
* Python 3.8.5
* Style checked with pycodestyle (version 2.8.x)

## Running the tests

$ python3 -m unittest discover tests

## Authors

See the AUTHORS file for the full list of contributors.
