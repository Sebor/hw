import sqlite3
import datetime
import json
import os
from bottle import run, request, abort, route, response, error

dbname = os.getenv('APP_DBNAME', 'users.db')
debug = os.getenv('APP_DEBUG', 'False')
reloader = os.getenv('APP_RELOADER', 'True')
port = os.getenv('APP_PORT', 8080)

class Database:
    def __init__(self, name):
        self._conn = sqlite3.connect(name)
        self._cursor = self._conn.cursor()
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self._conn.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

with Database(dbname) as db:
    db.execute("""CREATE TABLE IF NOT EXISTS users
                  (username TEXT NOT NULL, birthdate TEXT NOT NULL)
               """)
    db.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_username ON users(username)")

@error(404)
def error404(error):
    return '404 Not Found'

@route('/hello/<username:re:[aA-zZ]+>', method='PUT')
def UpdateUser(username):
    if not request.body:
        abort(400, 'No data received')
    data = json.load(request.body)
    try:
        datetime.datetime.strptime(data['dateOfBirth'], '%Y-%m-%d')
    except ValueError:
        abort(400, 'Incorrect date format')
    birthdate = data['dateOfBirth']
    if datetime.datetime.strptime(data['dateOfBirth'], '%Y-%m-%d').date() < datetime.date.today():
        with Database(dbname) as db:
            db.execute("INSERT OR REPLACE INTO users (username, birthdate) values(?, ?)", (username, birthdate))
        response.status = 204
        return
    else:
        abort(400, 'The date of birth must be less than the current one')

@route('/hello/<username:re:[aA-zZ]+>', method='GET')
def GetUser(username):
    try:
        today = datetime.date.today()
        with Database(dbname) as db:
            db.execute("SELECT birthdate FROM users WHERE username=?", (username,))
            data = db.fetchone()
        user_bmonth = datetime.datetime.strptime(data[0], '%Y-%m-%d').date().month
        user_bday = datetime.datetime.strptime(data[0], '%Y-%m-%d').date().day
        if [user_bmonth, user_bday] == [today.month, today.day]:
            response.content_type = 'application/json'
            return json.dumps({"message": "Hello, {}! Happy birthday!".format(username)})
        else:
            next_bday = datetime.date(today.year, user_bmonth, user_bday)
            if today < next_bday:
                days = (next_bday - today).days
            else:
                next_bday = datetime.date(today.year + 1, user_bmonth, user_bday)
                days = (next_bday - today).days
            response.content_type = 'application/json'
            return json.dumps({"message": "Hello, {}! Your birthday is in {} day(s)!".format(username, days)})
    except:
        return abort(404)

if __name__ == '__main__':
    run(debug=debug, port=port, reloader=reloader)