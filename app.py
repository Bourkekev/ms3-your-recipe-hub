import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime

from os import path
if path.exists("env.py"):
   import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
def home_recipes():
   return render_template("index.html", recipes=mongo.db.recipes.find())


@app.route('/all_recipes')
def all_recipes():
   return render_template("all-recipes.html", recipes=mongo.db.recipes.find())


@app.route('/single_recipe/<recipe_id>')
def single_recipe(recipe_id):
   the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
   return render_template("single-recipe.html", recipe=the_recipe)


@app.route('/add_recipe', methods=["GET", "POST"])
def add_recipe():
   if request.method == "POST":
      recipe = {
         "title": request.form.get("title"),
         "category_name": request.form.get("category_name"),
         "course_name": request.form.get("course_name"),
         "short_description": request.form.get("short_description"),
         "ingredients": request.form.get("ingredients"),
         "method": request.form.get("method"),
         "portions": request.form.get("portions"),
         "prep_time": request.form.get("prep_time"),
         "cook_time": request.form.get("cook_time"),
         "chef_notes": request.form.get("chef_notes"),
         "nutrition": request.form.get("nutrition"),
         "date": datetime.utcnow(),
         "user_name": "Kevin"
      }
      mongo.db.recipes.insert_one(recipe)
      flash("Recipe successfully added.")
      return redirect(url_for("all_recipes"))

   categories = mongo.db.categories.find().sort("category_name", 1)
   courses = mongo.db.courses.find().sort("course_name", 1)
   return render_template("add_recipe.html", categories=categories, courses=courses)


@app.route('/edit_recipe/<recipe_id>', methods=["GET", "POST"])
def edit_recipe(recipe_id):
   the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

   categories = mongo.db.categories.find().sort("category_name", 1)
   courses = mongo.db.courses.find().sort("course_name", 1)
   return render_template("edit_recipe.html", recipe=the_recipe, categories=categories, courses=courses)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
           port=os.environ.get('PORT'),
           debug=True)
