import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# mongoDB config
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home_page")
def home_page():
    return render_template("index.html")


@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html",
                            recipes=recipes,
                            title="All Recipes")


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html",
                            recipes=recipes,
                            title="All Recipes")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if username DOES already exists in db
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # if username DOES NOT already exist in db then insert details
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "profile_img_url": request.form.get("profile_img_url")
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html",
                            title="Register")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesnt exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html",
                            title="Log In")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username & profile image url from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"].capitalize()
    profile_img = mongo.db.users.find_one(
        {"username": session["user"]})["profile_img"]

    if session["user"]:
        user = mongo.db.users.find_one({"username": session["user"]})
        return render_template("profile.html",
                                username=username,
                                profile_img=profile_img,
                                title="Profile")

    return redirect(url_for("login"))


@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
    if request.method == "POST":
        original_username = username
        username = username.lower()
        current_user = mongo.db.users.find_one({"username": username})
        current_user['profile_img'] = request.form.get("profile_img")
        mongo.db.users.update({"username": username}, current_user)
        flash("Profile Picture Updated")
        return redirect(url_for("profile", username=original_username))

    return render_template("edit_profile.html",
                            title="Edit Profile",
                            username=username)


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        is_vegan = "on" if request.form.get("is_vegan") else "off"
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "ingredients_measurements":
                request.form.getlist("ingredients_measurements"),
            "preparation_steps": request.form.getlist("preparation_steps"),
            "time": request.form.get("time"),
            "is_vegan": is_vegan,
            "recipe_img": request.form.get("recipe_img"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("New Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html",
                            categories=categories,
                            title="Add a Recipe")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        is_vegan = "on" if request.form.get("is_vegan") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "ingredients_measurements":
                request.form.getlist("ingredients_measurements"),
            "preparation_steps": request.form.getlist("preparation_steps"),
            "time": request.form.get("time"),
            "is_vegan": is_vegan,
            "recipe_img": request.form.get("recipe_img"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Edited")
        return redirect(url_for("get_recipes"))
        
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html",
                            recipe=recipe,
                            categories=categories,
                            title="Edit your Recipe")


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name"))
    return render_template("categories.html",
                            categories=categories,
                            title="Manage Categories")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html",
                            title="Add Category")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html",
                            category=category,
                            title="Edit Category")


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
