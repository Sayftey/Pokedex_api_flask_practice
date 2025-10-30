from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests




app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)





@app.route("/",methods=["POST","GET"])
def index():
    there = "False"
    ind = "0"
    structured_data = {}
    base_url = "https://pokeapi.co/api/v2/pokemon/"
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
    




@app.route("/search_type", methods=["POST","GET"])
def search_type():
    lis = []
    structured_data_type = {}
    base_url_type = "https://pokeapi.co/api/v2/type/"
    base_url_poke = "https://pokeapi.co/api/v2/pokemon/"
    if request.method == "POST":
        Type = request.form.get("Content")
        url_type = base_url_type + Type
        response_type = requests.get(url_type)
        if response_type.status_code == 200:
            structured_data_type = response_type.json()
            p = 0
            for i in structured_data_type['pokemon']:
                print(structured_data_type['pokemon'][p]['pokemon']['name'])
                url_poke = structured_data_type['pokemon'][p]['pokemon']['url']
                response_poke = requests.get(url_poke)
                structured_data_poke = response_poke.json()
                lis.append(structured_data_poke['sprites']['front_default'])
                print(lis[p])
                p +=1 


            
    return render_template("search_type.html", **structured_data_type,lis=lis)





@app.route("/search_ability", methods=["POST", "GET"])
def search_ability():
    lis = []
    structured_data_type = {}
    base_url_type = "https://pokeapi.co/api/v2/ability/"
    if request.method == "POST":
        Type = request.form.get("Content")
        url_type = base_url_type + Type
        response_type = requests.get(url_type)
        if response_type.status_code == 200:
            structured_data_type = response_type.json()
            p = 0
            for i in structured_data_type['pokemon']:
                print(structured_data_type['pokemon'][p]['pokemon']['name'])
                url_poke = structured_data_type['pokemon'][p]['pokemon']['url']
                response_poke = requests.get(url_poke)
                structured_data_poke = response_poke.json()
                lis.append(structured_data_poke['sprites']['front_default'])
                print(lis[p])
                p +=1 
    return render_template("search_ability.html",**structured_data_type, lis=lis)


if __name__ == "__main__":
    app.run(debug=True)