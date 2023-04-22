from flask import Flask, render_template, make_response,request
from flask_mysqldb import MySQL
import datetime
import os
import logging
import socket

app = Flask(__name__)

logging.basicConfig(filename='./logs/record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
app.config['MYSQL_DB'] = "dockertrial"

mysql = MySQL(app)

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
    res.set_cookie('internal_ip', local_ip, 300)
    return res


@app.route("/showcount")
def show_count():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT value FROM global_counter ''')
    data = cursor.fetchone()
    cursor.close()
    return 'count: ' + str(data[0])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)