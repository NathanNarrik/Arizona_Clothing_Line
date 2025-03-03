from flask import Flask, render_template, request
from User import User
import datetime
import os
import pickle
from pickle import load, dump


f = open('users.txt', 'br')
app = Flask(__name__)

#populate users list with users from file
users = []
if os.path.getsize('users.txt') > 0:
    users = pickle.load(f)
f.close()


@app.route('/')
def home():
    return render_template('signup.html')

@app.route('/logout',  methods=['POST'])
def logout():
    return render_template('signup.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    f = open('users.txt', 'br')
    users = []
    if os.path.getsize('users.txt') > 0:
        users = pickle.load(f)
    f.close()

    for user in users:
        print(user.get_username())
    

    # Get the user's input from the form
    username = request.form['username']
    email = request.form['email']
    zipcode = request.form['zipcode']
    password = request.form['password']
    
    for user in users:
        if user.get_username() == username:
            return render_template('check.html', user=user)

    user = User(username, email, password, zipcode)
    # Add the user to the list of users
    users.append(user)
    # Save the list of users to a file
    f = open('users.txt', 'bw')
    pickle.dump(users, f)
    # Return the results page
    f.close()
    return render_template('check.html', user=user)

@app.route('/check', methods=['POST'])
def check():

    f = open('users.txt', 'br')
    users = []
    if os.path.getsize('users.txt') > 0:
        users = pickle.load(f)
    f.close()

    num_clothes = request.form['clothes']
    num_clothes = int(num_clothes)
    username = request.form['username']
    print("01 " + username)            
    
    for user in users:
        print("02 " + username)
        print("03 " + user.get_username())
        if user.get_username() == username:
            print(type(user))
            user.update_humidity()
            user.update_temperature()
            user.update_wind_speed()
            user.increment_clothes_dried(num_clothes)
            user.increment_eco_points()
            print(user.get_clothes_dried())
            f = open('users.txt', 'bw')
            pickle.dump(users, f)
            f.close()            
            return render_template('results.html', user=user, num_clothes=num_clothes)
    
    return render_template('login.html')         
    


@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html')


@app.route('/login_complete', methods=['POST'])
def login_complete():
    f = open('users.txt', 'br+')
    users = []
    if os.path.getsize('users.txt') > 0:
        users = pickle.load(f)
    
    username = request.form['username']
    password = request.form['password']

    print(users)
    for user in users:
        print(user.get_username()+ "1")

    for user in users:
        if user.get_username() == username:
            if user.get_password() == password:
                f.close()
                return render_template('check.html', user=user)
            else:
                f.close()
                return render_template('login.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)