from flask import Flask,request
from flask_restplus import Api,Namespace
import flask_restplus

app = Flask(__name__)
NS = Namespace('Simple API', description='Simple Demo App')
api = Api(app, version='1.0', title='Simple Users',
          description='Simple User API Requests')
api.add_namespace(NS, path="/flaskrest")  #What is this path?

ls=[{"id": 1,"name": "string"}]
model1 = api.model("Users", {
    'id': flask_restplus.fields.Integer(required=True, description="Id of the user"),
    'name': flask_restplus.fields.String(required=True, description="Name of User")
})

@NS.route("/Simple/")
class Simple(flask_restplus.Resource):
    def get(self):
        return ls

    @NS.expect(model1, validate=True)    #Hare expect of model act as payload to send json data as body
    def post(self):
        data=request.get_json()
        print(data)
        return ls.append(data)

@NS.route('/delete/<int:id>')     #Hare it accpet it as a parameter
class S1(flask_restplus.Resource):
    def delete(self,id):
        print(id)
        return "xxxx"

oo=S1()
if __name__ == '__main__':
   app.run(debug = True)

