from requests.sessions import session
from api_settings import *
import json
from sqlalchemy import or_, func

# Initializing our database
db = SQLAlchemy(app)


# the class Vehicles will inherit the db.Model of SQLAlchemy
class Vehicles(db.Model):
    __tablename__ = 'car_demo'  # creating a table name
    car_id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    car_make = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    car_model = db.Column(db.Integer, nullable=False)
    car_year = db.Column(db.String(80), nullable=False)
    car_color = db.Column(db.String(80), nullable=False)
    car_hp = db.Column(db.String(80), nullable=False)

    def json(self):
        return {'car_id': self.car_id, 'car_make': self.car_make,
                'car_model': self.car_model, 'car_year': self.car_year,
                'car_color': self.car_color, 'car_hp': self.car_hp}
        # this method we are defining will convert our output to json

    def add_vehicle(_car_make, _car_model, _car_year, _car_color, _car_hp):
        '''function to add vehicle to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our Vehicle constructor
        new_vehicle = Vehicles(car_make=_car_make, car_model=_car_model, car_year=_car_year, car_color=_car_color, car_hp=_car_hp)
        db.session.add(new_vehicle)  # add new vehicle to database session
        db.session.commit()  # commit changes to session

    def get_all_vehicles():
        '''function to get all vehicles in our database'''
        return [Vehicles.json(vehicle) for vehicle in Vehicles.query.all()]

    def get_vehicle(_car_id):
        '''function to get vehicle using the id of the vehicle as parameter'''
        return [Vehicles.json(Vehicles.query.filter_by(car_id=_car_id).first())]
        # Vehicles.json() coverts our output to json
        # the filter_by method filters the query by the id
        # the .first() method displays the first value

    def update_vehicle(_car_id, _car_make, _car_model, _car_year, _car_color, _car_hp):
        '''function to update the details of a vehicle using the id, title,
        year and genre as parameters'''
        vehicle_to_update = Vehicles.query.filter_by(car_id=_car_id).first()
        vehicle_to_update.car_make = _car_make
        vehicle_to_update.car_model = _car_model
        vehicle_to_update.car_year = _car_year
        vehicle_to_update.car_color = _car_color
        vehicle_to_update.car_hp = _car_hp
        db.session.commit()

    def delete_vehicle(_car_id):
        '''function to delete a vehicle from our database using
           the id of the vehicle as a parameter'''
        print(_car_id)
        Vehicles.query.filter_by(car_id=_car_id).delete()
        # filter by id and delete
        db.session.commit()  # commiting the new change to our database
    
    def search_all_vehicles(_search):
        search = "%{}%".format(_search)

        return [Vehicles.json(vehicle) for vehicle in Vehicles.query.filter(or_(Vehicles.car_make.like(search),Vehicles.car_model.like(search))).all()]

    def analyze_vehicles():
        '''function to analyze all vehicles in our database'''
        
        avg_hp_row = db.session.query(func.avg(Vehicles.car_hp)).all()

        avg_hp_decimal = [x[0] for x in avg_hp_row]

        # color_count = Vehicles.query.count(Vehicles.car_color).all()
        color_count_row = db.session.query(Vehicles.car_color, func.count(Vehicles.car_color)).group_by(Vehicles.car_color).order_by(func.count(Vehicles.car_color).desc()).all()
        color_count_json = []

        for row in color_count_row:
            row_to_string = {row[0]:row[1]}
            color_count_json.append(row_to_string)
        
        payload = {
            'count' : Vehicles.query.count(),
            'avg_hp' : int(avg_hp_decimal[0]),
            'color_count' : color_count_json
        }
        
        return payload