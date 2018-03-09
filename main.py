#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python package based on sqlite3 module.
It consists of two main custom modules:
database_module and users_module.
The user_module works with user and
contains 3 type of interface and statics
methods that work with interfaces.
The database_module works with database only.
"""

from parsers_module import args_parser

__author__ = "Tim Marchenko"


def start_program():
    login_id = args_parser.args_parser()
    args_parser.login_func(login_id)


if __name__ == '__main__':
    start_program()
