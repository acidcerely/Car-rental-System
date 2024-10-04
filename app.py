from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/CarRentalSystem'
db = SQLAlchemy(app)

class Car(db.Model):
    car_id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.Integer)
    rental_price_per_day = db.Column(db.Numeric(10, 2))

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(15))

class Rental(db.Model):
    rental_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    car_id = db.Column(db.Integer, db.ForeignKey('car.car_id'))
    rental_start_date = db.Column(db.Date)
    rental_end_date = db.Column(db.Date)
    rental_status = db.Column(db.String(20))

class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    rental_id = db.Column(db.Integer, db.ForeignKey('rental.rental_id'))
    payment_amount = db.Column(db.Numeric(10, 2))
    payment_date = db.Column(db.Date)

@app.route('/cars', methods=['POST'])
def add_car():
    data = request.get_json()
    new_car = Car(make=data['make'], model=data['model'], year=data['year'], rental_price_per_day=data['rental_price_per_day'])
    db.session.add(new_car)
    db.session.commit()
    return jsonify({'message': 'Car added successfully'}), 201

@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    new_customer = Customer(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], phone=data['phone'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'message': 'Customer added successfully'}), 201

@app.route('/rentals', methods=['POST'])
def add_rental():
    data = request.get_json()
    new_rental = Rental(customer_id=data['customer_id'], car_id=data['car_id'], rental_start_date=data['rental_start_date'], rental_end_date=data['rental_end_date'], rental_status=data['rental_status'])
    db.session.add(new_rental)
    db.session.commit()
    return jsonify({'message': 'Rental added successfully'}), 201

@app.route('/payments', methods=['POST'])
def add_payment():
    data = request.get_json()
    new_payment = Payment(rental_id=data['rental_id'], payment_amount=data['payment_amount'], payment_date=data['payment_date'])
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({'message': 'Payment added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
