import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from api.api import api_blueprint
from sqlmodels import init_database


app = Flask (__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/date_base.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.register_blueprint(api_blueprint)



if __name__ == "__main__":
    init_database()
    app.run(debug=True)