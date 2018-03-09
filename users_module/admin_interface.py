#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from logger_module import custom_loggers, logger_messages
from users_module import cafe_workers, constants

python_version = sys.version_info.major
if python_version == 3:
    input = input
else:
    input = raw_input


def admin_session(username, id_):
    """
    Admin interactive interface. It using admin static
    methods from users module. Contains 9 main commands.
    """
    admin = cafe_workers.Admin(username, id_)

    while True:
        navigation = input()

        if navigation == constants.Commands.EXIT or navigation == constants.Commands.ZERO:
            custom_loggers.logger.info(
                logger_messages.InterfaceMessages.GOOD_BUY.format(admin.username))
            exit()

        elif navigation == constants.Commands.RETURN or navigation == constants.Commands.COMMANDS:
            custom_loggers.print_logger.info(
                logger_messages.InterfaceMessages.COMMANDS.format(admin.commands))

        elif navigation == constants.Commands.ONE:
            custom_loggers.print_logger.info(logger_messages.InterfaceMessages.CREATE_DATA)
            admin.create_default_database()

        elif navigation == constants.Commands.TWO:
            custom_loggers.print_logger.info(logger_messages.InterfaceMessages.CLEAR_DATA)
            admin.clear_database()

        elif navigation == constants.Commands.THREE:
            custom_loggers.print_logger.info(logger_messages.InterfaceMessages.ADD_USER)
            admin.add_new_user()

        elif navigation == constants.Commands.FOUR:
            custom_loggers.print_logger.info(logger_messages.InterfaceMessages.REM_USER)
            admin.remove_users()

        elif navigation == constants.Commands.FIVE:
            custom_loggers.print_logger.info(logger_messages.InterfaceMessages.SET_PRICE)
            admin.set_positions_price()

        elif navigation == constants.Commands.SIX:
            custom_loggers.print_logger.info(logger_messages.InterfaceMessages.ADD_POSITION)
            admin.add_positions()

        elif navigation == constants.Commands.SEVEN:
            custom_loggers.print_logger.info(logger_messages.InterfaceMessages.REM_POSITION)
            admin.remove_positions()

        elif navigation == constants.Commands.EIGHT:
            custom_loggers.print_logger.info(logger_messages.InterfaceMessages.REM_POSITION)
            admin.get_menu_list()

        elif navigation == constants.Commands.NINE:
            custom_loggers.print_logger.info(logger_messages.InterfaceMessages.USER_LIST)
            admin.get_users_list()
        else:
            custom_loggers.logger.error(logger_messages.Messages.NO_COMMAND)
