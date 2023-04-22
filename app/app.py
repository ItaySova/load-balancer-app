from flask import Flask, render_template, make_response,request
from flask_mysqldb import MySQL
from routes.count import bp as count
from routes.homepage import bp as home
import logging
from database.database import app

logging.basicConfig(filename='./logs/record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app.register_blueprint(home)
app.register_blueprint(count)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)