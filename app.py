from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))


# Home Route (Form Page)
@app.route("/")
def home():
    return render_template("form.html")


# Create User
@app.route("/create", methods=["POST"])
def create_user():
    name = request.form['name']
    email = request.form['email']

    new_user = User(name=name, email=email)

    db.session.add(new_user)
    db.session.commit()

    return "User Added Successfully ✅"


# Get All Users
@app.route("/users")
def get_users():

    users = User.query.all()

    result = []

    for user in users:
        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })

    return jsonify(result)


# Delete User
@app.route("/delete/<int:id>")
def delete_user(id):

    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return "User Deleted Successfully"


# Run Application
if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=5000, debug=True)