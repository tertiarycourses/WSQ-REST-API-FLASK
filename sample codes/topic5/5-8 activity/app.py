from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentss.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # change this IRL

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created!')

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')

@app.cli.command('db_seed')
def db_seed():
    student1 = Student(name='Alfred',
                     city='Singapore',
                     addr='Woodslands',
                     pin=1010)
    student2 = Student(name='Steve',
                     city='Singapore',
                     addr='Ang Mo Kio',
                     pin=1020)
    
    student3 = Student(name='Ally',
                     city='Malaysia',
                     addr='Kulua Lumpur',
                     pin=1030)
    
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.commit()
    print('Database seeded!')

@app.route('/students', methods=['GET'])
def students():
    students_list = Student.query.all()
    result = students_schema.dump(students_list)
    return jsonify(result)

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    test = Student.query.filter_by(email=email).first()
    if test:
        return jsonify(message='That email already exists.'), 409
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify(message="User created successfully."), 201

@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else:
        email = request.form['email']
        password = request.form['password']

    test = User.query.filter_by(email=email, password=password).first()
    if test:
        access_token = create_access_token(identity=email)
        return jsonify(message="Login succeeded!", access_token=access_token)
    else:
        return jsonify(message="Bad email or password"), 401

# Get data
@app.route('/student_details/<int:student_id>', methods=["GET"])
def student_details(student_id: int):
    student = Student.query.filter_by(student_id=student_id).first()
    if student:
        result = student_schema.dump(student)
        return jsonify(result.data)
    else:
        return jsonify(message="That student does not exist"), 404

# Add data with authorization
@app.route('/add_student', methods=['POST'])
@jwt_required()
def add_student():
    name = request.form['name']
    test = Student.query.filter_by(name=name).first()
    if test:
        return jsonify("There is already a student by that name"), 409
    else:
        city = request.form['city']
        addr = request.form['addr']
        pin = int(request.form['int'])

        new_studnet = Student(name=name,
                            city=city,
                            addr=addr,
                            pin=pin)

        db.session.add(new_student)
        db.session.commit()
        return jsonify(message="You added a student"), 201

# Update data with authorization
@app.route('/update_student', methods=['PUT'])
@jwt_required()
def update_student():
    student_id = int(request.form['student_id'])
    student = Student.query.filter_by(student_id=student_id).first()
    if student:
        student.name = request.form['name']
        student.city = request.form['city']
        student.addr = request.form['addr']
        student.pin = int(request.form['pin'])
        db.session.commit()
        return jsonify(message="You updated a student"), 202
    else:
        return jsonify(message="That student does not exist"), 404

# Delete data with authorization
@app.route('/remove_student/<int:student_id>', methods=['DELETE'])
@jwt_required()
def remove_student(student_id: int):
    student = Student.query.filter_by(student_id=student_id).first()
    if student:
        db.session.delete(student)
        db.session.commit()
        return jsonify(message="You deleted a student"), 202
    else:
        return jsonify(message="That student does not exist"), 404

# database models
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

class Student(db.Model):
    __tablename__ = 'students'
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    city = Column(String(50))
    addr = Column(String(200)) 
    pin = Column(String(10))
    
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'city', 'addr', 'pin')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

if __name__ == '__main__':
    app.run()