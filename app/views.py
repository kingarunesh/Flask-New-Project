from app import app
from flask import render_template, request
from app.db.user_model import User, db


@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]

        user = User(name=name)
        db.session.add(user)
        db.session.commit()        

    users = User.query.all()

    return render_template("index.html", users=users)