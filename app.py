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
    return render_template("gyms.html", gyms=mongo.db.gyms.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)