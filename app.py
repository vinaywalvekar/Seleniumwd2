from flask import Flask

app = Flask(__name__)


# From Server's perspective
#POST :- Receive Data
#GET :- Send data back


#Create code

#Post /store data :(name:)
@app.route('/store', methods=['POST'])
def create_store():
    pass

#Get  /store/string:name;
@app.route('/store/<string:name>')
def get_store(name):
    pass

#Get /store
@app.route('/store')
def get_store():
    pass

#Post /store/<string:name>, item{name: price}

#get /store/<String:name>/item


app.run(port=4999)
