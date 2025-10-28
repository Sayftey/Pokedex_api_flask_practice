from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests


base_url = "https://pokeapi.co/api/v2/pokemon/"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)





@app.route("/",methods=["POST","GET"])
def index():
    there = "False"
    ind = "0"
    structured_data = {}
    if request.method == "POST":
        pokemon = request.form.get("Content")
        url = base_url + pokemon
        response = requests.get(url)
        if response.status_code == 200:
            there = "True"
            structured_data = response.json()
            print(structured_data['name'])
            print(structured_data['id'])
            print(f"Height: {structured_data['height']}")
            print(structured_data['abilities'][0]['ability']['name'])
            if len(structured_data['abilities']) == 2:
                print(structured_data['abilities'][1]['ability']['name'])
                ind = "1"
                print(ind)
            print(structured_data['sprites']['back_default'])
            img_url = structured_data['sprites']['front_default']
            return render_template('index.html', **structured_data, there=there,img_url=img_url, ind=ind)
        else:
            print("error")
            there = "False"
    print(ind)
    return render_template('index.html', **structured_data, there=there)
    

    








if __name__ == "__main__":
    app.run(debug=True)