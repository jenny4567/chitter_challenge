import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.peep_repository import PeepRepository
from lib.user_repository import UserRepository
from lib.user import User

# Create a new Flask app
app = Flask(__name__)
app.secret_key = "hello"

# Route to homepage of chitter
@app.route('/')
def get_homepage():
    connection = get_flask_database_connection(app)
    repository = PeepRepository(connection)
    peeps = repository.list_all_peeps()
    return render_template('home_page.html', peeps=peeps)

@app.route('/', methods=['POST'])
def login():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    user = user_repository.login_user(request.form['user_handle'], request.form['user_password'])
    if user.name_of_user == None:
        peep_repository = PeepRepository(connection)
        peeps = peep_repository.list_all_peeps()
        return render_template('home_page.html', peeps=peeps, errors = user_repository.generated_errors)
    session["user_handle"] = user.user_handle
    return redirect(f"/user/{user.user_handle}")

@app.route("/user/<user_page_handle>", methods=['GET', 'POST'])
def user_page(user_page_handle):
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    peep_repository = PeepRepository(connection)
    if request.method == 'GET':
        if session["user_handle"] == user_page_handle:
            user = user_repository.find_user(user_page_handle)
        else:
            print('not logged as this user')
            errors = 'You must log in to peep and peep from your user page. '
            return render_template('user_page.html', user=user, peeps=peeps, errors = errors)
    elif request.method == 'POST':
        user = user_repository.find_user(session["user_handle"])
        peep_repository.create_peep(user.id, request.form['content'], request.form['tags'])
    peeps = peep_repository.peeps_by_user(user.id)
    return render_template('user_page.html', user=user, peeps=peeps)

# @app.route("/user/<user_page_handle>", methods=['GET', 'POST'])
# def user_page(user_page_handle):
#     connection = get_flask_database_connection(app)
#     user_repository = UserRepository(connection)
#     peep_repository = PeepRepository(connection)
#     if request.method == 'GET':       
#             user = user_repository.find_user(user_page_handle)
#     elif request.method == 'POST':
#         if session["user_handle"] == user_page_handle:
#             user = user_repository.find_user(session["user_handle"])
#             peep_repository.create_peep(user.id, request.form['content'], request.form['tags'])
#         else:
#             user = user_repository.find_user(user_page_handle) 
#             peeps = peep_repository.peeps_by_user(user.id)
#             errors = 'You must log in to peep and peep from your user page. '
#             return render_template('user_page.html', user=user, peeps=peeps, errors = errors)
#     peeps = peep_repository.peeps_by_user(user.id)
#     return render_template('user_page.html', user=user, peeps=peeps)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))


