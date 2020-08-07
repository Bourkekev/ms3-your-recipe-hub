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
   if request.method == "POST":
      overall_time = int(request.form.get("prep_time")) + int(request.form.get("cook_time"))
      submit_edit = {
         "title": request.form.get("title"),
         "category_name": request.form.get("category_name"),
         "course_name": request.form.get("course_name"),
         "short_description": request.form.get("short_description"),
         "ingredients": request.form.get("ingredients"),
         "method": request.form.get("method"),
         "portions": int(request.form.get("portions")),
         "prep_time": int(request.form.get("prep_time")),
         "cook_time": int(request.form.get("cook_time")),
         "chef_notes": request.form.get("chef_notes"),
         "total_time" : overall_time,
         "nutrition": request.form.get("nutrition"),
         "date": datetime.utcnow(),
         "user_name": "Kevin"
      }
      mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit_edit)
      flash("Recipe successfully updated.")

   the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
   categories = mongo.db.categories.find().sort("category_name", 1)
   courses = mongo.db.courses.find().sort("course_name", 1)
   return render_template("edit_recipe.html", recipe=the_recipe, categories=categories, courses=courses)


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
   mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
   flash("Recipe successfully deleted.")
   return redirect(url_for('all_recipes'))


@app.route('/get_categories')
def get_categories():
   categories = list(mongo.db.categories.find().sort("category_name", 1))
   return render_template("categories.html", categories=categories)


@app.route('/add_category', methods=["GET", "POST"])
def add_category():
   if request.method == "POST":
      category = {
         "category_name": request.form.get("category_name")
      }
      mongo.db.categories.insert_one(category)
      flash("New Category Added")
      return redirect(url_for('get_categories'))

   return render_template("add_category.html")


@app.route('/edit_category/<category_id>', methods=["GET", "POST"])
def edit_category(category_id):
   if request.method == "POST":
      submit_edit = {
         "category_name": request.form.get("category_name")
      }
      mongo.db.categories.update({"_id": ObjectId(category_id)}, submit_edit)
      flash("Category successfully updated")
      return redirect(url_for('get_categories'))

   category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
   return render_template("edit_category.html", category=category)
   

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
           port=os.environ.get('PORT'),
           debug=True)
