#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import time
from logger_module import custom_loggers, logger_messages
from database_module import database_worker
from users_module import commands, input_checker, constants
from parsers_module import text_parsers

db_worker = database_worker.DatabaseWorker()

python_version = sys.version_info.major
if python_version == 3:
    input = input
else:
    input = raw_input


class CafeWorker(object):
    """
    The main class for cafe workers.
    """

    def __init__(self, username, id_):
        self.username = username
        self.id_ = id_
        custom_loggers.logger.info(logger_messages.Messages.WELCOME.format(self.username))
        custom_loggers.logger.info(logger_messages.Messages.PRESS_RETURN)


class Admin(CafeWorker):
    """
    Admin class contains 9 static methods
    equivalent administrator commands. Methods
    from third to seventh checks and parse user
    input and if it's valid sends it to database.
    """

    def __init__(self, username, id_):
        super(Admin, self).__init__(username, id_)
        self.commands = commands.Commands.ADMIN_COMMANDS

    @staticmethod
    def create_default_database():  # Admin command N.1
        db_worker.create_default()

    @staticmethod
    def clear_database():  # Admin command N.2
        db_worker.clear()

    @staticmethod
    def add_new_user():  # Admin command N.3
        if not db_worker.status:
            return None

        while True:
            full_name = input(logger_messages.Messages.ENTER_NAME)
            if not length_checker(full_name):
                pass
            elif full_name == constants.Const.CANCEL:
                custom_loggers.logger.warn(logger_messages.Messages.ABORT)
                return None
            elif not input_checker.InputChecker.user_name(full_name):
                pass
            else:
                full_name = text_parsers.cut_spaces(full_name)
                break

        while True:
            id_ = input(logger_messages.Messages.ENTER_ID)
            if not length_checker(id_):
                pass
            elif id_ == constants.Const.CANCEL:
                custom_loggers.logger.warn(logger_messages.Messages.ABORT)
                return None
            elif not input_checker.InputChecker.id_(id_):
                pass
            elif db_worker.personal_data(id_):
                username = db_worker.personal_data(id_)[0][1]
                custom_loggers.logger.error(
                    logger_messages.Messages.ID_IN_USE.format(id_, username))
                pass
            else:
                id_ = text_parsers.cut_spaces(id_)
                break

        while True:
            role = input(logger_messages.Messages.ENTER_ROLE)
            if not length_checker(role):
                pass
            elif role == constants.Const.CANCEL:
                custom_loggers.logger.warn(logger_messages.Messages.ABORT)
                return None
            elif not input_checker.InputChecker.role(role):
                pass
            else:
                db_worker.add_user(id_, full_name, role)
                break

    @staticmethod
    def remove_users():  # Admin command N.4
        if not db_worker.status:
            return None
        id_s = input(logger_messages.Messages.ENTER_IDS)
        if not length_checker(id_s):
            return None

        id_s = text_parsers.lite_parser(id_s)
        for id_ in id_s:
            user_data = db_worker.personal_data(id_)
            if not user_data:
                custom_loggers.logger.error(
                    logger_messages.Messages.NO_ID.format(id_))
            else:
                username = user_data[0][1]
                db_worker.remove_user(id_, username)

    @staticmethod
    def set_positions_price():  # Admin command N.5
        if not db_worker.status:
            return None
        titles = input(logger_messages.Messages.ENTER_TITLES_AND_PRICE)
        if not length_checker(titles):
            return None
        try:
            titles = text_parsers.hard_parser(titles)
        except ValueError:
            custom_loggers.logger.error(logger_messages.Messages.INC_INPUT)
            return None

        for position in titles:
            title = position
            price = titles[position]
            if not db_worker.positions_data(title):
                custom_loggers.logger.error(
                    logger_messages.Messages.NO_POSITION.format(title))
            elif not input_checker.InputChecker.price(price, title):
                pass
            else:
                db_worker.set_price(title, price)

    @staticmethod
    def add_positions():  # Admin command N.6
        if not db_worker.status:
            return None
        titles = input(logger_messages.Messages.ENTER_NEW_POSITIONS)
        if not length_checker(titles):
            return None
        try:
            titles = text_parsers.hard_parser(titles)
        except ValueError:
            custom_loggers.logger.error(logger_messages.Messages.INC_INPUT)
            return None

        for position in titles:
            title = position
            price = titles[position]
            if db_worker.positions_data(title):
                custom_loggers.logger.error(
                    logger_messages.Messages.ON_THE_MENU.format(title))
            elif not input_checker.InputChecker.price(price, title):
                pass
            else:
                db_worker.add_position(title, price)

    @staticmethod
    def remove_positions():  # Admin command N.7
        if not db_worker.status:
            return None
        titles = input(logger_messages.Messages.ENTER_TITLES)
        if not length_checker(titles):
            return None

        titles = text_parsers.lite_parser(titles)
        for position in titles:
            if not db_worker.positions_data(position):
                custom_loggers.logger.error(
                    logger_messages.Messages.NO_POSITION.format(position))
            else:
                db_worker.remove_position(position)

    @staticmethod
    def get_menu_list():  # Admin command N.8
        if not db_worker.status:
            return None

        menu_list = db_worker.menu_data()
        for position in menu_list:
            title = position[0]
            price = position[1]
            custom_loggers.print_logger.info(
                logger_messages.Messages.MENU_LIST.format(title, price))

    @staticmethod
    def get_users_list():  # Admin command N.9
        if not db_worker.status:
            return None
        users_list = db_worker.users_data()
        if not users_list:
            custom_loggers.logger.error(logger_messages.Messages.EMPTY_USERS)
            return None
        for user in users_list:
            id_ = user[0]
            user_name = user[1]
            role = user[2]
            custom_loggers.print_logger.info(
                logger_messages.Messages.USER_LIST.format(id_, user_name, role))


class Seller(CafeWorker):
    """
    Seller class contains 2 static methods equivalent
    seller commands. The main method is "make_a_sell".
    It checks and parse user input and if it's valid
    sends to the database.
    """

    def __init__(self, username, id_):
        super(Seller, self).__init__(username, id_)
        self.commands = commands.Commands.SELLER_COMMANDS

    @staticmethod
    def make_sell(username):  # Seller command N.1
        if not db_worker.status:
            return None
        custom_loggers.print_logger.info(logger_messages.Messages.ENTER_CLIENT_ORDER)
        client_order = input(logger_messages.Messages.CLIENT_ORDER)
        if not length_checker(client_order):
            return None
        try:
            client_order = text_parsers.hard_parser(client_order)
        except ValueError:
            custom_loggers.logger.error(logger_messages.Messages.INC_INPUT)
            return None

        bill_list = [constants.Const.BILL_HEAD.format(username)]
        order_price = 0
        for order in client_order:
            title = order
            count = float(client_order[order])
            position_price = db_worker.position_price(title)
            if not position_price:
                custom_loggers.logger.error(
                    logger_messages.Messages.NO_POSITION.format(title))
            elif not input_checker.InputChecker.price(count, title):
                pass
            else:
                title, count, sum_count = get_the_bill(title, count, position_price)
                bill_list.append(
                    constants.Const.BILL_APPEND.format(title, count, sum_count))
                order_price += sum_count

        if order_price == 0:
            return None
        bill_list.append(constants.Const.BILL_TOTAL.format(order_price))
        commit_sale(username, order_price, bill_list)

    @staticmethod  # Seller command N.2
    def show_menu():
        Admin.get_menu_list()


class Manager(CafeWorker):
    """
    Manager class contains 1 static methods
    that shows parsed sales total data.
    """

    def __init__(self, username, id_):
        super(Manager, self).__init__(username, id_)
        self.commands = commands.Commands.MANAGER_COMMANDS

    @staticmethod
    def get_sales_total():  # Manager command N.1
        if not db_worker.status:
            return None
        users_data = db_worker.users_data()
        custom_loggers.print_logger.info(logger_messages.Messages.SALES_TOTAL)
        total_value = 0
        total_sales_count = 0
        for user in users_data:
            role = user[2]
            if role == constants.Const.SELLER:
                username = text_parsers.seller_name_parser(user[1])
                sales_count = text_parsers.sales_count_parses(user[3])
                seller_amount = text_parsers.sales_amount_parser(user[4])
                total_value += user[4]
                total_sales_count += user[3]
                custom_loggers.print_logger.info(
                    logger_messages.Messages.USERS_SALES.format(
                        username, sales_count, seller_amount))

        total_value = text_parsers.sales_amount_parser(total_value)
        total_sales_count = text_parsers.sales_count_parses(total_sales_count)
        custom_loggers.print_logger.info(
            logger_messages.Messages.TOTAL_VALUE.format(
                constants.Spaces.USERNAME_SPACES, total_sales_count, total_value))


# Help functions below.

def length_checker(input_str):
    if len(input_str) == 0:
        custom_loggers.logger.error(logger_messages.Messages.EMPTY_INPUT)
        return None
    else:
        return input_str


def get_the_bill(title, count, position_price):
    position_price = position_price
    count = count
    sum_count = position_price * count
    return title, count, sum_count


def commit_sale(username, order_price, bill_list):
    for order in bill_list[1:]:
        custom_loggers.logger.info(order)
    while True:
        make_a_sale = input(logger_messages.Messages.MAKE_SALE)
        if make_a_sale == 'n' or make_a_sale == 'N':
            custom_loggers.logger.warn(logger_messages.Messages.ABORT)
            break
        elif make_a_sale == 'y' or make_a_sale == 'Y' or make_a_sale == '':
            db_worker.commit_sale(username, order_price)
            custom_loggers.logger.info(logger_messages.Messages.SALE_COMP)
            with open(get_bill_name(), 'w+') as bill:
                for data in bill_list:
                    bill.write('{}\n'.format(data))
                bill.flush()
                bill.close()
            break
        else:
            custom_loggers.logger.error(logger_messages.Messages.INC_INPUT)


def get_bill_name():
    bill_name = time.strftime("%d.%m.%Y_%H.%M.%S")
    bills_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bills")
    bills_path = os.path.join(bills_dir, bill_name)
    if not os.path.exists(bills_dir):
        os.makedirs(bills_dir)
    return bills_path
