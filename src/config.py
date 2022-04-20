import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)



if os.name == "nt":
    dirname = dirname[0:len(dirname)-3]
    try:
        load_dotenv(dotenv_path=os.path.join(dirname, '.env'))
    except FileNotFoundError:
        pass

    if not os.path.exists(dirname+'\\data'):
        os.makedirs(dirname+'\\data')

    DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.db'
    DATABASE_FILE_PATH = os.path.join(dirname, 'data\\', DATABASE_FILENAME)

else:
    try:
        load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
    except FileNotFoundError:
        pass

    dirname = dirname[0:len(dirname)-3]

    DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.db'
    DATABASE_FILE_PATH = os.path.join(dirname, 'data', DATABASE_FILENAME)
