from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABSE_URL")

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__  = 'users'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    des = db.Column(db.String)

db.init_app(app)


@app.route("/new", methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        title = request.form['title']
        des = request.form['des']

        user = User(title = title, des = des)
        db.session.add(user)
        db.session.commit()
    return render_template('new.html')

@app.route("/title/<title>")
def users(title):
    user = User.query.filter_by(title=title).first()
    if user is None:
        return "Title does not exist"
    else:
        return user.des


app.run(host='0.0.0.0', port=8080, debug=True)