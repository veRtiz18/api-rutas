from flask import Flask, render_template, request, jsonify
import random
import googlemaps

app = Flask(__name__)

# Configura tu clave de API de Google Maps
gmaps = googlemaps.Client(key='AIzaSyAgIwoNsnI4JVgb-jGacBcRLiOd9JMLtRs')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_directions', methods=['POST'])
def get_directions():
    data = request.json
    origin = data.get('origin')
    destination = data.get('destination')
    waypoints = data.get('waypoints', [])
    travel_mode = data.get('travel_mode')

    if travel_mode == 'DRIVING':
        cost_per_toll = 50
        fuel_cost_per_liter = 20
        fuel_consumption_per_km = 0.1
    elif travel_mode == 'BICYCLING':
        cost_per_toll = 0
        fuel_cost_per_liter = 0
        fuel_consumption_per_km = 0
    elif travel_mode == 'WALKING':
        cost_per_toll = 0
        fuel_cost_per_liter = 0
        fuel_consumption_per_km = 0

    total_distance = data.get('total_distance')
    total_duration = data.get('total_duration')

    total_fuel_cost = total_distance * fuel_consumption_per_km * fuel_cost_per_liter
    number_of_tolls = int(total_distance / 100)
    total_toll_cost = number_of_tolls * cost_per_toll
    total_trip_cost = total_fuel_cost + total_toll_cost

    return jsonify({
        'origin': origin,
        'destination': destination,
        'waypoints': waypoints,
        'total_distance': total_distance,
        'total_duration': total_duration,
        'total_fuel_cost': total_fuel_cost,
        'total_toll_cost': total_toll_cost,
        'total_trip_cost': total_trip_cost
    })

if __name__ == '__main__':
    app.run(debug=True)
