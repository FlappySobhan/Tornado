from decouple import config
from peewee import PostgresqlDatabase
from peewee import Model


def database() -> PostgresqlDatabase:
    db = PostgresqlDatabase(
        database=config('DATABASE'),
        user=config('DB_USER'),
        password=config('DB_PASSWORD'),
        host=config('HOST'),
        port=config('PORT')
    )
    return db


class BaseModel(Model):
    """This is the base class that all models inherit from it"""
    class Meta:
        database = database()
