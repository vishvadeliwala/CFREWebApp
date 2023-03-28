from flask import Flask
from flask_login import LoginManager

from index.controller import home
from login import login
from signup import signup

app = Flask(__name__, static_folder='../frontend/static')



app.register_blueprint(home)
app.register_blueprint(login)
app.register_blueprint(signup)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)