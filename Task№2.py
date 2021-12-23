from flask import Flask


app = Flask(__name__)
print(__name__)

users1 = {'user1': {'username': 'JPetrov', 'name': 'John', 'surname': 'Petrov', 'age': 19},
          'user2': {'username': 'AIvanov', 'name': 'Alex', 'surname': 'Ivanov', 'age': 21}}


@app.route('/redirect')
def users():
    return '<a href = http://127.0.0.1:5000/users>users</a>'


@app.route('/users')
def return_users():
    return f'<a href = http://127.0.0.1:5000/user1>{users1["user1"]["username"]}</a>' \
           "\n" f'<a href = http://127.0.0.1:5000/user2>{users1["user2"]["username"]}</a>'


@app.route('/user1')
def return_user1():
    if 'user1' in users1:
        return users1["user1"]
    else:
        return 'bad request',404


@app.route('/user2')
def return_user2():
    if 'user2' in users1:
        return users1["user2"]
    else:
        return 'bad request',404

if __name__ == '__main__':
    app.run(debug=True)
