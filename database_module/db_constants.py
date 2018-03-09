class SqliteCommands(object):
    # Select
    SELECT_ALL = 'SELECT * from sqlite_master WHERE type = "table"'
    SELECT_USERS_DATA = 'SELECT * from users'
    SELECT_PERSONAL = 'SELECT * from users WHERE id = ?'
    SELECT_BY_USER = 'SELECT * from users WHERE full_name = ?'
    SELECT_MENU = 'SELECT * from menu'
    SELECT_POSITION = 'SELECT * from menu WHERE position = ?'
    SELECT_PRICE = 'SELECT price from menu WHERE position = ?'

    # Update
    UPDATE_COUNT = 'UPDATE users SET sales_counter = ? WHERE full_name = ?'
    UPDATE_TOTAL = 'UPDATE users SET sales_amount = ? WHERE full_name = ?'
    UPDATE_PRICE = 'UPDATE menu SET price = ? WHERE position = ?'

    # Create
    CREATE_MENU = 'CREATE table menu (position text, price integer)'
    CREATE_USERS = 'CREATE table users (id text, full_name text, role text, ' \
                   'sales_counter integer, sales_amount integer)'

    # Insert
    INSERT_IN_MENU = 'INSERT into menu (position, price) VALUES (?, ?)'
    INSERT_IN_USERS = 'INSERT into users (id, full_name, role, sales_counter, sales_amount) ' \
                      'VALUES (?, ?, ?, ?, ?)'

    # Delete
    DEL_FROM_USERS = 'DELETE from users WHERE id = ?'
    DEL_FROM_MENU = 'DELETE from menu WHERE position = ?'

    # Drop
    DROP_USERS = 'DROP TABLE users'
    DROP_MENU = 'DROP TABLE menu'


class Tables(object):
    # Menu
    COFFEE = ('coffee', 2)
    TEA = ('tea', 1)
    SUGAR = ('sugar', 0.1)
    CREAM = ('cream', 0.5)
    CINNAMON = ('cinnamon', 0.1)
    ZERO = 0
