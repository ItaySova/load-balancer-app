from flask import render_template, make_response,request, Blueprint, redirect
from database.database import mysql

bp = Blueprint('/logs', __name__)

@bp.route("/logs", methods=['GET', 'POST'])
def logs():
    print("test")
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM access_log ''')
        data = cursor.fetchall()
        cursor.close()
        headings = ("log id", "date_time", "client_ip", "internal_ip")
        res = make_response(render_template("logs.html", headings=headings, data = data))
        return res
    else:
        return redirect('/')