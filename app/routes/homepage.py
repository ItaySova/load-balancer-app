from flask import render_template, make_response,request, Blueprint
from database.database import mysql
import datetime
import socket

bp = Blueprint('/', __name__)

@bp.route("/")
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
    return res
