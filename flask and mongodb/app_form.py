from flask import Flask,jsonify, render_template, request, redirect, url_for

import pymongo
app = Flask(__name__, template_folder='templates')

# MongoDB connection

client=pymongo.MongoClient("mongodb+srv://shivamgangwar:Indianarmy2002@pymongo.quqwc2q.mongodb.net/?appName=pymongo")

db=client['Frontend']
collection=db['user_data']

@app.route("/form", methods=["GET","POST"])
def loadingData():
    if request.method=="POST":
        print("Received POST request. Attempting database connection/insert...")
        username=request.form.get("username")
        password=request.form.get("password")
    
        document = {
            'username': username,
            'password': password
        }
    
    # Insert the document into the collection
        try:
            collection.insert_one(document)
            print("Database insert successful!")
            message = f"Data submitted successfully for user: {username}!"
            return redirect(url_for('display_message', message=message))
        except Exception as e:
            message=f"An error occurred: {e}"
    return render_template("index.html")

@app.route("/message")
def display_message():
    # # Retrieve the 'message' argument passed via the URL query string
    message = request.args.get('message', "No status message provided.")
    
    # Render a new template to display the message
    return render_template("message.html", message=message)


if __name__=="__main__":
    app.run(debug=True)