from flask import render_template, make_response,request, Blueprint
from database.database import mysql

bp = Blueprint('/form', __name__)

@bp.route("/form", methods=['GET', 'POST'])
def form_handler():
    if request.method == 'GET':
        pass
    else:
        pass