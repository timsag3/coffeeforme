from logger_module import custom_loggers, logger_messages
from users_module import constants


class InputChecker(object):

    @staticmethod
    def user_name(full_name):
        if not symbol_checker(full_name):
            custom_loggers.logger.error(logger_messages.Messages.INC_USER)
            return None
        else:
            return full_name

    @staticmethod
    def id_(id_):
        if not id_.isdigit():
            custom_loggers.logger.error(logger_messages.Messages.INC_ID)
            return None
        else:
            return True

    @staticmethod
    def role(role):
        if role == constants.Const.SELLER or role == constants.Const.MANAGER:
            return role
        else:
            custom_loggers.logger.error(logger_messages.Messages.INC_ROLE)
            return None

    @staticmethod
    def price(number, title):
        if not positive_number_checker(number):
            custom_loggers.logger.info(
                logger_messages.Messages.INC_ATTR.format(number, title))
            return None
        else:
            return True


def symbol_checker(input_str):
    for symbol in input_str:
        if symbol.isalpha() or symbol == ' ':
            pass
        else:
            return None
    return input_str


def positive_number_checker(number):
    try:
        price = float(number)
        if price <= 0:
            return None
        else:
            return True
    except ValueError:
        return None
