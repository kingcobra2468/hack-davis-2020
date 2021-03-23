from flask import Flask, render_template
from routes import home_blueprint, graphic_blueprint
from flask_bootstrap import Bootstrap
from config import IP_ADDR, PORT

app = Flask(__name__)
app.register_blueprint(home_blueprint)
app.register_blueprint(graphic_blueprint)

if __name__ == "__main__":
    
    Bootstrap(app)
    app.run(host=IP_ADDR, port=PORT)
