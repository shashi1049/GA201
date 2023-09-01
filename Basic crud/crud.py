from flask import Flask,request,jsonify
user = {}
app = Flask(__name__)

@app.route('/add',methods=["POST"])
def postProperty():
    data = request.get_json()
    username = data.get("name")
    userpassword = data.get("password")
    flag = False
    for key in user:
      if key == username:
       flag = True
       break
    if flag == True:
       return jsonify({"msg" : "User is already present"})
    else:
       user[username] = userpassword
       return jsonify({"msg" : "User is added successfully", "userobj" : user}) 
    
@app.route('/read',methods=["GET"])
def GETProperty():
    
    return jsonify({ "userobj" : user}) 

@app.route('/update',methods=["PATCH"])
def UPDATEProperty():
    data = request.get_json()
    username = data.get("name")
    userpassword = data.get("password")
    flag = False
    for key in user:
      if key == username:
       flag = True
       break
    if flag == True:
       user[username] = userpassword
       return jsonify({"msg" : f"{username} passoword has been updated", "userobj" : user})
    else:
       
       return jsonify({"msg" : "User not found"}) 
    
@app.route('/delete',methods=["DELETE"])
def DELETEProperty():
    data = request.get_json()
    username = data.get("name")
    flag = False
    for key in user:
      if key == username:
       flag = True
       break
    if flag == True:
       del user[username]
       return jsonify({"msg" : f"{username} user has been deleted successfully", "userobj" : user})
    else:
       
       return jsonify({"msg" : "User not found"}) 

if __name__ == '__main__':
    app.run()