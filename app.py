import flask.json
import requests
import sqlite3 
import matplotlib.pyplot as plt
from flask import Flask
from flask import render_template, request, jsonify, make_response
from flask_json import FlaskJSON, JsonError, json_response
from matplotlib.figure import Figure

app = Flask(__name__)
json = FlaskJSON(app)


def get_db_connection():
    conn = sqlite3.connect('WingWalker_database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

# @app.route('/edit_data', methods=['GET','POST'])
# def r_data():
#     if request.method == "POST":
#         serial_id = request.form.get("serial_id")
#         print("id is")
#         print(serial_id)
#         conn = get_db_connection()
#         posts = conn.execute('SELECT * FROM first_table WHERE seiral_number = ?', [id]).fetchone()
#         print(posts)
#         data = {
#             'seiral_number' : posts['seiral_number'],
#             'Product_Name' : posts['Product_Name'],
#             'manufacturer' : posts['manufacturar'],
#             'material' : posts['material'],
#             'prod
# uction_year' : posts['production_year'],
#             'expiration' : posts['expiration']
#         }
#         json_object = flask.json.dumps(data, indent=4)
#         print(json_object)

#         with open("data.json", "w") as outfile:
#                outfile.write(json_object)
#         outfile.close()
#         conn.close()
#     else:
#         return  render_template('edit.html')
#     return render_template('edit.html' )

@app.route('/edit2_data', methods=['GET','POST'])
def r2_data():
    return render_template('edit.html' ) 

@app.route('/retrive_data1', methods=['GET','POST'])
def r1_data():
    filename = 'data.json'
    with open(filename, 'r+') as file:
            file_data = flask.json.load(file)
            seiral_number = file_data['seiral_number']
            Product_Name = file_data['Product_Name']
            manufacturer = file_data['manufacturer']
            material = file_data['material']
            production_year = file_data['production_year']
            expiration = file_data['expiration']
    file.close()

    return render_template('retrive_data.html', seiral_number="2001111", Product_Name=Product_Name, manufacturer=manufacturer, material=material, production_year=production_year, expiration=expiration)



@app.route('/upload_data', methods=['GET', 'POST'])
def u_data():
    if request.method == "POST":
        seiral_number = request.form.get("serial_id")
        Product_Name = request.form.get("Product_Name")
        manufacturer = request.form.get("manufacturer")
        material = request.form.get("material")
        production_year = request.form.get("production_year")
        expiration = request.form.get("expiration")

        conn = get_db_connection()
        conn.executemany("INSERT INTO first_table (seiral_number, Product_Name, manufacturar, material, production_year,expiration) VALUES (seiral_number,Product_Name, manufacturer, material, production_year, expiration)", seiral_number, Product_Name, manufacturer, material, production_year, expiration)


    return render_template('upload_data.html')




if __name__ == '__main__':
    app.run()
