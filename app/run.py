from flask import Flask
from routes import image_feed_blueprint, discovery_blueprint, home_blueprint, graphic_blueprint
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.register_blueprint(image_feed_blueprint, url_prefix = "/video/")
app.register_blueprint(discovery_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(graphic_blueprint)
if __name__ == "__main__":
    Bootstrap(app)
    app.run(host='0.0.0.0')
