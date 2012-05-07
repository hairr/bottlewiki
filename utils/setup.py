#!/usr/bin/env python3
#
# Criação do banco e tabelas

import sqlite3
from os import path

if path.exists('../wiki.sql'):
    print('existe')
else:
    print('não existe')
