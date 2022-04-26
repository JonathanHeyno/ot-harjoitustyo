import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)


#Polkujen muodostus jos kyseessä Windows ympäristö
if os.name == "nt":
    dirname = dirname[0:len(dirname)-3]
    try:
        load_dotenv(dotenv_path=os.path.join(dirname, '.env'))
    except FileNotFoundError:
        pass

    if not os.path.exists(dirname+'\\data'):
        os.makedirs(dirname+'\\data')

    if not os.path.exists(dirname+'\\saves'):
        os.makedirs(dirname+'\\saves')

    DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.db'
    DATABASE_FILE_PATH = os.path.join(dirname, 'data\\', DATABASE_FILENAME)
    SAVE_FILE_PATH = os.path.join(dirname, 'saves\\')

#Polkujen muodostus jos ei Windows ympäristö
else:
    try:
        load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
    except FileNotFoundError:
        pass

    dirname = dirname[0:len(dirname)-3]
    if not os.path.exists(dirname + '/data/'):
        os.makedirs(dirname + '/data/')

    if not os.path.exists(dirname + '/saves/'):
        os.makedirs(dirname + '/saves/')

    DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.db'
    DATABASE_FILE_PATH = os.path.join(dirname, 'data', DATABASE_FILENAME)
    SAVE_FILE_PATH = os.path.join(dirname, 'saves/')
