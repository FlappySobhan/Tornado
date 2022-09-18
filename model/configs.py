from decouple import config
from peewee import PostgresqlDatabase
from peewee import Model


db = PostgresqlDatabase(
    database=config('DATABASE'),
    user=config('DB_USER'),
    password=config('DB_PASSWORD'),
    host=config('HOST'),
    port=config('PORT')
)


class BaseModel(Model):
    class Meta:
        database = db
