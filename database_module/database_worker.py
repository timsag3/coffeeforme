#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sqlite3
from logger_module import custom_loggers, logger_messages
from database_module import db_constants

database_dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "database")
database_path = os.path.join(database_dir_path, "database.db")


class DatabaseWorker(object):
    """
    Class that works with sqlite3 package.
    Contains 13 methods and 1 property.
    The property checks for database status.
    Methods setups database or returns data from it.
    """

    def __init__(self):
        if not os.path.exists(database_dir_path):
            os.makedirs(database_dir_path)
        self.path = database_path

    @property
    def status(self):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(db_constants.SqliteCommands.SELECT_ALL)
        data = cursor.fetchall()
        cursor.close()
        if len(data) > 0:
            return True
        else:
            custom_loggers.logger.error(logger_messages.Messages.NO_DATA)
            return False

    def create_default(self):
        try:
            conn = sqlite3.connect(self.path)
            cursor = conn.cursor()
            cursor.execute(db_constants.SqliteCommands.CREATE_USERS)
            custom_loggers.logger.info(logger_messages.Messages.USER_TABLE_CREATED)
            cursor.execute(db_constants.SqliteCommands.CREATE_MENU)
            cursor.execute(
                db_constants.SqliteCommands.INSERT_IN_MENU, db_constants.Tables.COFFEE)
            cursor.execute(
                db_constants.SqliteCommands.INSERT_IN_MENU, db_constants.Tables.TEA)
            cursor.execute(
                db_constants.SqliteCommands.INSERT_IN_MENU, db_constants.Tables.SUGAR)
            cursor.execute(
                db_constants.SqliteCommands.INSERT_IN_MENU, db_constants.Tables.CREAM)
            cursor.execute(
                db_constants.SqliteCommands.INSERT_IN_MENU, db_constants.Tables.CINNAMON)

            custom_loggers.logger.info(logger_messages.Messages.MENU_TABLE_CREATED)
            custom_loggers.logger.info(logger_messages.Messages.DATA_SETUP)
            conn.commit()
            cursor.close()
        except sqlite3.OperationalError:
            custom_loggers.logger.error(logger_messages.Messages.TABLES_EXIST)

    def clear(self):
        try:
            conn = sqlite3.connect(self.path)
            cursor = conn.cursor()
            cursor.execute(db_constants.SqliteCommands.DROP_USERS)
            cursor.execute(db_constants.SqliteCommands.DROP_MENU)
            conn.commit()
            cursor.close()
            custom_loggers.logger.warn(logger_messages.Messages.DATA_CLEAR)
        except sqlite3.OperationalError:
            custom_loggers.logger.error(logger_messages.Messages.EMPTY_DATA)

    def users_data(self):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(db_constants.SqliteCommands.SELECT_USERS_DATA)
        users_data = cursor.fetchall()
        if len(users_data) == 0:
            return None
        cursor.close()
        return users_data

    def personal_data(self, id_):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(db_constants.SqliteCommands.SELECT_PERSONAL, [(id_)])
        personal_data = cursor.fetchall()
        if len(personal_data) == 0:
            return None
        cursor.close()
        return personal_data

    def add_user(self, id_, full_name, role):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(
            db_constants.SqliteCommands.INSERT_IN_USERS, (
                id_, full_name, role, db_constants.Tables.ZERO, db_constants.Tables.ZERO))
        custom_loggers.logger.info(
            logger_messages.Messages.USER_ADD.format(full_name, id_, role))
        conn.commit()
        cursor.close()

    def remove_user(self, id_, username):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(db_constants.SqliteCommands.DEL_FROM_USERS, [(id_)])
        custom_loggers.logger.warn(logger_messages.Messages.USER_REM.format(username, id_))
        conn.commit()
        cursor.close()

    def commit_sale(self, user_name, order_price):
        """
        The main function for seller interface.
        It's commit sales data to the database.
        """
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(db_constants.SqliteCommands.SELECT_BY_USER, [(user_name)])
        user_data = cursor.fetchall()
        current_sales_count = user_data[0][3]
        current_sales_amount = user_data[0][4]
        new_sales_count = current_sales_count + 1
        new_sales_amount = current_sales_amount + order_price
        cursor.execute(db_constants.SqliteCommands.UPDATE_COUNT, (new_sales_count, user_name))
        cursor.execute(db_constants.SqliteCommands.UPDATE_TOTAL, (new_sales_amount, user_name))
        conn.commit()
        cursor.close()

    def menu_data(self):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(db_constants.SqliteCommands.SELECT_MENU)
        menu_data = cursor.fetchall()
        cursor.close()
        return menu_data

    def positions_data(self, title):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(db_constants.SqliteCommands.SELECT_POSITION, [(title)])
        position_data = cursor.fetchall()
        if len(position_data) == 0:
            return None
        cursor.close()
        return position_data

    def position_price(self, title):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(db_constants.SqliteCommands.SELECT_PRICE, [(title)])
        position_price = cursor.fetchall()
        if len(position_price) == 0:
            return None
        cursor.close()
        position_price = position_price[0][0]
        return position_price

    def set_price(self, title, price):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(db_constants.SqliteCommands.UPDATE_PRICE, (price, title))
        custom_loggers.logger.warn(
            logger_messages.Messages.PRICE_SET.format(title, price))
        conn.commit()
        cursor.close()

    def add_position(self, title, price):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(db_constants.SqliteCommands.INSERT_IN_MENU, (title, price))
        custom_loggers.logger.info(
            logger_messages.Messages.POSITION_ADD.format(title, price))
        conn.commit()
        cursor.close()

    def remove_position(self, title):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute(db_constants.SqliteCommands.DEL_FROM_MENU, [(title)])
        custom_loggers.logger.warn(
            logger_messages.Messages.POSITION_REM.format(title))
        conn.commit()
        cursor.close()
