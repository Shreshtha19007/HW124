from flask import Flask,jsonify,request
app = Flask(__name__)
data = [
    {
        "Contact": 9987655432,
        "Name": "Kim",
        "id"  : 1,
        "done" : False
    },
    {
        "Contact": 9987655421,
        "Name": "Mia",
        "id"  : 2,
        "done" : False
    }
]
@app.route("/add-data",methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status": "error", 
            "message": "Please provide the data"
        },400)
    contact = {
    "id": tasks[-1]["id"]+ 1,
    "Name": request.json["Name"],
    "Contact": request.json.get("Contact",""),
    "done": False
    }
    tasks.append(task)
    return jsonify({
    "status": "success",
    "message": "task added successfully",
    
})


       

   

