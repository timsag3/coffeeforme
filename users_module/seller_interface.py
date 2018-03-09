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


def seller_session(username, id_):
    """
    Seller interactive interface. It using seller
    static methods from users module and contains
    two main commands.
    """
    seller = cafe_workers.Seller(username, id_)

    while True:
        navigation = input()

        if navigation == constants.Commands.EXIT or navigation == constants.Commands.ZERO:
            custom_loggers.logger.info(
                logger_messages.InterfaceMessages.GOOD_BUY.format(seller.username))
            exit()

        elif navigation == constants.Commands.RETURN or navigation == constants.Commands.COMMANDS:
            custom_loggers.print_logger.info(
                logger_messages.InterfaceMessages.COMMANDS.format(seller.commands))

        elif navigation == constants.Commands.ONE:
            custom_loggers.print_logger.info(logger_messages.InterfaceMessages.MAKE_SELL)
            seller.make_sell(seller.username)

        elif navigation == constants.Commands.TWO:
            custom_loggers.print_logger.info(logger_messages.InterfaceMessages.MENU)
            seller.show_menu()

        else:
            custom_loggers.logger.error(logger_messages.Messages.NO_COMMAND)
