import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
   import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'your_recipe_hub'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
def home_recipes():
   return render_template("index.html", recipes=mongo.db.recipes.find())


@app.route('/all_recipes')
def all_recipes():
   return render_template("all-recipes.html", recipes=mongo.db.recipes.find())

 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
           port=os.environ.get('PORT'),
           debug=True)
