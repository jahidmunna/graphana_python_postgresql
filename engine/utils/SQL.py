import os
import traceback
from sqlalchemy import create_engine
from logging import getLogger, NullHandler

# logging setting
default_logger = getLogger(name=__name__)
default_logger.addHandler(NullHandler())


class SQL:
    def __init__(self):
        sql_config = {
            "postgres_user": os.environ['POSTGRES_USER'],
            "postgres_password": os.environ['POSTGRES_PASSWORD'],
            "postgres_host": os.environ['POSTGRES_HOST'],
            "postgres_port": os.environ['POSTGRES_PORT'],
            "postgres_db": os.environ['POSTGRES_DB']
        }
        try:
            self.engine = create_engine(
                'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}'.format(**sql_config))
        except Exception as e:
            traceback.print_exc()
            raise ConnectionError("Could not connect to DB: ", e)


sql = SQL()
engine = sql.engine
