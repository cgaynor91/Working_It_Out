{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":25,"position":25,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":23},"action":"insert","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":14,"column":23},"action":"remove","lines":["import os","from flask import Flask","","app = Flask(__name__)","","","@app.route('/')","def hello():","    return 'Hello World ...again'","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":2},{"start":{"row":0,"column":0},"end":{"row":21,"column":23},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId ","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'task_manager'","app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_tasks')","def get_tasks():","    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"]}],[{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"remove","lines":["r"],"id":3},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"remove","lines":["e"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"remove","lines":["g"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"remove","lines":["a"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"remove","lines":["n"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"remove","lines":["a"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"remove","lines":["m"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"remove","lines":["_"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"remove","lines":["k"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"remove","lines":["s"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"remove","lines":["a"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["t"]}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["w"],"id":4},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["o"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["r"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["k"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["i"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["n"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["g"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["_"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["i"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"insert","lines":["_"],"id":5},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"insert","lines":["o"]},{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"insert","lines":["u"]},{"start":{"row":6,"column":43},"end":{"row":6,"column":44},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":50},"end":{"row":7,"column":70},"action":"remove","lines":["mongodb://localhost'"],"id":6}],[{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"remove","lines":["'"],"id":7}],[{"start":{"row":7,"column":49},"end":{"row":7,"column":144},"action":"insert","lines":["mongodb+srv://root:<password>@myfirstcluster-ikccs.mongodb.net/test?retryWrites=true&w=majority"],"id":8}],[{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"insert","lines":["'"],"id":9}],[{"start":{"row":7,"column":145},"end":{"row":7,"column":146},"action":"insert","lines":["'"],"id":10}],[{"start":{"row":7,"column":78},"end":{"row":7,"column":79},"action":"remove","lines":[">"],"id":11},{"start":{"row":7,"column":77},"end":{"row":7,"column":78},"action":"remove","lines":["d"]},{"start":{"row":7,"column":76},"end":{"row":7,"column":77},"action":"remove","lines":["r"]},{"start":{"row":7,"column":75},"end":{"row":7,"column":76},"action":"remove","lines":["o"]},{"start":{"row":7,"column":74},"end":{"row":7,"column":75},"action":"remove","lines":["w"]},{"start":{"row":7,"column":73},"end":{"row":7,"column":74},"action":"remove","lines":["s"]},{"start":{"row":7,"column":72},"end":{"row":7,"column":73},"action":"remove","lines":["s"]},{"start":{"row":7,"column":71},"end":{"row":7,"column":72},"action":"remove","lines":["a"]},{"start":{"row":7,"column":70},"end":{"row":7,"column":71},"action":"remove","lines":["p"]},{"start":{"row":7,"column":69},"end":{"row":7,"column":70},"action":"remove","lines":["<"]}],[{"start":{"row":7,"column":69},"end":{"row":7,"column":70},"action":"insert","lines":["a"],"id":12},{"start":{"row":7,"column":70},"end":{"row":7,"column":71},"action":"insert","lines":["d"]},{"start":{"row":7,"column":71},"end":{"row":7,"column":72},"action":"insert","lines":["m"]},{"start":{"row":7,"column":72},"end":{"row":7,"column":73},"action":"insert","lines":["i"]},{"start":{"row":7,"column":73},"end":{"row":7,"column":74},"action":"insert","lines":["n"]},{"start":{"row":7,"column":74},"end":{"row":7,"column":75},"action":"insert","lines":["p"]},{"start":{"row":7,"column":75},"end":{"row":7,"column":76},"action":"insert","lines":["a"]},{"start":{"row":7,"column":76},"end":{"row":7,"column":77},"action":"insert","lines":["s"]},{"start":{"row":7,"column":77},"end":{"row":7,"column":78},"action":"insert","lines":["s"]},{"start":{"row":7,"column":78},"end":{"row":7,"column":79},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":78},"end":{"row":7,"column":79},"action":"remove","lines":["s"],"id":13}],[{"start":{"row":7,"column":115},"end":{"row":7,"column":116},"action":"remove","lines":["t"],"id":14},{"start":{"row":7,"column":114},"end":{"row":7,"column":115},"action":"remove","lines":["s"]},{"start":{"row":7,"column":113},"end":{"row":7,"column":114},"action":"remove","lines":["e"]},{"start":{"row":7,"column":112},"end":{"row":7,"column":113},"action":"remove","lines":["t"]}],[{"start":{"row":7,"column":112},"end":{"row":7,"column":113},"action":"insert","lines":["w"],"id":15},{"start":{"row":7,"column":113},"end":{"row":7,"column":114},"action":"insert","lines":["o"]},{"start":{"row":7,"column":114},"end":{"row":7,"column":115},"action":"insert","lines":["r"]},{"start":{"row":7,"column":115},"end":{"row":7,"column":116},"action":"insert","lines":["k"]},{"start":{"row":7,"column":116},"end":{"row":7,"column":117},"action":"insert","lines":["i"]},{"start":{"row":7,"column":117},"end":{"row":7,"column":118},"action":"insert","lines":["n"]},{"start":{"row":7,"column":118},"end":{"row":7,"column":119},"action":"insert","lines":["g"]},{"start":{"row":7,"column":119},"end":{"row":7,"column":120},"action":"insert","lines":["_"]}],[{"start":{"row":7,"column":112},"end":{"row":7,"column":120},"action":"remove","lines":["working_"],"id":16},{"start":{"row":7,"column":112},"end":{"row":7,"column":126},"action":"insert","lines":["working_it_out"]}],[{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"remove","lines":["s"],"id":17},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"remove","lines":["k"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"remove","lines":["s"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"remove","lines":["a"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"remove","lines":["t"]}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["g"],"id":18},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["y"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["m"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"remove","lines":["s"],"id":19},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":["k"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"remove","lines":["s"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"remove","lines":["a"]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"remove","lines":["t"]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["g"],"id":20},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["y"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["m"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":60},"end":{"row":15,"column":61},"action":"remove","lines":["s"],"id":21},{"start":{"row":15,"column":59},"end":{"row":15,"column":60},"action":"remove","lines":["k"]},{"start":{"row":15,"column":58},"end":{"row":15,"column":59},"action":"remove","lines":["s"]},{"start":{"row":15,"column":57},"end":{"row":15,"column":58},"action":"remove","lines":["a"]},{"start":{"row":15,"column":56},"end":{"row":15,"column":57},"action":"remove","lines":["t"]}],[{"start":{"row":15,"column":56},"end":{"row":15,"column":57},"action":"insert","lines":["g"],"id":22},{"start":{"row":15,"column":57},"end":{"row":15,"column":58},"action":"insert","lines":["y"]},{"start":{"row":15,"column":58},"end":{"row":15,"column":59},"action":"insert","lines":["m"]},{"start":{"row":15,"column":59},"end":{"row":15,"column":60},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"remove","lines":["s"],"id":23},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"remove","lines":["k"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"remove","lines":["s"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"remove","lines":["a"]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["t"]}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["g"],"id":24},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["y"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["m"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"remove","lines":["s"],"id":25},{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"remove","lines":["k"]},{"start":{"row":15,"column":42},"end":{"row":15,"column":43},"action":"remove","lines":["s"]},{"start":{"row":15,"column":41},"end":{"row":15,"column":42},"action":"remove","lines":["a"]},{"start":{"row":15,"column":40},"end":{"row":15,"column":41},"action":"remove","lines":["t"]}],[{"start":{"row":15,"column":40},"end":{"row":15,"column":41},"action":"insert","lines":["g"],"id":26},{"start":{"row":15,"column":41},"end":{"row":15,"column":42},"action":"insert","lines":["y"]},{"start":{"row":15,"column":42},"end":{"row":15,"column":43},"action":"insert","lines":["m"]},{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"insert","lines":["s"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":21,"column":23},"end":{"row":21,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":true,"wrapToView":true},"firstLineState":0},"timestamp":1580561497754,"hash":"151662d39a4088172509431815b5e641240e562c"}