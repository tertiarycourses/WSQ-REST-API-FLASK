from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
    
# Flask command lines
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created!')

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')

# database models
class Students(db.Model):
    __tablename__ = 'students'
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    city = Column(String(50))
    addr = Column(String(200)) 
    pin = Column(String(10))
    
if __name__ == '__main__':
    app.run(debug=True)



