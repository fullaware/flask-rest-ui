from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from api import *

@app.route('/')
def show_all():
   return render_template('show_all.html', vehicles = Vehicles.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['car_make'] or not request.form['car_model'] or not request.form['car_year']:
         flash('Please enter all the fields', 'error')
      else:
         vehicle = Vehicles(request.form['car_make'], request.form['car_model'],
            request.form['car_year'], request.form['car_color'], request.form['car_hp'])
         
         db.session.add(vehicle)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == "__main__":
    app.run(port=1234, debug=True)