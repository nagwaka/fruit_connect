from flask import Flask, request, render_template, flash, redirect, url_for
from models.sign_up import UserSignUp
from models.base import Session, engine, Base


app = Flask(__name__)

Base.metadata.create_all(engine)
# Define the route to render the form

@app.route('/')
def create_account():
    locations = ['City A', 'City B', 'City C']
    return render_template('add_user.html', locations=locations)


# Define the route to handle form submission
@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        location = request.form['location']

        session = Session()
        new_user = UserSignUp(name=name, email=email, phone_number=phone_number, location=location)
        session.add(new_user)
        session.commit()
        session.close()

        return redirect(url_for('homepage', name=name))


@app.route('/welcome/<name>')
def homepage(name):
    return render_template('homepage.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
