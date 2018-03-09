#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import sqlite3
from users_module import admin_interface, manager_interface, seller_interface, constants
from logger_module import custom_loggers, logger_messages
from database_module import database_worker


def args_parser():
    """
    Returns arguments from command-line input.
    """
    parser = argparse.ArgumentParser(description='A command-line interface for cafe.')
    parser.add_argument('-id', dest='user_id', default='admin', type=str)
    console_args = parser.parse_args()
    guest_user_id = console_args.user_id
    return guest_user_id


def login_func(login_id):
    """
    Determines the type of interface for user.
    """
    if login_id == constants.Const.ADMIN:
        admin_interface.admin_session(constants.Const.ADMIN,
                                      constants.Const.ADMIN)
    elif not get_role_by_id(login_id):
        custom_loggers.logger.error(logger_messages.Messages.NO_DATA)
    else:
        id_, username, role = get_role_by_id(login_id)
        if role == constants.Const.SELLER:
            seller_interface.seller_session(username, id_)
        elif role == constants.Const.MANAGER:
            manager_interface.manager_session(username, id_)


def get_role_by_id(id_):
    """
    Determines the role of user.
    """
    db_worker = database_worker.DatabaseWorker()
    try:
        user_data = db_worker.personal_data(id_)
        if not user_data:
            custom_loggers.logger.error(logger_messages.Messages.NO_ID.format(id_))
            exit()
        else:
            id_ = user_data[0][0]
            username = user_data[0][1]
            role = user_data[0][2]
            return id_, username, role
    except sqlite3.OperationalError:
        custom_loggers.logger.error(logger_messages.Messages.NO_DATA)
        exit()
