## How to set up configuration

All the required user informations are stored in config.ini, replace "your_db_password" by your own MYSQL DB password and "your_secret_key" by your own secret key.


### Two steps to run the application

first, open your mysql and load the assignment.sql

```
mysql -u username -p
source assignment.sql;
```

then, run the flask application
```
python3 app.py
```