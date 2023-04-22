from flask import Flask, render_template, make_response,request, Blueprint
from database.database import mysql

bp = Blueprint('count', __name__)

@bp.route("/count")
def show_count():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT value FROM global_counter ''')
    data = cursor.fetchone()
    cursor.close()
    return 'count: ' + str(data[0])
