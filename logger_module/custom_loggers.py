#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import sys
import os

# Logs directory
logs_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logs')
logs_path = os.path.join(logs_dir, 'logs.txt')

if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Loggers format
date_format = '%d.%m.%Y %H:%M:%S'
formatter = logging.Formatter('%(asctime)s ~%(name)s~: %(message)s', date_format)
logs_formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', date_format)

# Main logger
logger = logging.getLogger('CoffeeForMe')
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler(stream=sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
file_handler = logging.FileHandler(logs_path)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logs_formatter)
logger.addHandler(file_handler)

# Print logger
print_logger = logging.getLogger('CFM_prints')
print_logger.setLevel(logging.INFO)
print_handler = logging.StreamHandler(stream=sys.stdout)
print_handler.setLevel(logging.INFO)
print_logger.addHandler(print_handler)
