import os

from dotenv import load_dotenv
import psycopg2

from sqlalchemy import create_engine

load_dotenv()

def get_connection():

    connection = psycopg2.connect (
    host = os.getenv("DB_HOST"),
    port = os.getenv("DB_PORT"),
    database = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD")

    )

    return connection





def get_connection_sql():


    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")


    connection_url = (
        f"postgresql+psycopg2://"
        f"{user}:{password}@{host}:{port}/{database}"

    )

    return create_engine(connection_url)

