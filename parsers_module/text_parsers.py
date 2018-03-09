def cut_spaces(input_string):
    new_string = input_string.strip()
    return new_string


def lite_parser(input_string):
    input_list = list(input_string.split(','))
    new_list = []
    for string in input_list:
        new_list.append(string.strip())
    return new_list


def hard_parser(input_string):
    beautiful_dict = dict(x.split('=') for x in input_string.split(','))
    new_dict = {}
    for i in beautiful_dict:
        new_dict[i.strip()] = beautiful_dict[i].strip()
    return new_dict


def seller_name_parser(username):
    spaces_count = user_column_spaces - len(username)
    parsed_username = ' ' * spaces_count + username + ' '
    return parsed_username


def sales_count_parses(number):
    spaces_count = count_column_spaces
    len(str(number))
    parsed_number = spaces_count * ' ' + str(number) + ' '
    return parsed_number


def sales_amount_parser(number):
    spaces_count = total_value_column_spaces - len(str(number))
    parsed_number = spaces_count * ' ' + str(number) + ' '
    return parsed_number


user_column_spaces = 23
count_column_spaces = 11
total_value_column_spaces = 14
