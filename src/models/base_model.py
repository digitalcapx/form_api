import peewee, os, dotenv

dotenv.load_dotenv()

pg_db = peewee.PostgresqlDatabase(os.environ.get('NAME_DB'), 
                           user=os.environ.get('USER_DB'), 
                           password=os.environ.get('PASS_DB'),
                           host=os.environ.get('HOST_DB'), 
                           port=os.environ.get('PORT_DB'))

class BaseModel(peewee.Model):
    """Classe model base"""

    class Meta:
        database = pg_db