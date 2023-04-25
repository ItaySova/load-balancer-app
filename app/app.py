from routes.count import bp as count
from routes.homepage import bp as home
from routes.table import bp as logs_table
import logging
from database.database import app

# logging.basicConfig(filename='./logs/record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
logging.basicConfig(level=logging.DEBUG)
app.logger.info("hello world")

app.register_blueprint(home)
app.register_blueprint(count)
app.register_blueprint(logs_table)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)