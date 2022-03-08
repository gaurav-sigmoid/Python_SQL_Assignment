import psycopg2
import logging
from sqlalchemy import create_engine
from config import config


class Create_connection:

    def get_connection(self):
        try:
            params = config()
            connection = psycopg2.connect(**params)
            return connection
        except:
            logging.error("Connection Error")
            raise Exception("Connection cannot be established")
        finally:
            logging.info("Connection successfully established")

    def get_engine(self):
        try:
            params = config()
            engine = create_engine(**params)
            return engine
        except:
            logging.error("Error in engine creation")
        finally:
            logging.info("Engine successfully created")

