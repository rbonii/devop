from flask import Flask, jsonify, render_template, request
from flaskext.mysql import MySQL
from mysql import connector
import os

app = Flask(__name__)
mysql = MySQL(app)

# MySQL configurations
#app.config['MYSQL_HOST'] = 'localhost'
username = os.environ.get('USR')
password = os.environ.get('PASSWORD')
#app.config['MYSQL_DB'] = {{mysqldb}}




@app.route("/api/data")
def get_data():
    cur = connector.connect(user = username, password = password, host='localhost', database='ecole')
    cursor=cur.cursor()
    cursor.execute('''SELECT * from ACTIVITES''')
    
#    r1 = cursor.fetchmany(size=2)
    rv = cursor.fetchall()
    return str(rv)
#    return str(r1)




if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug = True)
