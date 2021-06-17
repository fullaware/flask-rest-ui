from typing import Text
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.wrappers import response
from settings import *
import requests


@app.route('/')
def show_all():
    response = requests.get(api_endpoint)
    return render_template('show_all.html', vehicles=response.json())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['car_make'] or not request.form['car_model'] or not request.form['car_year']:
            flash('Please enter all the fields', 'error')
        else:
            r = request.form.to_dict()
            res = requests.post(api_endpoint, json=r)
            print(res.text)
            flash('Record was successfully added')

            return redirect(url_for('show_all'))
    return render_template('new.html')


@app.route('/delete/<int:car_id>', methods=['POST'])
def delete(car_id):
    uri_car_id = api_endpoint+'/'+str(car_id)
    print(uri_car_id)
    requests.delete(uri_car_id)

    flash('Vehicle was successfully deleted')

    return redirect(url_for('show_all'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':

        response = request.form
        
        headers = {
            'content-type': 'application/json',
            'content-length': str(len(response))
        }
        str_args = {
            'car_make': response['car_make'],
            'car_model': response['car_model'],
            'car_year': response['car_year'],
            'car_color': response['car_color'],
            'car_hp': response['car_hp']
        }

        json_args = json.dumps(str_args)

        uri_api_endpoint = api_endpoint+'/'+str(response['car_id'])

        requests.put(uri_api_endpoint, data=json_args, headers=headers)
        flash('Record was successfully updated')
        return redirect(url_for('show_all'))
    else:
        return redirect(url_for('show_all'))
    # return render_template('update.html', vehicle=car_id)

@app.route('/search', methods=['POST'])
def search():
    
    print(jsonify(request.args()))

    return redirect(url_for('show_all'))

if __name__ == "__main__":
    app.run(port=8088, debug=True)
