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
    

@app.route("/add_new_gym")
def add_new_gym():
    return render_template("add_gym.html")

# Sends the data that the user inserts to the database

@app.route("/insert_gym", methods=['POST'])
def insert_gym():
    gym = mongo.db.gyms
    gym.insert_one(request.form.to_dict())
    return redirect(url_for('get_gym_names'))


# Allows user to update information about a gym

@app.route("/edit_gym/<gym_id>")
def edit_gym(gym_id):
    the_gym = mongo.db.gyms.find_one({"_id": ObjectId(gym_id)})
    return render_template("update_gym.html", gym=the_gym)

# Delete option for a user if they wish to delete a review they wrote or delete a review written by someone else that may be incorrect

@app.route("/delete_gym/<gym_id>")
def delete_gym(gym_id):
    mongo.db.gyms.remove({'_id': ObjectId(gym_id)})
    return redirect(url_for('get_gym_names'))
    
@app.route("/leave_review")
def gym_review():
    return render_template("gym_review.html", gyms=mongo.db.gyms.find())    
    
# Sends the data that the user inserts to the database

@app.route("/gym_review", methods=['POST'])
def insert_review():
    review = mongo.db.reviews
    review.insert_one(request.form.to_dict())
    return redirect(url_for('gym_review'))


@app.route("/read_review")
def read_review():
    return render_template("read_reviews.html", reviews=mongo.db.reviews.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)