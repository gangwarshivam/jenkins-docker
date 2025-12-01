from flask import Flask,jsonify

app = Flask(__name__)

DATA_PATH='data.txt'

def load_data():
    with open(DATA_PATH,'r') as file:
        lines=[line.strip() for line in file.readlines()]
        return lines

@app.route("/api")
def loadingData():
    data=load_data()
    return jsonify(data)

if __name__=="__main__":
    app.run(debug=True)