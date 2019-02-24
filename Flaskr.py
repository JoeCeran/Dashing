from flask import Flask, render_template,session,redirect,url_for,request   
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,SubmitField,
                    RadioField,SelectField,TextField,
                    TextAreaField,SubmitField)     

from wtforms.validators import DataRequired
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'


@app.route("/")
def home():
    return render_template("Base.html")

@app.route("/child")
def child():
    return render_template("Child.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)