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


def manager_session(username, id_):
    """
    Manager interactive interface. It using manager
    static method from users module and contains one
    main command.
    """
    manager = cafe_workers.Manager(username, id_)

    while True:
        navigation = input()

        if navigation == constants.Commands.EXIT or navigation == constants.Commands.ZERO:
            custom_loggers.logger.info(
                logger_messages.InterfaceMessages.GOOD_BUY.format(manager.username))
            exit()

        elif navigation == constants.Commands.RETURN or navigation == constants.Commands.COMMANDS:
            custom_loggers.print_logger.info(
                logger_messages.InterfaceMessages.COMMANDS.format(manager.commands))

        elif navigation == constants.Commands.ONE:
            custom_loggers.print_logger.info(logger_messages.InterfaceMessages.SALES_TOTAL)
            manager.get_sales_total()

        else:
            custom_loggers.logger.error(logger_messages.Messages.NO_COMMAND)
