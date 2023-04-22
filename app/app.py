from flask import Flask, render_template, make_response,request
from flask_mysqldb import MySQL
from routes.count import bp as count
from routes.homepage import bp as home
import datetime
import os
import logging
import socket
from database.database import app, mysql
# app = Flask(__name__)

logging.basicConfig(filename='./logs/record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
# app.config['MYSQL_DB'] = "dockertrial"

# mysql = MySQL(app)

@app.route("/")
def home():
    rem_ip = request.remote_addr
    time = datetime.datetime.now()
    local_ip = socket.gethostbyname(socket.gethostname())
    cursor = mysql.connection.cursor()
    cursor.execute(''' UPDATE global_counter SET value=value + 1 ''')
    try:
        cursor.execute(''' INSERT INTO access_log VALUES(%s,%s,%s) ''',(time, rem_ip,local_ip))
    except:
        print("can't insert into table - please try again")
    mysql.connection.commit()
    cursor.close()
    res = make_response(render_template("index.html", com_ip=local_ip, remote_ip = rem_ip))
    res.set_cookie('internal_ip', local_ip, 30)
    # res.set_cookie('remote_ip', rem_ip, 30)
    return res


app.register_blueprint(home)
app.register_blueprint(count)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)