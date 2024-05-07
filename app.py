from flask import Flask, jsonify, request, session, make_response
from flask_migrate import Migrate
from models import db, User
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = b'***************************************'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)
db.init_app(app)
bcrypt = Bcrypt(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    user = User(username, password, email)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

if __name__ == '__main__':
    app.run(port=5555, debug=True)
