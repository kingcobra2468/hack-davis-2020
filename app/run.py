from flask import Flask, render_template
from routes import home_blueprint, graphic_blueprint
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.register_blueprint(home_blueprint)
app.register_blueprint(graphic_blueprint)

@app.route('/buildingData')
def makingMap():
    return render_template("buildingData.html")

if __name__ == "__main__":
    Bootstrap(app)
    app.run(host='0.0.0.0')
