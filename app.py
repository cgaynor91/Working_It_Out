import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'working_it_out'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:adminpass@myfirstcluster-ikccs.mongodb.net/working_it_out?retryWrites=true&w=majority')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_gyms')
def get_gyms():
    return render_template("home.html", gyms=mongo.db.gyms.find())

@app.route("/about")
def about():
    return render_template("about.html")
    
# ADD_RIVER page:

@app.route("/add_new_gym")
def add_new_gym():
    return render_template("add_gym.html")

# This function POSTs the input data from the user, to the database:

@app.route("/insert_gym", methods=['POST'])
def insert_gym():
    river = mongo.db.gyms
    river.insert_one(request.form.to_dict())
    return redirect(url_for('get_gym_names'))


# Allows user to update information about a gym

@app.route("/edit_gym/<gym_id>")
def edit_gym(gym_id):
    the_gym = mongo.db.gyms.find_one({"_id": ObjectId(gym_id)})
    return render_template("update_gym.html", gym=the_gym)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)