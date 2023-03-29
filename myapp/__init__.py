from flask import Flask
from config import configure_app
import secrets
# Import blueprints
from index.controller import home
from index.login import login
from index.signup import signup
from index.signout import signout
from index.home import homepage
from index.contact import contact
from index.crop import crop
from index.fertilizer import fertilizer
from index.history import history

app = Flask(__name__)
app.secret_key = secrets.token_bytes(32)
configure_app(app)

# register blue prints
app.register_blueprint(home, url_prefix='')
app.register_blueprint(login, url_prefix='')
app.register_blueprint(homepage, url_prefix='')
app.register_blueprint(signup, url_prefix='')
app.register_blueprint(signout, url_prefix='')
app.register_blueprint(contact, url_prefix='')
app.register_blueprint(crop, url_prefix='')
app.register_blueprint(fertilizer, url_prefix='')
app.register_blueprint(history, url_prefix='')
