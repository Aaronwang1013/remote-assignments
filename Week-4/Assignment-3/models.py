# DB connection
import pymysql
from flask_bcrypt import generate_password_hash


##configuration
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")
DB_CONFIG = config_object["DB_CONFIG"]

# DB class (will be a database connection whenever initialize)
class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["db"]
        )
        # all query will return dict
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def queryone(self, sql, args=None):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    def create_user(self, email, password):
        try:
            sql = "INSERT INTO user (email, password) VALUES (%s, %s)"
            self.cursor.execute(
                sql, (email, generate_password_hash(password))
            )
            self.conn.commit()
            # print("successfully add")
        except pymysql.IntegrityError:
            raise ValueError("User already exists")


# test = Database()
# print(test.query('SHOW columns FROM user'))
# cursor = Database()
# print(cursor.query("SELECT id FROM user WHERE email =%s", ("email.com",)))
# cursor.create_user("aaron", "1234")
