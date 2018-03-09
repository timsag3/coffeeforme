coffeeforme (version 1.2)
=========================

This package is a command-line interactive interface for CoffeeForMe cafe workers.
The program supports the compatibility of Python2 and Python3 versions.
Runs on Linux and Windows operating systems.


SETUP (administrator interface)
===============================

 1. When you first time run the program you should login as administrator
    and setup the database. To do that run the program with "-id admin" arguments
    or even without any arguments:

        python main.py -id admin
        python main.py

    and then press "RETURN". The program will show you available commands.
    You need "Create and setup database" command so input "1" key than press "RETURN".
    After that the program creates database with two default tables: "users" and "menu".
    Anytime you need you can clear the database by using "Clear database" command ("2" key)

 2. The "users" table contains nothing so you need to add new users by yourself.
    To do that you need "Add new user" command so input "3" key and follow
    the program instructions.
    Also you can remove users by id using "Remove users" command ("4" key).
    The "Show users" command ("9" key) will show you list of users.

 3. The "menu" table contains default menu positions (coffee, tea, sugar, cream) and
    its default prices. You can easily modify it by using "Set positions price",
    "Add menu positions" and "Remove menu positions" commands ("5", "6", "7" keys).
    To do that input required key and follow instructions.


HOW TO USE (users interfaces)
=============================

 1. Using this program more easily than it's setup. The program will automatically detect
    your role and direct you to the right interface. You only need to login as user:

        python main.py -id user_id

 2. Seller interface contains two commands: "Make a sell" ("1" key) and "Show the menu" ("2" key).
    "Make a sell" command will ask seller about client order then commit data to the
    database and writes a bill (to bills directory). "Show the menu" command shows
    positions that available to sale .

 3. Manager interface contains the only one command "Get sales total" that show information
    about current sales.


PACKAGE TREE
============

coffeeforme(ver1.2)/
├── database_module
│   ├── database
│   ├── database_worker.py
│   ├── db_constants.py
│   └── __init__.py
├── logger_module
│   ├── custom_loggers.py
│   ├── __init__.py
│   ├── logger_messages.py
│   └── logs
├── main.py
├── parsers_module
│   ├── args_parser.py
│   ├── __init__.py
│   └── text_parsers.py
├── README.txt
└── users_module
    ├── admin_interface.py
    ├── bills
    ├── cafe_workers.py
    ├── commands.py
    ├── constants.py
    ├── __init__.py
    ├── input_checker.py
    ├── manager_interface.py
    └── seller_interface.py


CONTACT
=======

Please send bug reports and other feedback to

    timsagepy@gmail.com

