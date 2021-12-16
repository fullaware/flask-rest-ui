import requests
from vehicles import *

# route to get all movies


@app.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    '''Function to get all the vehicles in the database'''
    return jsonify(Vehicles.get_all_vehicles())


# route to get vehicle by id
@app.route('/api/vehicles/<int:car_id>', methods=['GET'])
def get_vehicle_by_id(car_id):
    return_value = Vehicles.get_vehicle(car_id)
    return jsonify(return_value)


# route to add new vehicle
@app.route('/api/vehicles', methods=['POST'])
def add_vehicle():
    '''Function to add new vehicle to our database'''
    request_data = request.get_json()  # getting data from client
    print(request_data)
    Vehicles.add_vehicle(request_data["car_make"], request_data["car_model"],
                         request_data["car_year"], request_data["car_color"], request_data["car_hp"])
    response = Response("Vehicle added", 201, mimetype='application/json')
    return response


# route to update vehicle with PUT method
@app.route('/api/vehicles/<int:car_id>', methods=['PUT'])
def update_vehicle(car_id):
    '''Function to edit vehicle in our database using vehicle id'''
    request_data = request.get_json()
    Vehicles.update_vehicle(car_id, request_data["car_make"], request_data["car_model"],
                            request_data["car_year"], request_data["car_color"], request_data["car_hp"])
    response = Response("Vehicle Updated", status=200,
                        mimetype='application/json')
    return response


# route to delete vehicle using the DELETE method
@app.route('/api/vehicles/<int:car_id>', methods=['DELETE'])
def remove_vehicle(car_id):
    '''Function to delete vehicle from our database'''
    Vehicles.delete_vehicle(car_id)
    response = Response("Vehicle Deleted", status=200,
                        mimetype='application/json')
    return response

# route to search all vehicles by string


@app.route('/api/vehicles/search', methods=['POST'])
def search_vehicles():
    json_search = request.get_json()
    search_string = json_search['search']
    print(search_string)
    
    return Vehicles.search_all_vehicles(search_string)

@app.route('/api/vehicles/analytics', methods=['GET'])
def analyze_vehicles():
    '''Function to get all the vehicles in the database'''
    return jsonify(Vehicles.analyze_vehicles())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088, debug=True)
