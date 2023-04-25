from flask import render_template, make_response,request, Blueprint
from database.database import mysql

bp = Blueprint('/logs', __name__)

@bp.route("/logs", methods=['GET', 'POST'])
def logs():
    print("test")
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM access_log ''')
        data = cursor.fetchone()
        cursor.close()
        res = make_response(render_template("logs.html", log_id=data[0], date_time = data[1], client_ip=data[2] , internal_ip=data[3]))
        # res = f'data retrieved, response type {(data)}'
        return res
    else:
        pass